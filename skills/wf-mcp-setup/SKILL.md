---
name: wf-mcp-setup
description: Connect a Webflow workspace to the current project via MCP. Use when starting a Webflow client project, troubleshooting Webflow MCP auth, or the user says "connect webflow", "add webflow", "webflow mcp", or needs Cursor Cloud vs local MCP setup.
---

# Connect Webflow MCP

Add a project-scoped Webflow MCP server so this directory can read and write a specific Webflow workspace.

Official endpoint: `https://mcp.webflow.com/mcp` (or beta). OAuth tokens are keyed by **server name**, so different projects can use different workspaces without sharing one global Webflow login.

Pi is the primary harness for repo files. Always write the shared project file when touching configs. For Cursor, follow the correct surface — **local IDE and Cloud Agents are separate**.

## Cursor local vs Cursor Cloud (read first)

| | **Cursor local** (desktop IDE) | **Cursor Cloud Agents** |
|--|--|--|
| Runs | On your machine | Isolated VM / [cursor.com/agents](https://cursor.com/agents) |
| MCP config | `.cursor/mcp.json` | Cloud Agents MCP UI (and optional Team MCP Servers) |
| Loads `.mcp.json`? | No | No |
| Loads `.cursor/mcp.json`? | Yes | No |
| Setup file | [references/cursor-local.md](references/cursor-local.md) | [references/cursor-cloud.md](references/cursor-cloud.md) |

Configuring one does **not** configure the other. If the user says “Cloud” / “cloud agent”, use the Cloud setup file only. If they are in the desktop app on a folder, use the local setup file.

**Never** tell a Cloud user that Dashboard → Plugins & MCPs → **Add** is how to add a custom HTTP MCP — that button opens the Marketplace.

## Setup Flow

### Step 1: Pick a Server Name

Ask the user for a short identifier. Convention: `webflow-{project-or-site-slug}` (lowercase, hyphens).

Examples: `webflow-marketing-site`, `webflow-product-docs`, `webflow-redesign-2026`

### Step 2: Choose Production or Beta

Ask **production** (default) or **beta**.

- Production: `https://mcp.webflow.com/mcp`
- Beta: `https://mcp.webflow.com/beta/mcp` and name the server `webflow-{name}-beta`

### Step 3: Choose harness / surface

Ask which surfaces need Webflow for this project (one or more):

| Surface | What to do |
|--|--|
| Pi / Claude Code | Write `.mcp.json` (below), then auth |
| Cursor **local** | Follow [references/cursor-local.md](references/cursor-local.md) |
| Cursor **Cloud Agents** | Follow [references/cursor-cloud.md](references/cursor-cloud.md) |

### Step 4: Write `.mcp.json` (Pi + Claude; document intended name)

Merge into existing files. Do not wipe other MCP servers.

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

`.mcp.json` contains no secrets. It may be committed. Do not require gitignoring it.

Claude-only shortcut (still write Cursor local/Cloud per their files if needed):

```bash
claude mcp add --transport http --scope project webflow-{name} https://mcp.webflow.com/mcp
```

### Step 5: Authenticate (per surface)

The user selects the correct Webflow workspace in the browser.

**Pi**

- Restart the session in this project directory, or `/reload` after the file exists.
- Open `/mcp` and connect `webflow-{name}`, or `/mcp-auth webflow-{name}`.
- From an agent turn: `mcp({ action: "auth-start", server: "webflow-{name}" })`.

**Claude Code**

- New session in this project directory (not resume).
- If OAuth does not start: `claude mcp remove webflow-{name}` then re-add.
- `claude mcp list` should show Connected.

**Cursor local** — [references/cursor-local.md](references/cursor-local.md)

**Cursor Cloud Agents** — [references/cursor-cloud.md](references/cursor-cloud.md)

### Step 6: Verify

Discover Webflow MCP tools in-session. Do not freeze tool names.

Call the Webflow guide/index tool once if the server exposes one. Prefer listing sites to confirm the intended workspace.

## Troubleshooting

**Needs authentication after restart**

- Fresh session in this project directory (local/Pi/Claude).
- Confirm the harness is reading the right config (Pi/Claude: `.mcp.json`; Cursor local: `.cursor/mcp.json`; Cloud: Agents MCP UI).
- Re-auth. Tokens are keyed by server name.

**Wrong workspace**

- Remove the server entry, re-add, re-auth. One OAuth flow locks to one workspace.

**Pi cannot see a Cursor-only server**

- Copy the entry into `.mcp.json`. Do not rely on host-config import for normal setup.

**Local Cursor works but Cloud does not (or the reverse)**

- Expected until both surfaces are configured. They do not share MCP registration. Use the matching setup file.

**Already have Claude's managed Webflow plugin**

- Independent of project-scoped servers. Both can be active.

**Leftover broker / non-Webflow HTTP MCP**

- Disable or remove it. Do not authenticate abandoned broker hosts. Project work uses `webflow-{name}` → `https://mcp.webflow.com/mcp` only.

## Notes

- One workspace per server entry. Multiple workspaces = multiple entries.
- Do not add a single global Webflow MCP server for all client work.
- Codex is out of scope for this skill.
- Do not put private site IDs, screenshots, or tokens in this public skills repo.
