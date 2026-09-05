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

Unverified Google API projects may be restricted to private uploads. Report actual returned visibility. Long Shorts with active copyright claims may be blocked; do not assume background music is safe because it is short. Scheduled publishing and analytics are not yet implemented in v0.1.
