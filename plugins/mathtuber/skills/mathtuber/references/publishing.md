# Publishing

Use the user's requested channel/visibility or an applicable saved policy. Do not infer public publication from possession of a token. Explicit publish authorization does not need a second plugin confirmation.

Create a restricted configuration outside the repository containing `{"token_path":"/absolute/path/to/existing/youtube_token.json"}`. The token is the Google authorized-user OAuth file. The publisher refreshes an existing token and verifies channel identity; it never prints token material. A new connection requires Google consent; do not borrow a different app's credentials.

Write an intent file with `channel_id`, `title`, `description`, `tags`, `privacy` (private/unlisted/public), `made_for_kids`, and `authorized: true` only when supported by the user's request/policy.

First inspect a concrete upload plan:

```sh
python3 "$ENGINE" publish --project "$PROJECT" --intent /path/intent.json --dry-run
```

Then execute an authorized upload:

```sh
python3 "$ENGINE" publish --project "$PROJECT" --intent /path/intent.json --credentials /path/credentials-config.json
```

Current final acceptance is required. The worker uploads privately, verifies processing, then sets the authorized visibility. The same video bytes and channel resume/reconcile the existing receipt even when metadata changes. An uncertain initialization stops rather than blindly duplicating a video. Changed video bytes create a new upload.

Visibility readback can lag the update. The worker retries reads for a bounded 15 seconds. `visibility_pending` retains the existing video ID and observed visibility; it is not evidence of a platform restriction. Reconcile that video's status before reporting it public or attempting another upload.

Daily API quota rejection produces `state: quota_wait`, `code: YOUTUBE_DAILY_QUOTA` and a UTC `retry_not_before`. Keep the receipt and accepted export. Before that time the worker returns the wait without contacting YouTube. Afterward, rerun the same publish command: a rejected initialization may start, while an existing resumable session is reconciled and resumed. `publish_batch.py` stops at the first quota wait with exit code 2, preserving earlier results; rerun the same batch after the wait. Existing video receipts prevent duplicate inserts. A reset is a retry opportunity, not a guarantee of success.

The API's documented daily reset is midnight Pacific Time; the worker adds ten minutes and accounts for daylight saving. On 2026-09-06 the official quota table describes a separate default 100-call daily `videos.insert` bucket, with other requests in other buckets. Account allocations can differ; do not infer remaining uploads from published-video counts or hard-code an old per-upload cost. A generic HTTP 429 alone does not establish daily quota exhaustion. [YouTube quota documentation](https://developers.google.com/youtube/v3/determine_quota_cost).

Receipts containing resumable session URLs are restricted local files; never paste them into public logs or commits. Public command results omit these URLs. A legacy `starting` receipt without a session remains `UPLOAD_UNCERTAIN`: only reconcile it after inspecting concrete evidence of a rejected initialization or finding the existing upload. Do not delete an uncertain receipt just to unblock the command. The plugin does not schedule its own wakeup; the host agent must use its scheduler or resume after the timestamp.

After publication or on handoff, independently verify the current batch with `python3 <root>/scripts/publication_status.py --batch /path/batch.json --credentials /path/credentials-config.json --output /path/publication-status.json`. It uses the same `projects` entries (`project` and `intent`) as the batch publisher and makes no video inserts or updates. A single video can use a one-entry batch. Each row binds the current export hash to its upload receipt and reports actual visibility and processing. `complete` requires both the requested visibility and successful processing; missing receipts, stale exports, missing videos and pending states remain incomplete. `--require-complete` returns exit code 2 for an incomplete report, suitable for a host workflow that must stop before counting a release. Do not count `quota_wait` or a locally saved published receipt as independent confirmation.

Unverified Google API projects may be restricted to private uploads. Report actual returned visibility. Long Shorts with active copyright claims may be blocked; do not assume background music is safe because it is short. Scheduled publishing and analytics are not yet implemented in v0.1.
