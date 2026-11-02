# tokportal

Connects Claude Code to [TokPortal](https://tokportal.com), which runs warmed, locally operated TikTok and Instagram accounts and posts the content we give it. Adds:

- **The TokPortal MCP server** (`tokportal-mcp`, TokPortal's official package, pinned to 1.22.0): 108 `tokportal_*` tools for accounts, bundles, uploads, scheduling, analytics, comments and credits.
- **The `tokportal-carousel` skill**: takes a finished carousel set (`01.png … NN.png` + `caption.txt`) and schedules it as a TikTok photo carousel. It runs a dry run first, turns the AI-content label on, and never spends credits without your go.

## Setup (once per person or environment)

1. Get an API key at app.tokportal.com/developer, signed in to the Sociaaal TokPortal account.
2. Put it in your environment as `TOKPORTAL_API_KEY`, never in chat or in a file in this repo:
   - **Claude Code on your machine:** add `export TOKPORTAL_API_KEY=sk_...` to your shell profile, then open a new terminal.
   - **Claude Code on the web / cloud sessions:** the environment's settings (cloud environment menu in the session's title bar, then Edit) → environment variables → `TOKPORTAL_API_KEY`. New sessions pick it up.
3. Install the plugin:
   ```
   /plugin marketplace update sociaaal-plugins
   /plugin install tokportal@sociaaal-plugins
   ```
4. Restart Claude Code, then ask "what's my TokPortal credit balance?". A working setup calls `tokportal_get_credit_balance`.

Needs Node 18+ (the server runs through `npx`).

## Usage

- "Schedule the four Dre carousels on our TikTok account, one a day from Thursday"
- "How many TokPortal credits do we have and what does a new US TikTok account cost?"
- "How did last week's carousels do?"

## Guardrails

- Credits are charged when an account order (bundle) is created, with no refunds, so every order is dry-run first and confirmed in chat.
- `ai_content_disclaimer` is always set on our posts, because the photos are AI-generated.
- Account credentials are never revealed (revealing removes TokPortal's management and coverage).
