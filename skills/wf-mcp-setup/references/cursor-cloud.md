# Cursor Cloud Agents — Webflow MCP

Use this when the agent runs as a **Cursor Cloud Agent** (browser / `cursor.com/agents` VM), not the desktop IDE.

## How Cloud differs from local

| | Cursor **Cloud Agents** (this file) | Cursor **local** (IDE) |
|--|--|--|
| Where it runs | Isolated VM at [cursor.com/agents](https://cursor.com/agents) | Your machine |
| Config source | Cloud Agents MCP UI and/or Team MCP Servers | `.cursor/mcp.json` |
| Project `.mcp.json` / `.cursor/mcp.json` | **Not loaded** into the Cloud VM for MCP | Local Cursor uses `.cursor/mcp.json` |
| Tool calls | Proxied by Cursor backend (HTTP recommended) | App talks to the MCP server directly |
| Custom HTTP add | Agents home `+` → MCP Servers → Add MCP | Write JSON + reload |

Committing `.mcp.json` helps Pi / Claude Code and documents the intended server name. It does **not** turn on Cloud MCP by itself.

## Prerequisites

- Same server name as the project (`webflow-{name}`) so docs and harnesses match.
- Production URL `https://mcp.webflow.com/mcp` (Streamable HTTP). SSE and `mcp-remote` are not supported on Cloud Agents.

## Personal Cloud setup (usual path)

1. Open [cursor.com/agents](https://cursor.com/agents) — the Agents **chat** home, not Team Dashboard → Integrations.
2. Click **`+`** left of the prompt (“Add files, skills, and MCP servers”).
3. Hover **MCP Servers** → **Add MCP**.
4. Add a custom **HTTP** server:
   - **Name:** `webflow-{name}` (must match the project-scoped name)
   - **URL:** `https://mcp.webflow.com/mcp`
5. Complete OAuth. Select the **correct Webflow workspace** for this project.
6. Enable the server for the agent run.
7. Start a **new** Cloud Agent (or re-enable MCP on the run) after first auth.

### Wrong UI paths (do not use for custom HTTP)

| UI | What it actually does |
|--|--|
| Dashboard → **Integrations** | GitHub / Slack / Linear / etc. — not MCP |
| Dashboard → **Plugins & MCPs** → **Add** | Opens the **Marketplace** (plugins) — not a custom URL form |
| IDE **Customize → MCP** | Local only — does not sync to Cloud Agents |

## Team-shared Cloud setup (admin)

1. Open Dashboard → **Plugins & MCPs**.
2. Find **Team MCP Servers** (separate from marketplace **Add**).
3. Add the same HTTP server: name `webflow-{name}`, URL `https://mcp.webflow.com/mcp`.
4. Teammates complete their own OAuth (per-user, even for shared servers).
5. Optional: **Add to Team Marketplace** so IDE / CLI can install the same server later. That step is not required for Cloud Agents once the Team MCP server exists.

## Verify

- Ask a Cloud Agent whether namespace `webflow-{name}` is available with real Webflow tools (not auth-only).
- Call the Webflow guide/index tool once if exposed, then list sites.
- Confirm sites belong to the intended workspace only.

## Troubleshooting

- **Only marketplace after Add** — you used Plugins & MCPs → Add. Use Agents `+` → MCP Servers → Add MCP instead.
- **Tools missing on a Cloud run** — personal/team Cloud MCP not enabled for that account; project JSON files are ignored.
- **Wrong workspace** — remove/disable the Cloud MCP entry, re-add, re-auth.
- **Dead broker / leftover HTTP MCP** — disable or remove it. Do not authenticate abandoned broker hosts. Use only `webflow-{name}` → `https://mcp.webflow.com/mcp`.
- **Local works, Cloud does not** — expected until this Cloud setup is done. Follow this file, not [cursor-local.md](cursor-local.md).
