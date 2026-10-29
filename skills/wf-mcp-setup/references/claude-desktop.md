# Claude Desktop — Webflow MCP

Use this when the agent runs in the Claude desktop app. The app has two surfaces that load MCP servers in different ways, so first find out which one the user works in.

## Chat vs Code

| | Code tab (Claude Code) | Chat |
|--|--|--|
| Project config | `.mcp.json` at the project root | None. Chats have no project directory |
| Remote servers | Project-scoped HTTP entry, one login per server name | Custom connectors at the account or org level, **one connector per URL per org** |
| Local servers | `.mcp.json`, plus everything in `claude_desktop_config.json` | `claude_desktop_config.json`, loaded in every chat |
| Per-client Webflow workspaces | Native, see [claude-code.md](claude-code.md) | Only through `mcp-remote` local servers (below) |

Docs: [custom connectors](https://claude.com/docs/connectors/custom/add-unlisted.md), [local MCP servers in Claude Desktop](https://modelcontextprotocol.io/docs/develop/connect-local-servers).

## Code tab

Follow [claude-code.md](claude-code.md). Servers you add to `claude_desktop_config.json` for Chat also load into every local Code tab session, and that file explains the overlap.

## Chat

### Why custom connectors do not work per client

Each connector holds one OAuth login, so it points at one Webflow workspace. When someone in the org has already added `https://mcp.webflow.com/mcp` (by hand or from the connector directory), adding it again fails with "A connector with this URL already exists in your organization." The org owner adds the connector once, and every member connects that same entry.

- **One Webflow workspace is enough:** connect the existing entry under Settings → Connectors. Do not add a custom connector.
- **More than one workspace:** use the local proxy path below. It works alongside the org connector.

### Proxy path

Each `mcp-remote` process keeps its OAuth tokens in its own `MCP_REMOTE_CONFIG_DIR`. Two servers can point at the same Webflow URL and still hold separate logins.

1. **Install `mcp-remote` once, outside every repository, at an exact version.** Check `npm view mcp-remote version`, review the release, and pin it. It needs Node 20 or newer.

   ```bash
   npm install --prefix "$HOME/.claude-desktop-mcp/runtime/mcp-remote" --save-exact mcp-remote@<version>
   ```

2. **Create an auth directory for this server only.** It must be outside the repository, and no other server may share it.

   ```bash
   mkdir -p "$HOME/.claude-desktop-mcp/webflow-auth/webflow-{name}"
   chmod 700 "$HOME/.claude-desktop-mcp/webflow-auth" "$HOME/.claude-desktop-mcp/webflow-auth/webflow-{name}"
   ```

3. **Merge the server into `claude_desktop_config.json`** (Settings → Developer → Edit Config). On macOS it is in `~/Library/Application Support/Claude/`, and on Windows in `%APPDATA%\Claude\`. Back it up first and keep the other keys in the file.

   The app is started from the GUI, so it does not inherit the shell `PATH` and version managers such as nvm are invisible to it. Use absolute paths, and resolve them first with `command -v node` and `echo $HOME`.

   ```json
   {
     "mcpServers": {
       "webflow-{name}": {
         "command": "/absolute/path/to/node",
         "args": [
           "/absolute/home/.claude-desktop-mcp/runtime/mcp-remote/node_modules/mcp-remote/dist/proxy.js",
           "https://mcp.webflow.com/mcp",
           "--transport", "http-only"
         ],
         "env": {
           "MCP_REMOTE_CONFIG_DIR": "/absolute/home/.claude-desktop-mcp/webflow-auth/webflow-{name}"
         }
       }
     }
   }
   ```

4. **Restart the app.** It reads `claude_desktop_config.json` only at launch, so it does not see a new or changed server until restart. Quit fully with ⌘Q on macOS, or with Quit in the tray menu on Windows. Closing the window leaves the app running. Then reopen it. Restart again after every change to the file. The proxy opens a browser login for each new server. The user picks the correct Webflow workspace. Complete one login before starting the next.

### Every chat sees every server

These servers are configured for the whole machine, not for a project, so every chat loads all of them. Name servers clearly. Tell the agent which server to use for the client, or turn off the others for that chat in its tools menu.

## Verify

- Settings → Developer shows `webflow-{name}` as running.
- In a new chat, list sites through `webflow-{name}`, and confirm the sites and their workspace ID belong to the intended workspace.
- With two or more servers, confirm that each one returns a different workspace ID. Different sites under the same workspace ID mean both logins picked the same workspace.
- Quit and reopen the app. The server must reconnect without opening a login again.

## Troubleshooting

- **"A connector with this URL already exists in your organization":** this is expected (see above). Connect the existing entry, or use the proxy path.
- **New server missing from the tools menu:** the app was not fully restarted. Quit it (do not just close the window) and reopen it.
- **Server fails at startup:** read `~/Library/Logs/Claude/mcp-server-webflow-{name}.log`. The usual cause is a relative path or a command that is only on the shell `PATH`.
- **Two servers return the same workspace:** they share an auth directory, or both logins chose the same workspace. Move only that server's auth directory aside, create a new one, and authorize again. Do not delete every MCP credential as a blanket repair.
- **Works in Code, not in Chat (or the reverse):** this is expected. The two surfaces do not share MCP registration.
