# Cursor Grok Bot — Webflow

Use this when the agent is Cursor's Grok Bot. It has a built-in Webflow connection, so there is no MCP server to add and no config file to edit.

## Connect

Connect Webflow from Grok Bot's built-in connections, and log in to the right account, workspace and sites in the browser.

For another client, add another Webflow account the same way and keep the existing one connected. Each account keeps its own login, so several workspaces can sit side by side.

## Check it worked

Before working, tell the bot which Webflow account to use, and have it list that account's sites with a read-only call. Confirm they belong to the right workspace. With several accounts, check each one returns its own workspace.

## If it stops working

- **Wrong workspace:** confirm which account the bot used, then sign in to that account again and pick the right workspace.
- **Asks to log in again:** reconnect that account only, and leave the others connected.
