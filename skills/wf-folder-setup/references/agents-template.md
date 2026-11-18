# AGENTS.md template

Fill the template from what Webflow returned and what the user said. Write only what you know: a line or optional section with no content is left out, and the finished file holds no braces.

Every line must pass one test: the Webflow site cannot hold it. Pages, classes, variables, components and CMS structure are read live from the site, so they stay out of this file.

## Publishing scale

One scale, applied twice: once to site publishes and once to CMS items. For CMS, staging means the item shows on the staging domain, and production means the item is live on the production domain.

| Level | Sentence to write |
| --- | --- |
| 0 | Agents never publish. |
| 1 | Agents publish to staging, asking each time. |
| 2 | Agents publish to staging freely. Production is published by a person. |
| 3 | Agents publish to staging freely, and to production asking each time. |
| 4 | Agents publish to staging and production freely. |

## Template

Sections marked optional are written only when the user gave content for them. Remove the markers.

```markdown
# {Site name}: Webflow working folder

The site is built and hosted in Webflow, and Webflow is the source of truth. Read pages, classes, CMS items and custom code live before changing them. This folder holds context, a backup of custom code and records of finished jobs. Nothing here is deployed.

## Facts

- **Site:** {display name} (`{site-id}`)
- **Production:** {production URL}
- **Staging:** {staging URL}
- **Owner:** {client}, through {partner agency}
- **Webflow MCP server:** `webflow-{name}` in `.mcp.json`. Reach this site through this server only, and confirm the site ID above before the first read or change.
- **Convention:** {naming convention}
- **Site rules:** read the agent rules and skills stored on the site before building, when it has any.

## Publishing

These levels govern agents. A publish the user makes by hand, or asks for in the conversation, is the user's own.

- **Site: {level}.** {sentence from the scale}
- **CMS: {level}.** {sentence from the scale}

## Outside systems (optional)

- **{System}:** {what it does for the site}. Account owned by {owner}. {Write rule, for a tracker.}

A secret stays where it is kept. Record that place here, and keep the secret itself out of this folder.

## House style (optional)

{Up to five lines: the patterns an agent cannot see on the Style Guide page.}

## Known quirks (optional)

- {What happens, where, and the fix or workaround.}

## Folder layout

- `snippets/` is a backup of the custom code that lives in Webflow. Site-wide files start with `global-` (`global-head.html`, `global-footer.html`), page files are `<page-slug>-head.html` and `<page-slug>-footer.html`, and a registered script or embed is named for what it does. Each file opens with a comment giving its placement in Webflow and the date it was backed up. Before a job changes custom code, compare the live code with its snippet. At the close of the job, refresh the snippets it touched. When the newest backup date is more than a month old, suggest a full refresh and wait for a yes.
- `work/YYYY-MM-<name>/` holds the files a job produces that are worth keeping: its handoff and plan, and any CMS import or export with a note on what moved, when, and the field mapping. Routine edits leave no record.

## Committing

Commit and push to `main` once per workstream, at its close, after the work is final and in production. Changes to this file are committed on their own when they happen.
```

The Owner line is left out for the user's own site, and it drops "through {partner agency}" for a direct client.
