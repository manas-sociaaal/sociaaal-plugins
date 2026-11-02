---
name: tokportal-carousel
description: Schedule finished carousel sets (folders of 01.png … NN.png plus caption.txt) as TikTok or Instagram photo carousels on TokPortal-managed accounts. Use when someone asks to post, schedule, publish or upload carousels or slideshows through TokPortal, to check TokPortal credits, accounts or bundles, or to order a new warmed TikTok account. Runs every write as a dry run first and never spends credits without the operator's explicit go.
---

# TokPortal carousel posting

TokPortal runs real, warmed TikTok and Instagram accounts on local phones. We never log into those accounts: we hand TokPortal the media, caption, sound and a publishing window, and their account manager posts it. Everything goes through the `tokportal_*` MCP tools from this plugin.

## Before anything

1. `tokportal_get_current_user` and `tokportal_get_credit_balance`. If they fail with an auth error, the API key is missing: tell the operator to add `TOKPORTAL_API_KEY` (a key from app.tokportal.com/developer) to their environment, and stop.
2. `tokportal_list_accounts` (platform `tiktok`) and `tokportal_list_bundles` to see which accounts exist and which bundles post to them. Name accounts by their username to the operator, never by id.

## Money rules

- Credits are debited when a bundle is **created**, and there is no refund. Never call `tokportal_create_bundle` or `tokportal_create_bundles_bulk` for real until the operator has seen the dry-run price (`credits_would_charge`) and said go in chat.
- Every write (`create_*`, `upload_*`, `configure_*`, `publish_*`) runs first with `dry_run: true`. Show the operator what would happen and what it would cost, then repeat it for real only on their go.
- Paid per-post options stay off unless asked: `volume_original_sound`, `volume_added_sound`, `story_repost_url`, `instant_repost_as_story`.
- Never call `tokportal_reveal_account_credentials`: revealing takes the account out of TokPortal's management and coverage.

## Where posts go

- A **bundle** is one account's order. One bundle posts to exactly one account.
- New account: `bundle_type: account_and_videos`, `platform: tiktok`, `country: USA`, `videos_quantity` = number of posts planned, with Advanced Niche Warming (`wants_advanced_warming: true` plus 3, 6 or 9 `advanced_warming_terms` for the niche, e.g. "texting tips", "rizz", "college dating"). The first possible posting day is today + 3 (UTC).
- An account that already exists: `bundle_type: videos_only` with its `account_id`. The first possible posting day is today + 1. The account needs active TokPortal Coverage (`tokportal_get_account_managed_subscription`).
- Add slots to an existing bundle with `tokportal_add_video_slots` (dry run first).

## Schedule one carousel set

Input: a set folder with `01.png … NN.png` in upload order and `caption.txt` (the Drive layout `<week>/<App>/<set>/`).

1. Upload each slide in file order with `tokportal_upload_image_direct` (`file_path`, `bundle_id`, `purpose: carousel`). Keep the returned **`storage_path`**, not `public_url`. Keep the order: slide 01 first.
2. Configure the slot with `tokportal_configure_bundle_video` (or `tokportal_batch_configure_bundle_videos` for several sets):
   - `video_type: carousel`
   - `carousel_images`: the storage paths in slide order
   - `description`: the full caption.txt text (max 2,200 characters)
   - `tiktok_sound_url`: a TikTok sound link. It is required for TikTok carousels. Ask the operator which trending sound to use if the set doesn't name one.
   - `target_publish_date`: `YYYY-MM-DD`, the first day of a two-day window (the manager posts that day or the next). At most 3 posts per day per bundle.
   - `ai_content_disclaimer: true`: our slides use AI-generated photos, and this has the manager switch on TikTok's AI-generated content label. Always on.
3. Read `ignored_fields` and `errors[]` in every response. An empty `ignored_fields` is the only proof everything was stored. Batch calls answer 200 even when rows fail.
4. `tokportal_get_bundle_publish_readiness`, then `tokportal_publish_bundle_video` (one slot) or `tokportal_publish_all_bundle_videos`, dry run first. Dates already in the past move forward automatically; report any `adjusted_videos` to the operator.

## After posting

- Results: `tokportal_list_account_video_analytics` and `tokportal_get_analytics_dashboard` per account.
- Comments asking for "pt 2" are the signal for the next part. Report them; replying through `tokportal_create_comment_tasks` is a paid action and needs the operator's go like any other spend.

## Report back

One short summary: which account, which sets on which dates, the AI label set, credits spent (real calls only), and anything TokPortal refused or moved.
