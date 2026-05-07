# Per-App Research Dossiers

One file per Sociaaal LLC app. Each dossier deepens the YAML row in `../known_paths.yaml` with audience research, past-creative observations, current cultural hooks, and a don't-do list.

The Winner Agent loads the relevant dossier on every run (Step 1 of the workflow). Updating these files improves agent output without changing the workflow.

## Filename → app mapping

| File | App |
|---|---|
| `babylab.md` | BabyLab |
| `celebs.md` | Celebs |
| `voicify.md` | Voicify |
| `fontmaker.md` | Fontmaker |
| `fontkey.md` | Fontkey |
| `litstick.md` | Litstick |
| `autopaste.md` | AutoPaste |
| `remindful.md` | Remindful |
| `toned.md` | Toned |
| `herome.md` | HeroMe |
| `rizz-god.md` | Rizz God |
| `cappuccino.md` | Cappuccino |
| `vibe.md` | Vibe |
| `caption-ai.md` | Caption AI |
| `dream-wise-ai.md` | Dream Wise AI |
| `holy-guides.md` | Holy Guides |
| `hot-spotsss.md` | hot spotsss |

## Dossier structure

Every file follows the same 10-section template:

1. **App at a glance** — one-line summary, category, scale
2. **Audience profile** — demographics, psychographics, where they hang out
3. **Core promise** — the one transformation a user gets
4. **Value props (ranked)** — why they keep coming back
5. **Past creative observations** — what we've shipped, formats already burned
6. **Cultural moments to ride** — current zeitgeist that maps to this app
7. **Format playbook** — what works / what doesn't
8. **Competitor context** — apps to differentiate from
9. **Don't-do list** — legal, brand, tone constraints
10. **Open research questions** — gaps to fill in next iteration

## Maintenance

When you ship a new batch and notice patterns:
- Update **Past creative observations** with the format you just shipped
- Update **Cultural moments to ride** if the trend has rotated
- Bump the plugin version (patch) and push

Open a PR or commit directly to `main` if you're the maintainer.
