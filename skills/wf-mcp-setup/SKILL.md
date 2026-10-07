---
name: wf-mcp-setup
description: Connect a Webflow workspace to the current project via MCP. Use when starting a Webflow client project, troubleshooting Webflow MCP auth, or the user says "connect webflow", "add webflow", "webflow mcp", or needs Webflow MCP set up for a specific agent harness or cloud agent surface.
---

# Connect Webflow MCP

Add a project-scoped Webflow MCP server so this directory can read and write a specific Webflow workspace.

Official endpoint: `https://mcp.webflow.com/mcp` (or beta). OAuth tokens are keyed by **server name**, so different projects can use different workspaces without sharing one global Webflow login.

Do not assume which harness the user runs. Ask, or detect it from the session and the project's existing config files. A project can be used from more than one harness, and each one needs its own registration.

## Setup Flow

### Step 1: Pick a Server Name

Ask the user for a short identifier. Convention: `webflow-{project-or-site-slug}` (lowercase, hyphens).

Examples: `webflow-marketing-site`, `webflow-product-docs`, `webflow-redesign-2026`

### Step 2: Choose Production or Beta

Ask **production** (default) or **beta**.

- Production: `https://mcp.webflow.com/mcp`
- Beta: `https://mcp.webflow.com/beta/mcp` and name the server `webflow-{name}-beta`

### Step 3: Identify the harnesses

List every harness or surface that needs Webflow for this project. For each one, find where it reads **project-scoped** MCP config: check its docs or CLI help rather than assuming. If a harness has a file below, follow it instead of the generic steps; these surfaces are easy to get wrong:

- Codex (desktop app, CLI, IDE extension): [references/codex.md](references/codex.md)
- Cursor desktop IDE: [references/cursor-local.md](references/cursor-local.md)
- Cursor Cloud Agents: [references/cursor-cloud.md](references/cursor-cloud.md)

Local and cloud surfaces of the same product are often separate. Configuring one does not configure the other.

### Step 4: Write the server entry

Write the same entry everywhere it is needed. Merge into existing files; do not wipe other MCP servers.

`.mcp.json` at the project root is the most widely shared format. Write it whenever any harness in use reads it:

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

For a harness that uses its own file or format, translate the same name, transport (Streamable HTTP), and URL into that file. If the harness has a CLI command that adds a project-scoped HTTP server, prefer it, then confirm the file it wrote.

Transport must be Streamable HTTP. Do not use SSE. Use a local proxy such as `mcp-remote` only where a harness file calls for it.

### Step 5: Authenticate

Start a fresh session in this project directory so the harness loads the new config, then connect `webflow-{name}` through the harness's MCP connection flow. The user selects the correct Webflow workspace in the browser.

Desktop OAuth does not authorize cloud agent surfaces. Authenticate each surface on its own.

### Step 6: Verify

Discover Webflow MCP tools in-session. Do not freeze tool names.

Call the Webflow guide/index tool once if the server exposes one. Prefer listing sites to confirm the intended workspace.

## Troubleshooting

**Needs authentication after restart**

- Fresh session in this project directory, not a resumed one.
- Confirm the harness is reading the file you wrote.
- Re-auth. Tokens are keyed by server name. If OAuth never starts, remove the server entry, re-add it, and retry.

**Wrong workspace**

- Remove the server entry, re-add, re-auth. One OAuth flow locks to one workspace.

**Works in one harness but not another**

- Expected until each one is configured. Harnesses and surfaces do not share MCP registration. Copy the entry into the file the missing one reads.

**Already have a managed or account-level Webflow connector**

- Independent of project-scoped servers. Both can be active. Use the project-scoped server for client work so the workspace stays pinned to the project.

## Notes

- One workspace per server entry. Multiple workspaces = multiple entries.
- Do not add a single global Webflow MCP server for all client work.
