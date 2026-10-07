# Codex — Webflow MCP

Use this when the agent runs in Codex: the ChatGPT desktop app, the Codex CLI, or the Codex IDE extension. All three share the same configuration.

## How Codex differs

| | Codex | Most other harnesses |
|--|--|--|
| Project config | `.codex/config.toml` (TOML), loaded only in **trusted** projects | `.mcp.json` (JSON) |
| Reads `.mcp.json`? | No | Usually |
| CLI `codex mcp add` | Writes the user-level `~/.codex/config.toml`, not the project | Often supports a project scope |
| Remote OAuth | Native, but a new Webflow connection overwrites the previous one, and token refresh is unreliable (below) | Native, one login per server name |

Docs: [Codex MCP](https://developers.openai.com/codex/mcp).

## Choose native OAuth or the proxy

Codex's native MCP OAuth has two problems for Webflow work:

- **Only one Webflow connection survives.** Authorizing a new Webflow server overwrites the previous connection, even under a different server name. Every project ends up on whichever workspace was authorized last. That makes native OAuth impractical for agencies and freelancers with more than one client.
- **Token refresh is unreliable.** Codex can fail to refresh an expired access token even though a refresh token is stored. A connection works for about an hour, then later tasks fail with `invalid_grant` and ask for another browser login. Track it at [openai/codex#17265](https://github.com/openai/codex/issues/17265).

Choose the path:

- **More than one Webflow workspace on this machine, or #17265 still open:** use the proxy path. A local [`mcp-remote`](https://github.com/geelen/mcp-remote) process per server owns that server's OAuth tokens in its own directory and refreshes them, and Codex talks to it over STDIO.
- **A single workspace and #17265 fixed:** the native path is enough. Confirm it survives a natural token expiry (at least an hour) without a new login before calling the setup done.

## Native path

Single Webflow workspace only. A second native Webflow connection replaces this one.

Merge into the project's `.codex/config.toml`. Do not wipe other servers.

```toml
[mcp_servers.webflow-{name}]
url = "https://mcp.webflow.com/mcp"
default_tools_approval_mode = "writes"
```

Then run `codex mcp login webflow-{name}` from the project directory and pick the correct Webflow workspace in the browser.

## Proxy path

The proxy keeps each project's tokens in its own directory, so different projects can stay on different Webflow workspaces.

1. **Install `mcp-remote` once, outside every repository, at an exact version.** Check `npm view mcp-remote version`, review the release, and pin it. Do not run `npx mcp-remote@latest` at startup; an unattended upgrade can change auth behavior. It needs Node 20 or newer.

   ```bash
   npm install --prefix "$HOME/.codex/runtime/mcp-remote" --save-exact mcp-remote@<version>
   ```

2. **Create an auth directory for this server only.** It must be outside the repository, and no other server may share it.

   ```bash
   mkdir -p "$HOME/.codex/webflow-mcp-auth/webflow-{name}"
   chmod 700 "$HOME/.codex/webflow-mcp-auth" "$HOME/.codex/webflow-mcp-auth/webflow-{name}"
   ```

3. **Merge the server into `.codex/config.toml`.** Use absolute paths rather than relying on `~` or `$HOME` expansion; resolve them first with `command -v node` and `echo $HOME`.

   ```toml
   [mcp_servers.webflow-{name}]
   command = "/absolute/path/to/node"
   args = ["/absolute/home/.codex/runtime/mcp-remote/node_modules/mcp-remote/dist/proxy.js", "https://mcp.webflow.com/mcp", "--transport", "http-only"]
   env = { MCP_REMOTE_CONFIG_DIR = "/absolute/home/.codex/webflow-mcp-auth/webflow-{name}" }
   startup_timeout_sec = 120
   default_tools_approval_mode = "writes"
   ```

   These paths are machine-specific. If the project is shared, decide with the user whether `.codex/config.toml` is committed or gitignored.

4. **Authorize once through the proxy's client.** The user picks the correct Webflow workspace in the browser. Do not start a second OAuth flow while one is open.

   ```bash
   MCP_REMOTE_CONFIG_DIR="/absolute/home/.codex/webflow-mcp-auth/webflow-{name}" \
     /absolute/path/to/node /absolute/home/.codex/runtime/mcp-remote/node_modules/mcp-remote/dist/client.js \
     https://mcp.webflow.com/mcp --transport http-only
   ```

   Stop the client after it lists Webflow tools. Never print the token files.

5. **Optionally add `required = true`** once auth works, so Codex fails at startup instead of running a Webflow task without Webflow.

6. **Restart Codex once** so it loads the new server, then start a new task in the project.

## Verify

- `codex mcp list` shows `webflow-{name}`.
- In a new task, list sites with a read-only tool and confirm they belong to the intended workspace.
- Start a second new task. It must connect without opening OAuth again.
- Webflow's MCP may group a read-only site list with publish actions in one tool, so `default_tools_approval_mode = "writes"` can prompt for approval on a read. Approve that one call manually; do not loosen the approval mode to avoid it.

## Troubleshooting

- **Asks for login on every task (native path):** this is the refresh defect. Move to the proxy path.
- **Another project switched workspaces (native path):** a newer native Webflow login overwrote this one. Move every Webflow server to the proxy path.
- **Asks for login (proxy path):** confirm the `MCP_REMOTE_CONFIG_DIR` path is absolute, unique to this server, and still contains credential files. If config changed mid-task, start a new task before re-authorizing. Re-authorize only after a concrete failure.
- **Server missing in Codex:** the project is not trusted, or the entry is in `.mcp.json` instead of `.codex/config.toml`.
- **Wrong workspace:** move only this server's auth directory aside, create a fresh one, and authorize again. Never delete every MCP credential as a blanket repair.
- **Leftover native entry:** if a `url =` entry and a proxy entry exist for the same project, keep one. Two servers for one workspace confuse the agent about which to use.
