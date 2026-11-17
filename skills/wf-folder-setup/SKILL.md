---
name: wf-folder-setup
description: Set up or audit a working folder for a Webflow site, with its AGENTS.md, MCP pin, publishing levels and custom code backup. Use when starting work on a Webflow site in a new folder, or bringing an existing folder up to standard.
---

# Webflow working folder

A **working folder** is the local folder for one Webflow site. The site is built and hosted in Webflow, so the working folder holds only what the site cannot: whose site it is, which MCP server reaches it, what agents may publish, a backup of custom code, and records of finished jobs. Nothing in it is deployed.

This skill writes local files only. It reads Webflow and leaves the site as it found it.

## Route

- **Fresh:** the folder is empty or holds only MCP config. Run the five stages below.
- **Existing:** the folder already holds instruction files or work. Follow [audit.md](references/audit.md).

## Stages

Run the stages in order. Open each with "Stage n of 5" and its name, and ask only that stage's questions. Read from Webflow whatever Webflow can tell you, and ask the user for the rest.

### 1. Site

Ask which Webflow site this working folder is for, and whose it is: the user's own, a direct client's, or a client's through a partner agency. Suggest the site's slug as the folder name and use the name the user chooses. One working folder serves one site.

Done when you can state the site, the relationship and the folder path.

### 2. Connect

The working folder needs a project-scoped server named `webflow-{name}` in `.mcp.json`. When it is missing or unauthenticated, run `wf-mcp-setup`, and when that needs a fresh session, tell the user to resume here at stage 2.

Through that server, using the tool names this session exposes, read:

- the site's display name, site ID, production domains and staging subdomain;
- the naming convention, identified the way `wf-build` identifies it;
- the names of any agent rules and skills stored on the site.

Done when the user confirms that the site ID and name you read back are the intended site.

### 3. Rules

Ask for the two publishing levels, showing the scale from [agents-template.md](references/agents-template.md). Both default to 2.

Then offer each optional section with one question, and leave out any the user skips:

- **Outside systems:** trackers, form destinations, tag managers, consent tools, analytics, font licences, domain registrars, and who owns each account.
- **House style:** only when the site follows an in-house convention. Ask for the patterns the Style Guide page does not show.
- **Known quirks:** anything about this site that has already cost time.

Done when both levels are set and each optional section has an answer or a skip.

### 4. Write

Draft `AGENTS.md` from [agents-template.md](references/agents-template.md). Show the user the draft and the list of files, and wait for a yes before writing anything.

Then write:

- `AGENTS.md`
- `CLAUDE.md`, holding the single line `@AGENTS.md`
- `.gitignore`:

  ```
  .DS_Store
  .env*
  .claude/settings.local.json
  .playwright-mcp/
  .firecrawl/
  ```

- `snippets/`, the first backup of the site's custom code.

`.mcp.json` holds no secrets and is committed.

For the backup, count the static pages first, tell the user how many reads the backup needs, and wait for a yes. Then save each non-empty block as one file, named and headed as the template's Folder layout section describes:

- the site's head and footer code;
- every registered script, with its name, version and where it is applied; for a hosted script, record its URL in place of the source;
- the head and footer code of every static page that has any.

Code Embed elements stay out of the first backup. A job backs one up when it first touches it.

Done when every non-empty block has a file with a header, and you have told the user how many files were written and which blocks were empty.

### 5. Git

Run `git init` and make the first commit. Offer a private remote, and create it only on a yes, on the host and under the owner the user names.

Close with a summary: the files written, the two publishing levels, the sections skipped, and every fact you could not verify against Webflow.
