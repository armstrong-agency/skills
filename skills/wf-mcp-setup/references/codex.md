# Codex — Webflow MCP

Use this when the agent runs in Codex: the ChatGPT desktop app, the Codex CLI, or the Codex IDE extension. On one machine they share `~/.codex/config.toml`, but the desktop app can bundle a different Codex version from the one on the shell's `PATH`.

## How Codex differs from the generic steps

| | Codex |
|--|--|
| Project config | `.codex/config.toml` (TOML), loaded only in **trusted** projects |
| Reads `.mcp.json`? | No |
| CLI `codex mcp add` | Writes the user-level `~/.codex/config.toml`, not the project |
| Login | `codex mcp login <name>`, once per connection |

Docs: [Codex MCP](https://developers.openai.com/codex/mcp).

## Connect

### Easiest: the Webflow plugin

Open the Webflow plugin's settings in Codex and choose **Connected accounts → Connect another account**. Log in to the right account, workspace and sites in the browser, and keep the existing account connected. Add one account per client workspace the same way.

Before working, pick the intended account and list its sites to confirm the workspace. If the agent can't reach the plugin settings, ask the user to add the account there, rather than disconnecting one that works.

### Pinned to a project

To tie a connection to one project folder, give it its own name and merge it into the project's `.codex/config.toml`:

```toml
[mcp_servers.webflow-{name}]
url = "https://mcp.webflow.com/mcp"
default_tools_approval_mode = "writes"
```

Then run `codex mcp login webflow-{name}` from the project directory, and the user picks the right workspace and sites in the browser. Log in to one connection at a time.

You can have several connections on one machine, each on a different workspace. Two projects that use the same name share one login, so use the same name only when you want that. These connections are separate from the plugin's accounts.

## Check it worked

1. Confirm Codex can see the connection: the plugin lists the account under **Connected accounts**, or for a project connection, `codex mcp list` from the project directory shows `webflow-{name}`. Either way, the chat you're working in must be able to call it.
2. Call the connection's guide tool once, then list sites with a read-only call. Confirm they belong to the right workspace. A successful login isn't enough on its own.
3. With several connections, list sites through each one and confirm each returns its own workspace.

Webflow's MCP may group a read-only site list with publish actions in one tool, so `default_tools_approval_mode = "writes"` can prompt for approval on a read. Approve that one call manually rather than loosening the approval mode.

## If it stops working

Copy the exact error first.

- **Connection missing:** the project isn't trusted, the entry is in `.mcp.json` instead of `.codex/config.toml`, the entry is disabled, or the chat started before the entry was added. Start a new chat in the project.
- **Asks to log in again:** run `codex mcp login` for that connection only.
- **Wrong workspace:** confirm which connection name the chat called, then log in to that connection again and pick the right workspace.
- **Two entries for one workspace:** ask the user which one to keep before disabling the other.

Leave working connections alone: never remove every connection or clear every login as a blanket repair.

_Tested November 9, 2026 with Codex 0.166 and 0.167: two named connections stayed on separate workspaces from project config alone, after their access tokens expired and renewed, and after a full quit and relaunch. The same name in two projects shared one login. The plugin's **Connect another account** option was confirmed in the UI, but working through two plugin accounts at once was not tested. Before these versions, adding a second named connection could log out the first. If that still happens, update Codex and check again, and if it persists, use the proxy path below._

## Proxy path

Use this only when adding a second connection still logs out the first after updating Codex. A local [`mcp-remote`](https://github.com/geelen/mcp-remote) process per connection keeps that connection's login in its own directory, and Codex talks to it locally.

1. **Install `mcp-remote` once, outside every repository, at an exact version.** Check `npm view mcp-remote version`, review the release, and pin it. Check the pinned release's Node requirement.

   ```bash
   npm install --prefix "$HOME/.codex/runtime/mcp-remote" --save-exact mcp-remote@<version>
   ```

2. **Create a login directory for this connection only,** outside the repository and shared with no other connection.

   ```bash
   mkdir -p "$HOME/.codex/webflow-mcp-auth/webflow-{name}"
   chmod 700 "$HOME/.codex/webflow-mcp-auth" "$HOME/.codex/webflow-mcp-auth/webflow-{name}"
   ```

3. **Replace the connection's entry in `.codex/config.toml`.** Use absolute paths; resolve them first with `command -v node` and `echo $HOME`.

   ```toml
   [mcp_servers.webflow-{name}]
   command = "/absolute/path/to/node"
   args = ["/absolute/home/.codex/runtime/mcp-remote/node_modules/mcp-remote/dist/proxy.js", "https://mcp.webflow.com/mcp", "--transport", "http-only"]
   env = { MCP_REMOTE_CONFIG_DIR = "/absolute/home/.codex/webflow-mcp-auth/webflow-{name}" }
   startup_timeout_sec = 120
   default_tools_approval_mode = "writes"
   ```

   These paths are machine-specific. If the project is shared, decide with the user whether `.codex/config.toml` is committed or gitignored.

4. **Log in once through the proxy's client,** and the user picks the right workspace and sites. Stop the client after it lists Webflow tools, and never print the login files.

   ```bash
   MCP_REMOTE_CONFIG_DIR="/absolute/home/.codex/webflow-mcp-auth/webflow-{name}" \
     /absolute/path/to/node /absolute/home/.codex/runtime/mcp-remote/node_modules/mcp-remote/dist/client.js \
     https://mcp.webflow.com/mcp --transport http-only
   ```

5. **Restart Codex,** start a new chat in the project, and run the checks above.

If a proxy connection asks to log in again, confirm its `MCP_REMOTE_CONFIG_DIR` is absolute, unique to that connection, and still holds files.
