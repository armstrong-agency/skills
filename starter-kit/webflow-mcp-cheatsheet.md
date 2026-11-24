# Webflow MCP setup cheatsheet

The Webflow MCP is the connection that lets an AI tool read and change your Webflow site. This page sets it up the safe way: one named connection per site, tied to that site's folder, so an agent cannot wander into a different site.

Hand this page to whoever owns your Webflow site. It takes about 10 minutes.

## The idea

- Make one folder on your computer per Webflow site.
- Give that folder its own connection, named `webflow-{site}` (for example `webflow-acme-marketing`).
- Each named connection has its own Webflow login, and you choose which sites it can reach when you sign in.

The address is the same for every tool: `https://mcp.webflow.com/mcp`

## Claude Code

Run this from the site's folder:

```bash
claude mcp add --transport http webflow-{site} --scope project https://mcp.webflow.com/mcp
```

That writes a `.mcp.json` file in the folder:

```json
{
  "mcpServers": {
    "webflow-{site}": {
      "type": "http",
      "url": "https://mcp.webflow.com/mcp"
    }
  }
}
```

Then:

1. Quit Claude Code and start it again in the folder. It only reads this file at startup.
2. Approve the `webflow-{site}` server when asked.
3. Run `/mcp`, choose `webflow-{site}`, and sign in. Pick the right workspace and sites in the browser.

## Codex

Codex does not read `.mcp.json`. Add this to `.codex/config.toml` in the site's folder:

```toml
[mcp_servers.webflow-{site}]
url = "https://mcp.webflow.com/mcp"
default_tools_approval_mode = "writes"
```

Then, from the folder:

```bash
codex mcp login webflow-{site}
```

Pick the right workspace and sites in the browser, and start a new chat in the project. Codex only loads project config in a folder you have marked as trusted.

## Cursor

Cursor reads `.cursor/mcp.json` in the site's folder:

```json
{
  "mcpServers": {
    "webflow-{site}": {
      "type": "http",
      "url": "https://mcp.webflow.com/mcp"
    }
  }
}
```

Then:

1. Reload the Cursor window.
2. Turn the server on under Cursor Settings, MCP.
3. Sign in, and pick the right workspace and sites in the browser.

Cursor's cloud agents do not read this file. They are set up separately in Cursor's web dashboard.

## Grok Bot

Grok Bot, the tool I use in the course, has a built-in Webflow connection, so there is no file to edit. Connect Webflow from its connections menu and sign in to the right workspace. To work on a second site in another workspace, add another Webflow account the same way and keep the first one connected.

## Check it worked

A successful login does not prove you are on the right site. Before any real work, ask the AI:

> List the Webflow sites you can reach, with their site IDs. Do not change anything.

Compare the answer to the site ID in your `AGENTS.md`. You can find a site's ID in Webflow under Site settings, General.

## When something goes wrong

| What you see | What to do |
|---|---|
| The tool asks you to sign in again after a restart | Start a fresh session in the site's folder instead of resuming an old one, then sign in to that one connection. |
| The AI lists the wrong sites | Sign out of that one named connection, sign in again, and pick the right workspace. Leave your other connections alone. |
| It works in one tool and not another | Each tool keeps its own setup. Add the same entry to the file the other tool reads. |
| The AI can see every site your company has | You are on a shared, account-wide connection. Switch to the named one for this folder. |

## One rule

Do not set up a single Webflow connection for all of your sites. One connection per site is what stops an agent from publishing a change to the wrong one.

The full version of these steps, covering more tools, is the [`wf-mcp-setup`](../skills/wf-mcp-setup/SKILL.md) skill in this repository: `npx skills add armstrong-agency/skills`, then ask your agent to run `wf-mcp-setup`.
