from datetime import datetime, timezone
import json
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'plugins/mathtuber'))
from mathtuber.youtube_retry import quota_retry, waiting, public_receipt


class QuotaTests(unittest.TestCase):
    def error(self, reason='quotaExceeded', status=403, message='Daily quota'):
        return SimpleNamespace(resp=SimpleNamespace(status=status),content=json.dumps(
            {'error':{'message':message,'errors':[{'reason':reason}]}}))

    def test_reset_uses_pacific_day_and_daylight_saving(self):
        cases=[('2026-09-06T04:00:00+00:00','2026-09-06T07:10:00+00:00'),
               ('2026-01-06T04:00:00+00:00','2026-01-06T08:10:00+00:00'),
               ('2026-03-09T00:00:00+00:00','2026-03-09T07:10:00+00:00'),
               ('2026-11-02T00:00:00+00:00','2026-11-02T08:10:00+00:00')]
        for now,retry in cases:
            with self.subTest(now=now):
                self.assertEqual(quota_retry(self.error(),datetime.fromisoformat(now))['retry_not_before'],retry)

    def test_generic_or_malformed_errors_are_not_daily_quota(self):
        for error in (self.error('rateLimitExceeded',429,'Too many requests'),
                      self.error(status=500),SimpleNamespace(content=b'bad'),
                      SimpleNamespace(resp=SimpleNamespace(status=429),content=b'not json')):
            self.assertIsNone(quota_retry(error))

    def test_daily_upload_response_does_not_disclose_identifiers(self):
        result=quota_retry(self.error('rateLimitExceeded',429,'Video Uploads per day for private-project-marker'))
        self.assertEqual(result['code'],'YOUTUBE_DAILY_QUOTA')
        self.assertNotIn('private-project-marker',json.dumps(result))

    def test_wait_boundary_and_redaction(self):
        state={'state':'quota_wait','retry_not_before':'2026-09-06T07:10:00Z','session_uri':'secret'}
        self.assertTrue(waiting(state,datetime(2026,9,6,7,9,tzinfo=timezone.utc)))
        self.assertFalse(waiting(state,datetime(2026,9,6,7,10,tzinfo=timezone.utc)))
        self.assertNotIn('session_uri',public_receipt(state))


if __name__=='__main__':unittest.main()
