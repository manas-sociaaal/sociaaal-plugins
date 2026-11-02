# tokportal

Posts our organic content through [TokPortal](https://tokportal.com), which runs warmed, locally operated TikTok and Instagram accounts and posts the content we give it. It uses TokPortal's official CLI, so it needs no MCP setup and no restart. Adds:

- **The `tokportal-carousel` skill.** It takes a finished carousel set (`01.png … NN.png` + `caption.txt`) and schedules it as a TikTok photo carousel through the `tokportal` CLI, with the AI-content label on. It never spends credits without your go.
- **`scripts/tp-dry-run.sh`.** The CLI has no dry-run flag, so this sends the same request with TokPortal's dry-run header. It validates and prices any write without creating anything or spending credits. The skill runs it before every paid step.

## Setup (once per person or environment)

1. Get an API key at app.tokportal.com/developer, signed in to the Sociaaal TokPortal account.
2. Put it in your environment as `TOKPORTAL_API_KEY`, never in chat or in a file in this repo:
   - **Claude Code on your machine:** add `export TOKPORTAL_API_KEY=sk_...` to your shell profile, then open a new terminal.
   - **Claude Code on the web / cloud sessions:** the environment's settings (cloud environment menu in the session's title bar, then Edit) → environment variables → `TOKPORTAL_API_KEY`. New sessions pick it up.
3. Install the CLI: `npm i -g @tokportal/cli@0.1.2` (Node 18+). Cloud sessions can add that line to the environment's setup script. Without it, the skill falls back to `npx -y @tokportal/cli@0.1.2`.
4. Install the plugin:
   ```
   /plugin marketplace update sociaaal-plugins
   /plugin install tokportal@sociaaal-plugins
   ```
5. Check it: `tokportal get-credit-balance` in a terminal, or ask Claude "what's my TokPortal credit balance?".

## Usage

- "Schedule the four Dre carousels on our TikTok account, one a day from Thursday"
- "How many TokPortal credits do we have and what does a new US TikTok account cost?"
- "How did last week's carousels do?"

## Guardrails

- Credits are charged when an account order (bundle) is created, with no refunds, so every order is dry-run first and confirmed in chat.
- `ai_content_disclaimer` is always set on our posts, because the photos are AI-generated.
- Account credentials are never revealed (revealing removes TokPortal's management and coverage).
- TokPortal's MCP server (`claude mcp add tokportal -e TOKPORTAL_API_KEY=… -- npx -y tokportal-mcp`) is an alternative with dry runs built in; this plugin doesn't need it.
