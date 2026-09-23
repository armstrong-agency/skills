# Cursor local (IDE) — Webflow MCP

Use this when the agent runs **inside the Cursor desktop app** on a project folder.

## How local differs from Cloud

| | Cursor **local** (this file) | Cursor **Cloud Agents** |
|--|--|--|
| Where it runs | Your machine, current workspace | Isolated VM at [cursor.com/agents](https://cursor.com/agents) |
| Config source | `.cursor/mcp.json` (and Customize → MCP) | Cloud Agents MCP UI / Team MCP Servers — **not** project files |
| Project `.mcp.json` | Ignored by Cursor | Ignored by Cloud Agents |
| Auth storage | OS credential store, keyed by server name | Cursor Cloud account (OAuth proxied by Cursor) |
| Custom HTTP add | Write JSON + reload, or Customize → MCP | Agents `+` → MCP Servers → Add MCP |

Local IDE MCP does **not** automatically enable Cloud Agents. Set Cloud up separately ([cursor-cloud.md](cursor-cloud.md)).

## Prerequisites

- Server name already chosen (`webflow-{name}`).
- Production URL `https://mcp.webflow.com/mcp` (or beta — see parent skill).

## Steps

1. Merge into **`.cursor/mcp.json`** (create if missing). Do not wipe other servers:

```json
{
  "mcpServers": {
    "webflow-{name}": {
      "type": "http",
      "url": "https://mcp.webflow.com/mcp"
    }
  }
}
```

2. If `.gitignore` exists, ensure `.cursor/mcp.json` is listed. Keep this file machine-local; do not commit it.

3. Also write the same entry to **`.mcp.json`** when Pi or Claude Code share the repo (see parent skill). `.mcp.json` has no secrets and may be committed.

4. Reload the Cursor window or reopen the project.

5. Approve / enable the server when prompted, or under **Cursor Settings → MCP** / **Customize → MCP**.

6. Complete OAuth in the browser. Select the **correct Webflow workspace** for this project.

## Verify

- Tools from `webflow-{name}` appear in the local agent session.
- Discover Webflow tool names in-session. Call the Webflow guide/index tool once if exposed.
- Optional: list sites and confirm only the expected workspace appears.

## Troubleshooting

- **Needs auth after restart** — fresh session in this project directory; confirm Cursor is reading `.cursor/mcp.json`; re-auth.
- **Wrong workspace** — remove the server entry, re-add, re-auth. One OAuth flow locks to one workspace.
- **Cloud agent still missing Webflow** — expected. Local setup does not apply to Cloud; follow [cursor-cloud.md](cursor-cloud.md).
