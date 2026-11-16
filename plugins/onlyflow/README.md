# onlyflow

Posts our organic content through [OnlyFlow](https://onlyflow.io), which runs our TikTok and Instagram accounts on our own iPhones. We upload media and create tasks (posts, reels, stories); the iPhone posts them. OnlyFlow ships no CLI, so this plugin adds one over its API:

- **`scripts/onlyflow`.** A command-line client for OnlyFlow's API (`https://onlyflow.io/api/v1`, the routes its official MCP server uses). It shows status, accounts, iPhones and tasks, uploads media, creates and validates posts, plans times, reschedules, cancels and deletes, and reads stats. Python 3, standard library only.
- **The `onlyflow-carousel` skill.** Takes a finished carousel set (`01.png … NN.png` + `caption.txt`), picks the 6 slides an OnlyFlow post allows, validates it, and schedules it on our account after your go.

## Setup (once per person or environment)

1. Create a key in OnlyFlow › Settings › MCP (organization owner only). One key per tool; revoke it there if it leaks.
2. Put it in your environment as `ONLYFLOW_API_KEY`, never in chat or in a file in this repo:
   - **Claude Code on your machine:** add `export ONLYFLOW_API_KEY=onlyflow_...` to your shell profile, then open a new terminal.
   - **Claude Code on the web / cloud sessions:** the environment's settings (cloud environment menu in the session's title bar, then Edit) › environment variables › `ONLYFLOW_API_KEY`.
3. Install the plugin:
   ```
   /plugin marketplace update sociaaal-plugins
   /plugin install onlyflow@sociaaal-plugins
   ```
4. Check it: `plugins/onlyflow/scripts/onlyflow status`, or ask Claude "what's on OnlyFlow?".
5. Add the TikTok account in OnlyFlow itself (log it in on the iPhone). The API can't create accounts or log in.

## Usage

- "What's the status of our OnlyFlow iPhones and accounts?"
- "Schedule batch 3 on OnlyFlow, one a day at 8 am ET from Tuesday."
- "Move tomorrow's post to 7 pm" / "Cancel the C12 post."
- "How did last week's posts do on OnlyFlow?"

## Things to know

- **A post is 1–6 photos.** Our carousels run 8–10 slides, so each goes up as its best 6: the hook, the story beats with the keyboard slide, and the closing question.
- **30 minutes minimum between two tasks on the same iPhone**, at most 30 days ahead, times with a timezone offset.
- Every task is validated (`?validate=1`) before it's created, and `--dry-run` stops there.
- OnlyFlow's own MCP server is the alternative to this CLI: `claude mcp add -s user onlyflow -e ONLYFLOW_API_KEY=… -- npx -y onlyflow-mcp@latest`.
