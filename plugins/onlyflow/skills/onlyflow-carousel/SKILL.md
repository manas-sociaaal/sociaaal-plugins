---
name: onlyflow-carousel
description: Post our finished carousel sets (folders of 01.png … NN.png plus caption.txt) as TikTok or Instagram photo posts on our own iPhones through OnlyFlow, from the command line. Use when someone asks to post, schedule or queue carousels or slideshows on OnlyFlow, to check OnlyFlow accounts, iPhones, tasks or stats, or to warm up an account on OnlyFlow. Validates every task before creating it and gets the operator's go before anything is scheduled.
---

# OnlyFlow carousel posting (CLI)

OnlyFlow drives our TikTok and Instagram accounts on our own iPhones. We upload media and create **tasks** (a Post, Reel or Story for an account, at a time); the iPhone carries the task out. Accounts are added and logged in inside OnlyFlow itself: the API cannot create accounts, log in or touch an iPhone directly.

Everything runs through the plugin's CLI, `${CLAUDE_PLUGIN_ROOT}/scripts/onlyflow` (Python 3, standard library). It reads the key from `ONLYFLOW_API_KEY`; never pass the key on the command line or print it. `onlyflow --help` lists every command.

## Before anything

`onlyflow status`: organization, iPhones (online or not), accounts, and scheduled or overdue tasks.
- No accounts listed: the TikTok account has not been added in OnlyFlow yet. Stop and say so; nothing can be posted until it is.
- An iPhone offline or with a connection issue: tasks on it go overdue. Say so before scheduling.

## Rules OnlyFlow enforces

A violation refuses the whole call and changes nothing.
- **A Post is 1–6 photos.** Our sets run 8–10 slides, so pick 6: always the hook (01) and the last slide (the comment question), plus the four slides that carry the story, with the RizzGod keyboard slide among them. Pass them with `--slides 1,…`.
- At least **30 minutes between two tasks on the same iPhone**. Use `onlyflow plan` for conflict-free times, or `onlyflow tasks --status scheduled` before picking times.
- Times are ISO 8601 **with the offset** (`2026-11-18T08:00:00-05:00`) and the IANA zone (`--tz America/New_York`), at most 30 days ahead. Without `--at` the task is created as Ready and only runs with `onlyflow run-now`.
- Images are centre-cropped to the ratio and never edited otherwise. Use `--ratio 9:16` for our 1080×1920 slides (full screen on TikTok).
- `--music` is the name of a sound, which the iPhone searches for and adds. Use the exact sound title.
- A warm-up (`--warmup`, optionally `--niche "texting"`) is an AI scroll of the feed before posting. At most 10 per iPhone per day.

## Post one carousel set

Input: a set folder with `01.png … NN.png` in upload order and `caption.txt` (the Drive layout `<week>/<App>/<set>/`).

1. Check it first, which uploads and validates but creates nothing:
   `onlyflow set <folder> --account @<username> --slides 1,2,3,6,8,9 --music "<sound title>" --at <ISO time> --tz America/New_York --dry-run`
2. Show the operator the plan (account, time, the 6 slides, caption, sound) and wait for their go in chat.
3. Then the same command without `--dry-run`. Keep the task id it prints.
4. `onlyflow task <id>` to confirm what was stored. `onlyflow tasks --status scheduled` lists the queue.

A week of sets is one command per set, spaced by `onlyflow plan`. Captions follow the organic rules: no app name. The app shows only as the keyboard in the screenshots, and the caption asks the same question as the last slide.

## Change or stop

- `onlyflow reschedule <id> <ISO time>` moves a task; `onlyflow cancel <id>` keeps it restorable (`onlyflow restore <id>`).
- `onlyflow delete <id> … --yes` removes tasks for good. Get the operator's OK first. A running task cannot be deleted.

## After posting

- `onlyflow tasks --status done,failed,overdue`: a failed or overdue task carries its reason (iPhone offline, account paused, scroll limit).
- Results come from the nightly scan: `onlyflow stats --days 7` and `onlyflow videos --account @<username>`.

## Report back

One short summary: which account, which sets on which times, slide picks, task ids, and anything OnlyFlow refused.
