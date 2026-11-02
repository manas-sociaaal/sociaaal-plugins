---
name: tokportal-carousel
description: Schedule finished carousel sets (folders of 01.png … NN.png plus caption.txt) as TikTok or Instagram photo carousels on TokPortal-managed accounts, through the TokPortal CLI. Use when someone asks to post, schedule, publish or upload carousels or slideshows through TokPortal, to check TokPortal credits, accounts or bundles, or to order a new warmed TikTok account. Dry-runs every paid step first and never spends credits without the operator's explicit go.
---

# TokPortal carousel posting (CLI)

TokPortal runs real, warmed TikTok and Instagram accounts on local phones. We never log into those accounts: we hand TokPortal the media, caption, sound and a publishing window, and their account manager posts it.

Everything runs through the official CLI, `tokportal` (`@tokportal/cli` 0.1.2), from Bash. It reads the key from `TOKPORTAL_API_KEY`; never pass `--api-key` on the command line or print the key.

```
tokportal <command> [--id <uuid>] [--position <n>] [--body-file x.json | --body '<json>'] [--json]
```

Path parameters are flags (`--id`, `--position`), query parameters are flags (`--platform tiktok`), JSON bodies go in `--body-file`. `tokportal help` lists every command. If `tokportal` is not installed, run it as `npx -y @tokportal/cli@0.1.2 …`.

## Dry runs

The CLI has no dry-run flag. For every write that costs credits or creates something, run the same request through the plugin's helper first:

```
${CLAUDE_PLUGIN_ROOT}/scripts/tp-dry-run.sh <METHOD> <path> [body.json | --image <file> <bundle_id>]
```

It sends `X-TokPortal-Dry-Run: true`: full validation and the real price, nothing created, no credits debited. Show the operator `credits_would_charge` and anything refused, then run the real `tokportal` command only on their go. Identifiers a dry run returns are synthetic; never reuse them in a real call.

## Before anything

1. `tokportal get-current-user` and `tokportal get-credit-balance`. Exit code 3 or `AUTH_INVALID_KEY` means the key is missing or wrong: tell the operator to set `TOKPORTAL_API_KEY` (a key from app.tokportal.com/developer) in their environment, and stop.
2. `tokportal list-accounts --platform tiktok` and `tokportal list-bundles` to see which accounts exist and which bundles post to them. Name accounts by their username to the operator, never by id.

## Money rules

- Credits are debited when a bundle is **created**, and there is no refund. `tokportal create-bundle` / `create-bundles-bulk` run for real only after the dry run's price has been shown and the operator said go in chat. `tokportal get-credit-costs` shows the price list.
- Paid per-post options stay off unless asked: `volume_original_sound`, `volume_added_sound`, `story_repost_url`, `instant_repost_as_story`.
- Never run `tokportal reveal-account-credentials`: revealing takes the account out of TokPortal's management and coverage.

## Where posts go

- A **bundle** is one account's order. One bundle posts to exactly one account.
- New account: `create-bundle` with `{"bundle_type":"account_and_videos","platform":"tiktok","country":"USA","videos_quantity":<posts planned>,"wants_advanced_warming":true,"advanced_warming_terms":["texting tips","rizz","college dating"]}` (3, 6 or 9 niche terms). The first possible posting day is today + 3 (UTC).
- An existing account: `{"bundle_type":"videos_only","account_id":"<id>", …}`. The first possible posting day is today + 1. The account needs active TokPortal Coverage (`tokportal get-account-managed-subscription --id <account>`).
- More posts on an existing bundle: `tokportal add-video-slots --id <bundle> --body-file slots.json` (dry run first).

## Schedule one carousel set

Input: a set folder with `01.png … NN.png` in upload order and `caption.txt` (the Drive layout `<week>/<App>/<set>/`).

1. Upload each slide in file order:
   `tokportal upload-image-direct --file 01.png --bundle-id <bundle> --purpose carousel --json`
   Keep the returned **`storage_path`**, not `public_url`, in slide order.
2. Write the slot body to a file, e.g. `slot.json`:
   ```json
   {
     "video_type": "carousel",
     "carousel_images": ["<storage_path 01>", "<storage_path 02>", "…"],
     "description": "<caption.txt, max 2200 characters>",
     "tiktok_sound_url": "<TikTok sound link>",
     "target_publish_date": "YYYY-MM-DD",
     "ai_content_disclaimer": true
   }
   ```
   - `tiktok_sound_url` is required for TikTok carousels. Ask the operator which trending sound to use if the set doesn't name one.
   - `target_publish_date` is the first day of a two-day window (the manager posts that day or the next). At most 3 posts per day per bundle.
   - `ai_content_disclaimer: true` is always on: our slides use AI-generated photos, and this has the manager switch on TikTok's AI-generated content label.
3. Dry run, then configure:
   `tp-dry-run.sh PUT /bundles/<bundle>/videos/<position> slot.json` → on go, `tokportal configure-bundle-video --id <bundle> --position <n> --body-file slot.json`.
   Several sets at once: `batch-configure-bundle-videos --id <bundle> --body-file batch.json` with `{"videos":[{…,"position":1},…]}`; it answers 200 even when rows fail, so read `configured`, `results` and `errors[]`.
4. Read `ignored_fields` in every response. An empty list is the only proof everything was stored.
5. `tokportal get-bundle-publish-readiness --id <bundle>`, then publish (dry run first): `tokportal publish-bundle-video --id <bundle> --position <n>` or `tokportal publish-all-bundle-videos --id <bundle>`. Dates already in the past move forward automatically; report any `adjusted_videos`.

## After posting

- Results: `tokportal list-account-video-analytics --id <account>` and `tokportal get-analytics-dashboard`.
- Comments asking for "pt 2" are the signal for the next part. Report them; replying through `tokportal create-comment-tasks` is a paid action and needs the operator's go like any other spend.

## Report back

One short summary: which account, which sets on which dates, the AI label set, credits spent (real calls only), and anything TokPortal refused or moved.
