# Claude Code — Webflow MCP

Use this when the agent runs in Claude Code: the `claude` CLI in a terminal, or the **Code** tab of the Claude desktop app. For the desktop app's Chat surface, use [claude-desktop.md](claude-desktop.md).

## CLI vs desktop Code tab

Both run the same Claude Code and read the same `.mcp.json` and `~/.claude.json`. They differ in what else they load.

| | CLI | Desktop Code tab (local session) |
|--|--|--|
| Project `.mcp.json` | Yes | Yes |
| `~/.claude.json` (local and user scope) | Yes | Yes. A user-scope stdio server beats a `.mcp.json` server of the same name, unlike the CLI |
| `claude_desktop_config.json` | No | Yes. It beats `.mcp.json` and `~/.claude.json` when a name appears in both |
| claude.ai connectors | Yes, lowest precedence, matched by URL | Yes, delivered by the app |
| Edit `.mcp.json` by hand | Any editor | Not in the app's file pane; use another editor |

Docs: [Claude Code MCP](https://code.claude.com/docs/en/mcp), [desktop shared configuration](https://code.claude.com/docs/en/desktop#shared-configuration).

## Set up

1. Add the project-scoped server from the project root. This writes `.mcp.json`. Then confirm that the file contains the entry from [SKILL.md](../SKILL.md).

   ```bash
   claude mcp add --transport http webflow-{name} --scope project https://mcp.webflow.com/mcp
   ```

2. **Restart Claude Code.** It reads MCP config only at startup, so a running session does not see the new server. Exit with `/exit` and run `claude` again in the project directory. Do not use `--resume` or `--continue`. The CLI asks you to approve project servers from `.mcp.json` before it uses them. Approve `webflow-{name}`.

3. Run `/mcp`, select `webflow-{name}`, and sign in. The user picks the correct Webflow workspace in the browser. From a shell, `claude mcp login webflow-{name}` runs the same flow.

Each server name gets its own sign-in, so `webflow-client-a` and `webflow-client-b` can point at the same URL and stay on different workspaces.

## Desktop Code tab

Steps 1 to 3 are the same, but restart differently:

- **After a change to `.mcp.json`:** start a new local session in the project folder. Do not resume an existing session.
- **After a change to `claude_desktop_config.json`:** quit the app fully (⌘Q on macOS; closing the window is not enough) and reopen it. The app reads that file only at launch.

Also check the following:

- **Desktop chat servers leak into every session.** Every server in `claude_desktop_config.json` (for example, per-client proxies set up for Chat) loads into every local Code tab session, whichever project is open. The agent then sees Webflow servers for other clients. Tell it which server belongs to this project, or turn off the others for the session.
- **Name collisions.** If `claude_desktop_config.json` defines `webflow-{name}` too, the Code tab uses that definition and its sign-in, not the project's `.mcp.json`. Give Chat proxies names that do not match project servers, or use one definition on purpose.
- **Org connector next to a project server.** The org's Webflow connector can be active alongside `webflow-{name}`. Use the project server for client work.

## Cloud sessions

Claude Code on the web and cloud sessions started from the app load `.mcp.json` from the repository without the approval prompt. Sign-in happens there, separately from local sign-ins. Connectors come from claude.ai organization settings. See [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web).

## Troubleshooting

- **Server shows `Pending approval`:** the folder is not trusted, or the approval prompt was declined. Run `claude mcp reset-project-choices` and start a new session.
- **Wrong workspace:** `/mcp` → `webflow-{name}` → Clear authentication, then sign in again. Do not remove other servers' sign-ins.
- **Code tab connects to a different workspace than the CLI:** a same-named server in `claude_desktop_config.json` or at user scope in `~/.claude.json` is overriding `.mcp.json`. Rename or remove the duplicate.
- **`claude mcp list` warns about the same name in more than one scope:** keep one definition and remove the others with `claude mcp remove webflow-{name} --scope <scope>`.
