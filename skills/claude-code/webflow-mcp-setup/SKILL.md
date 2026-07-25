---
name: webflow-mcp-setup
description: Connect a Webflow workspace to the current project via MCP. Use when starting a Webflow client project, troubleshooting Webflow MCP auth, or the user says "connect webflow", "add webflow", or "webflow mcp".
---

# Connect Webflow MCP

Add a project-scoped Webflow MCP server so Claude can read and write to a specific Webflow workspace from this project directory.

## How It Works

Each project gets its own Webflow MCP server entry pointing at `https://mcp.webflow.com/mcp`. On first connection, Claude Code opens a browser for OAuth — user selects the target workspace. The token is stored per server name, so different projects can connect to different workspaces.

## Setup Flow

### Step 1: Pick a Server Name

Ask the user for a short identifier. Convention: `webflow-{client-or-project-name}` (lowercase, hyphens).

Examples: `webflow-client-site`, `webflow-marketing-redesign`, `webflow-product-docs`

### Step 2: Add the Server

Ask the user if they want to connect to the **production** or **beta** MCP server.

**Production** (default):
```bash
claude mcp add --transport http --scope project webflow-{name} https://mcp.webflow.com/mcp
```

**Beta** (opt-in — newer features, may be less stable):
```bash
claude mcp add --transport http --scope project webflow-{name}-beta https://mcp.webflow.com/beta/mcp
```

This writes to `.mcp.json` in the project root. Remind the user to add `.mcp.json` to `.gitignore`.

### Step 3: Trigger OAuth

Claude Code should open a browser popup for OAuth automatically — either immediately or on the next session start. The user selects the correct Webflow workspace and authorizes.

If it doesn't trigger automatically:
1. Try starting a **new session** (not resume) in this project directory
2. If still stuck, remove and re-add: `claude mcp remove webflow-{name}` then re-add
3. Check `claude mcp list` — should show "Connected" after successful auth

### Step 4: Verify

```bash
claude mcp list
```

Look for the server showing as connected. Tools appear as `mcp__webflow-{name}__*`.

Call `webflow_guide_tool` once to load the Webflow MCP capabilities index.

## Troubleshooting

**"Needs authentication" after session restart:**
- Try a completely fresh session (`claude` not `claude -c`)
- Remove and re-add the server entry
- Make sure a browser is available (won't work over SSH / headless)

**Wrong workspace selected:**
- `claude mcp remove webflow-{name}` → re-add → re-auth with correct workspace
- Each OAuth flow locks to one workspace; no way to switch without re-adding

**Already have the managed `claude.ai Webflow` plugin:**
- The managed connection and project-scoped servers are independent
- Both can be active simultaneously (different workspaces)
- The managed one is always global; project-scoped ones stay local to the directory

## Notes

- **One workspace per server entry.** Multiple workspaces = multiple server entries.
- **`--scope project`** keeps the config in `.mcp.json` in the project root, not global config.
- **Token persists in macOS Keychain** per server name — survives session restarts.
