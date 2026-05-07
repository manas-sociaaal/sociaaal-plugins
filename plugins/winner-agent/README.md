# Winner Agent — Sociaaal LLC

A Claude Code plugin for the Sociaaal team. Produces editor-ready video creative packages for any of our 17 consumer AI apps.

Drop the app name, get back **5 concept folders** with:
- Full vertical-video scripts (timed shot lists)
- Image generation prompts (NanoBanana)
- Video generation prompts (Kling 3.0, Seedance 2.0, Kling Motion Control)
- Generated AI images and AI video clips
- App footage / real-footage checklist for the editor
- Editor notes (vibe, pacing, music, transitions)
- **9 hook variations per concept** for A/B testing (45 deliverables per run)

A typical run takes 5–15 minutes and produces a Drive folder ready for the video editor.

---

## Installation

In Claude Code:

```
/plugin install winner-agent
```

Or if installing from a `.plugin` file received over Slack/email, drop the file into Claude Code — it presents an install button.

---

## Prerequisites (per team member)

The plugin's skill assumes these are connected on the operator's machine. If any are missing, the skill flags it during the run.

| Requirement | How to set up |
|---|---|
| **Higgsfield MCP** | In Claude Code, run `/mcp add higgsfield`. Sign in. Ask Manas to add you to the Sociaaal shared workspace. |
| **Claude in Chrome MCP** | Install the browser extension from `https://claude.ai/browser-extension`. In Claude Code it'll appear as available. |
| **Sociaaal Drive access** | You should already be a member of the `CREATIVES: ALL ASSETS` shared drive. If not, ping Manas. |
| **Sociaaal Chrome profile** | A Chrome profile signed into: Sociaaal Google account (for Drive), TikTok Creative Center, Meta Ad Library. The skill picks this profile when it asks at run-start. |

---

## Usage

After install, in any Claude Code session:

```
/winner-agent Celebs
```

Or natural language:

> "Run winner-agent for BabyLab"
> "Pull weekly creative concepts for Voicify"
> "Get me 3 video concepts for Litstick"

The skill executes a 6-step workflow: setup → past-creatives intel → trend research → concept synthesis → asset generation → editor handoff.

Output lands in `Sociaaal / Winner Agent Outputs / <App> / <Year-Wxx>/` on the team Drive. Read `00_INDEX.md` first, then `TEAM_HANDOFF.md`, then pick 2–3 concepts to push to production.

---

## Apps the plugin supports

All 17 Sociaaal LLC apps:

BabyLab, Celebs, Voicify, Fontmaker, Litstick, AutoPaste, Toned, HeroMe, Rizz God, Cappuccino, Vibe, Caption AI, Dream Wise AI, Holy Guides, Remindful, hot spotsss, Fontkey.

Each app has its own spec (category, audience, format strengths/weaknesses, AI-asset fit) baked into `known_paths.yaml`. The skill reads the relevant row before writing concepts so output is shaped to the app — never generic.

---

## Cost per run

| Item | Cost |
|---|---|
| Claude (LLM thinking) | $1.50–3.00 |
| Higgsfield credits (10 images + 8 videos) | 150–400 credits (~$3–8) |
| **Per-run total** | **~$5–12** |

Across 4 team members running weekly for 5 apps each → ~$200–250/mo total. Compared to an outsourced creative strategist + AI artist for the same volume (~$3K–6K/mo), this is a 15–30× cost reduction.

---

## Maintenance

- **App spec updates:** edit `skills/winner-agent/known_paths.yaml` → bump plugin version → repackage
- **Workflow changes:** edit `skills/winner-agent/SKILL.md`
- **New helper scripts:** add to `skills/winner-agent/scripts/`

After any change, repackage with:
```bash
cd ~/Downloads/winner-agent-plugin && zip -r /tmp/winner-agent.plugin . -x "*.DS_Store"
```

Distribute the new `.plugin` file to the team.

---

## Privacy

The plugin runs locally on each team member's machine using their own credentials. It does NOT:
- Send Drive contents anywhere except back to your Drive
- Store Anthropic / Higgsfield tokens persistently (only reads from session env)
- Touch personal Chrome profiles other than the one selected per run

The only "shared" surface is the team Drive itself + the team Higgsfield workspace.

---

## Maintainer

Manas Gaikwad — Gen AI Creative Performance Director, Sociaaal LLC.

For issues, edits, or new app spec additions, ping Manas directly.
