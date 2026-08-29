---
name: wf-mcp-setup
description: Connect a project to a Webflow workspace over MCP so each repo can keep its own authorization. Use when starting a Webflow client project, troubleshooting Webflow MCP auth, or the user says "connect webflow", "add webflow", or "webflow mcp". Works in Claude Code and Cursor. Does not cover Codex.
---

# Webflow MCP setup

**Version 0.1.0**

Give this project its own Webflow MCP connection so you can move between client workspaces without re-authorizing every time. Claude Code and Cursor. This process does not work for Codex due to the shared nature of Codex MCP servers.

Official install if you need the current UI: [Cursor](https://developers.webflow.com/mcp/installing/cursor), [Claude Code](https://developers.webflow.com/mcp/installing/claude-code).

## How it works

Endpoint: `https://mcp.webflow.com/mcp` (HTTP). Not `/sse`.

One server entry per project. OAuth runs once per entry and stays attached to that workspace. A second client project gets a second entry, so authorization is preserved per repo.

The Cursor marketplace Webflow plugin is global. For client work, use a **project** config.

## Setup

**1. Name** — `webflow-{client-or-project}` (lowercase, hyphens).

**2. Add**

Claude Code (`.mcp.json` in the project):

```bash
claude mcp add --transport http --scope project webflow-{name} https://mcp.webflow.com/mcp
```

Gitignore `.mcp.json` if the user does not want it in git.

Cursor (project `.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "webflow-{name}": {
      "url": "https://mcp.webflow.com/mcp"
    }
  }
}
```

Then Settings → MCP → Connect. Authorize the right workspace.

If the marketplace plugin already points at the correct workspace, use it. Don't add a duplicate for the same workspace.

**3. Check** — Claude Code: `claude mcp list`. Cursor: MCP indicator connected. List the tools this session actually exposes.

## If something's wrong

- Auth expired: new session in this directory, authorize this project server once. Needs a browser.
- OAuth succeeded but tools didn't load: URL should end in `/mcp`, not `/sse`.
- Wrong workspace: re-authorize this project entry. Don't silently use another project's server.
