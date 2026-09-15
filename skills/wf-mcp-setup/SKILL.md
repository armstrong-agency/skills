---
name: wf-mcp-setup
description: Connect a Webflow workspace to the current project via MCP. Use when starting a Webflow client project, troubleshooting Webflow MCP auth, or the user says "connect webflow", "add webflow", or "webflow mcp".
---

# Connect Webflow MCP

Add a project-scoped Webflow MCP server so this directory can read and write a specific Webflow workspace.

Pi is the primary harness. Write the shared project file and the Cursor file. Do not stop after a Claude-only CLI add.

## How It Works

Each project gets its own Webflow MCP server entry pointing at `https://mcp.webflow.com/mcp` (or the beta URL). On first connection the harness opens a browser for OAuth; the user selects the target workspace. Tokens are stored per server name, so different projects can connect to different workspaces.

| File | Who reads it |
|------|----------------|
| `.mcp.json` | Pi (`pi-mcp-adapter`) and Claude Code project scope |
| `.cursor/mcp.json` | Cursor only. Keep it local. |

Pi does not load `.cursor/mcp.json` unless the user imports host configs. Cursor does not load `.mcp.json`. Write both.

## Setup Flow

### Step 1: Pick a Server Name

Ask the user for a short identifier. Convention: `webflow-{client-or-project-name}` (lowercase, hyphens).

Examples: `webflow-client-site`, `webflow-marketing-redesign`, `webflow-product-docs`

### Step 2: Choose Production or Beta

Ask the user if they want **production** (default) or **beta**.

- Production: `https://mcp.webflow.com/mcp`
- Beta: `https://mcp.webflow.com/beta/mcp` and name the server `webflow-{name}-beta`

### Step 3: Write Both Configs

Merge the server into existing files. Do not wipe other MCP servers.

**`.mcp.json`** (Pi + Claude):

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

**`.cursor/mcp.json`** (Cursor): same `mcpServers` entry.

If `.gitignore` exists, add `.cursor/mcp.json` when it is missing. Cursor MCP stays machine-local.

`.mcp.json` contains no secrets. It may be committed. Do not require gitignoring it.

Claude-only shortcut (writes `.mcp.json`, not Cursor):

```bash
claude mcp add --transport http --scope project webflow-{name} https://mcp.webflow.com/mcp
```

If you use that shortcut, still write `.cursor/mcp.json`.

### Step 4: Authenticate

The user selects the correct Webflow workspace in the browser.

**Pi**

- Restart the session in this project directory, or `/reload` after the file exists.
- Open `/mcp` and connect `webflow-{name}`, or `/mcp-auth webflow-{name}`.
- From an agent turn: `mcp({ action: "auth-start", server: "webflow-{name}" })`.

**Cursor**

- Reload the window or reopen the project.
- Approve the Webflow MCP server when Cursor prompts, or enable it under Cursor Settings → MCP.
- Complete OAuth in the browser.

**Claude Code**

- New session in this project directory (not resume).
- If OAuth does not start: `claude mcp remove webflow-{name}` then re-add.
- `claude mcp list` should show Connected.

### Step 5: Verify

Discover Webflow MCP tools in-session. Do not freeze tool names.

Call the Webflow guide/index tool once if the server exposes one.

## Troubleshooting

**Needs authentication after restart**

- Fresh session in this project directory.
- Confirm the harness is reading the file you wrote (Pi: `.mcp.json`; Cursor: `.cursor/mcp.json`).
- Re-auth. Tokens live in the OS credential store, keyed by server name.

**Wrong workspace**

- Remove the server entry, re-add, re-auth. One OAuth flow locks to one workspace.

**Pi cannot see a Cursor-only server**

- Copy the entry into `.mcp.json`. Do not rely on host-config import for normal setup.

**Already have Claude's managed Webflow plugin**

- Independent of project-scoped servers. Both can be active.

## Notes

- One workspace per server entry. Multiple workspaces = multiple entries.
- Do not add a global Webflow MCP server for client work.
- Codex is out of scope for this skill.
