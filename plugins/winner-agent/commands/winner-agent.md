---
description: Produce 5 editor-ready video concepts (with 9 hook variations each) for a Sociaaal app
argument-hint: <App> — e.g. Celebs, BabyLab, Voicify, Litstick, Toned, Fontmaker, AutoPaste, HeroMe, "Rizz God", Cappuccino, Vibe, "Caption AI", "Dream Wise AI", "Holy Guides", Remindful, "hot spotsss", Fontkey
---

Run the **winner-agent** skill from this plugin for the Sociaaal app: **$ARGUMENTS**

Follow the full workflow defined in the skill's `SKILL.md`:

1. Read `${CLAUDE_PLUGIN_ROOT}/skills/winner-agent/known_paths.yaml` for the app's spec
2. Read `${CLAUDE_PLUGIN_ROOT}/skills/winner-agent/research/<app-slug>.md` for the deeper research dossier
3. Pull past creatives from Google Drive via Claude in Chrome MCP
4. Pull current trends from TikTok Creative Center, Meta Ad Library, and Instagram via the operator's Chrome
5. **PAUSE at Checkpoint 1** — show the operator the trends found + past-creative gaps + candidate angles, ask for redirection or approval before synthesis
6. Synthesize exactly 5 concept directions tied to the trends
7. **PAUSE at Checkpoint 2** — show the 5 concept names + 1-line rationales, ask for approval / replacement
8. For each approved concept, write the full package: SCRIPT, STORYBOARD, IMAGE_PROMPTS, VIDEO_PROMPTS, App_Footage_NEEDED, EDITOR_NOTES, and the 9-variant VARIATIONS matrix
9. **PAUSE at Checkpoint 3** — show estimated Higgsfield credit cost, ask for approval / partial / skip before generating any AI assets
10. Generate AI images and AI videos via Higgsfield MCP
11. Save everything into the team Drive at `Sociaaal/Winner Agent Outputs/<App>/<Year-Wxx>/<NN_Concept Name>/`
12. **PAUSE at Checkpoint 4** — show Drive folder URLs + cost summary, ask for sign-off before final report

If the app name is not in `known_paths.yaml`, ask the operator before proceeding.

If "hot spotsss" is the target, the dossier is intentionally thin — ask the operator to clarify positioning before generating concepts.

The 5 × 9 deliverable structure is non-negotiable. If you can't confidently produce 5 concepts, push back and ask the operator before degrading the batch.
