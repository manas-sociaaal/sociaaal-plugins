# Sociaaal Plugins — Claude Code Marketplace

Internal Claude Code plugin marketplace for the Sociaaal LLC team. Add this marketplace once and you get one-command install + auto-updates for every plugin we ship.

---

## For team members — one-time setup (~2 min)

In any Claude Code session:

```
/plugin marketplace add sociaaal-llc/sociaaal-plugins
```

(Or whatever the GitHub org/repo path is — Manas will confirm.)

Then install whichever plugins you need:

```
/plugin install winner-agent@sociaaal-plugins
```

That's it. To update later, run:

```
/plugin marketplace update sociaaal-plugins
```

Or just reinstall: `/plugin install winner-agent@sociaaal-plugins` — Claude Code grabs the latest version automatically.

---

## Plugins available

### winner-agent

Produces editor-ready video creative packages for any of our 17 consumer AI apps. Trend research → script + prompts → AI asset generation → 9 hook variants per concept → Drive folder ready for the editor.

**Usage:** `/winner-agent Celebs` (or any app name)
**Cost:** ~$5–12 per run
**Time:** 5–15 min

Full docs: see [`plugins/winner-agent/README.md`](plugins/winner-agent/README.md)

**Per-member prerequisites:**
- Higgsfield MCP connected (shared workspace — Manas adds you)
- Claude in Chrome MCP + browser extension installed
- Sociaaal Drive access (already shared)
- Chrome profile signed in to Sociaaal Google + TikTok Creative Center + Meta Ad Library

---

## For maintainers — how to update a plugin

When you change a plugin (edit `SKILL.md`, update `known_paths.yaml`, add a script, etc.):

1. Bump the version in the plugin's `.claude-plugin/plugin.json` (semver)
2. Update the `version` field in this repo's `.claude-plugin/marketplace.json`
3. Commit and push:
   ```bash
   git add .
   git commit -m "winner-agent: <what you changed>"
   git push
   ```
4. Team members run `/plugin marketplace update sociaaal-plugins` to pull the new version (or it picks up automatically next time they `/plugin install`)

### Adding a new plugin to this marketplace

1. Drop the plugin folder under `plugins/<plugin-name>/` (must contain `.claude-plugin/plugin.json`)
2. Add an entry to the `plugins` array in `.claude-plugin/marketplace.json`
3. Commit + push

The team can then `/plugin install <plugin-name>@sociaaal-plugins`.

---

## Repository structure

```
sociaaal-plugins/
├── .claude-plugin/
│   └── marketplace.json          ← marketplace manifest (lists all plugins)
├── plugins/
│   └── winner-agent/             ← one plugin per subdirectory
│       ├── .claude-plugin/
│       │   └── plugin.json       ← plugin manifest
│       ├── skills/
│       │   └── winner-agent/
│       │       ├── SKILL.md
│       │       ├── known_paths.yaml
│       │       ├── scripts/
│       │       └── data/
│       └── README.md
└── README.md                     ← this file
```

---

## Versioning convention

Each plugin uses semver in its own `plugin.json`:

- **Patch (0.1.x):** prompt tweaks, single-app spec changes
- **Minor (0.x.0):** new tool added, new app added, new trend source
- **Major (x.0.0):** workflow restructure, breaking change

The marketplace itself is versioned in `marketplace.json` only when the marketplace structure changes (rare).

---

## Maintainer

Manas Gaikwad — Gen AI Creative Performance Director, Sociaaal LLC.
