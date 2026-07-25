---
name: webflow-mcp-setup
description: Connect Webflow MCP to the current project or folder in Codex. Use whenever the user says "connect to Webflow", "connect Webflow", "add Webflow", "set up Webflow MCP", starts a Webflow client project, or needs project-specific Webflow authentication. Default an unqualified request to a project-scoped standard Webflow connection, never a global MCP entry.
---

# Connect Webflow MCP in Codex

Create a Webflow MCP connection that is available only while Codex is working
in the current project. Treat connection setup as authorization to configure
and authenticate MCP only, not authorization to change Webflow content or
deploy a site.

## Connection model

- Interpret "connect to Webflow" as project-scoped to the current directory.
- Use the canonical production endpoint `https://mcp.webflow.com/mcp`. Do not
  add project names or other query parameters.
- For beta, use `https://mcp.webflow.com/beta/mcp` and suffix the server name
  with `-beta`.
- Derive a unique lowercase server name from the project directory:
  `webflow-{project-name}`.
- Isolate workspaces by server name. Several project-scoped servers may use the
  same canonical URL while targeting different Webflow workspaces.
- Give multiple connections stable, site-specific server names and document
  the server-to-site mapping in project instructions.
- Configure project scope in `.codex/config.toml`. Do not use `codex mcp add`
  because it writes user-level config and has no project-scope flag.
- Keep OAuth credentials out of project files. Do not add
  `.codex/config.toml` to `.gitignore` by default; it contains configuration,
  not tokens.
- Never create a global Webflow MCP entry unless the user explicitly requests
  one.
- Treat the managed `mcp__codex_apps__webflow` plugin as independent and
  global. It may coexist, but never substitute it for a requested
  project-scoped server.

## Setup

1. Resolve the intended project root. Default to the current working directory;
   use a discovered repository root when the current directory is inside a
   repository.
2. Inspect `.codex/config.toml` if it exists. Preserve every unrelated setting
   and MCP server.
3. Normalize the project basename to lowercase hyphen-case and name the server
   `webflow-{name}`. For multiple sites, use stable names that identify each
   site or role. Reuse matching entries rather than duplicating them.
4. If an existing Webflow URL contains `?project=`, migrate it back to the
   canonical URL while preserving the unique server name.
5. Create or merge this configuration:

   ```toml
   [mcp_servers.webflow-project-name]
   url = "https://mcp.webflow.com/mcp"
   auth = "oauth"
   default_tools_approval_mode = "writes"
   ```

6. Run `codex mcp login webflow-project-name` from the project root. Let the
   user complete Webflow OAuth and select the correct workspace.
7. Verify from the same directory with `codex mcp get webflow-project-name` and
   `codex mcp list`.
8. After adding, migrating, or authenticating the server, require a completely
   new Codex task in the project directory. Continuing or resuming the current
   task does not reload a failed MCP client.
9. In that new task, confirm the scoped server is available and verify the
   exact Webflow site identity before deep inspection or writes.
10. For multiple connections, record each server's intended site ID and role
    in the project's `AGENTS.md`. Require the agent to name and verify the
    target server before every operation; default migration-source sites to
    read-only.

## Safety and scope

- Do not call Webflow tools merely to test the connection unless the user
  explicitly authorizes Webflow access beyond setup. CLI configuration and
  OAuth status are sufficient verification.
- Do not make Webflow changes unless the user explicitly asks for those
  changes.
- Do not deploy or publish to Webflow production unless the user explicitly
  asks for that deployment.
- Prefer `default_tools_approval_mode = "writes"` so read-only tools can run
  normally and tools classified as writes require approval.
- Fail closed if the project-scoped server is unavailable. Report the
  unavailable server name and stop; do not call the global Webflow plugin or
  another project's server.

## Troubleshooting

- If project config is ignored, verify that Codex trusts the project; untrusted
  projects do not load `.codex/config.toml`.
- If OAuth is stale or targets the wrong workspace, run
  `codex mcp logout webflow-project-name`, then
  `codex mcp login webflow-project-name` and select the correct workspace.
- If tools do not appear after successful login, start a new task rather than
  resuming the current one.
- If a server reports `invalid_grant`, refresh only that uniquely named server
  with logout/login. Keep the canonical URL unchanged.
- If only `mcp__codex_apps__webflow` tools appear, the scoped server did not
  initialize. Do not interpret the global plugin's workspace as the project
  connection.
