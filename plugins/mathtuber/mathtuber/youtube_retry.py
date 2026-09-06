"""Sanitized daily-quota classification and Pacific reset times; no credentials."""
from datetime import datetime, timedelta, timezone
import json
from zoneinfo import ZoneInfo


def quota_retry(error, now=None):
    """Return a wait only for a definite API daily-quota response.

    A generic 429 can be a short rate limit; it does not establish a daily cap.
    Error text can contain cloud project identifiers, so never return it.
    """
    status = getattr(getattr(error, 'resp', None), 'status', None)
    if status not in (403, 429):
        return None
    try:
        payload = json.loads(error.content)['error']
        reasons = {item.get('reason') for item in payload.get('errors', [])}
        message = payload.get('message', '').lower()
    except (ValueError, TypeError, KeyError, AttributeError):
        return None
    daily_uploads = ('ratelimitexceeded' in {str(x).lower() for x in reasons}
                     and 'video uploads' in message and 'per day' in message)
    if 'quotaExceeded' not in reasons and not daily_uploads:
        return None
    now = now or datetime.now(timezone.utc)
    local = now.astimezone(ZoneInfo('America/Los_Angeles'))
    tomorrow = local.date() + timedelta(days=1)
    # A ten-minute buffer avoids a burst exactly at the documented reset.
    retry = datetime.combine(tomorrow, datetime.min.time(), local.tzinfo) + timedelta(minutes=10)
    return {'code': 'YOUTUBE_DAILY_QUOTA',
            'retry_not_before': retry.astimezone(timezone.utc).isoformat()}


def waiting(state, now=None):
    if state.get('state') != 'quota_wait':
        return False
    retry = datetime.fromisoformat(state['retry_not_before'].replace('Z', '+00:00'))
    return (now or datetime.now(timezone.utc)) < retry


def public_receipt(state):
    """Resumable session URLs are credentials; retain them only on disk."""
    return {key: state[key] for key in ('state', 'video_id', 'url', 'privacy',
            'intent_id', 'code', 'retry_not_before') if key in state}
