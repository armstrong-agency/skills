# Copy-paste AGENTS.md for a Webflow site

`AGENTS.md` is a plain text file of rules that an AI coding tool reads at the start of every session. It is where you tell the AI which site it is working on, what it may publish, and what a person has to check first.

This template is the short version of the one I use on client sites. It is adapted from the [`wf-folder-setup`](../skills/wf-folder-setup/SKILL.md) skill in this repository, which sets the same file up for you. It is CC0, so you can use and change it freely.

## How to use it

1. Make a folder on your computer for the site, one folder per Webflow site.
2. Save the template below in that folder as `AGENTS.md`.
3. Replace everything in `{curly braces}`. Delete any line or section you have nothing to put in.
4. If your team uses Claude Code, add a second file named `CLAUDE.md` holding the single line `@AGENTS.md`. Codex and Cursor read `AGENTS.md` on their own.
5. Open your AI tool in that folder. It now reads the rules before it does anything.

Keep the file short. The AI reads your pages, classes, components and CMS from Webflow itself, so none of that belongs here. The file only holds what Webflow cannot tell it.

## Pick your publishing levels

Choose one level for the site and one for CMS items. I recommend level 2 for both until your team has reviewed a few weeks of AI work.

| Level | The sentence to paste |
|---|---|
| 0 | Agents never publish. |
| 1 | Agents publish to staging, asking each time. |
| 2 | Agents publish to staging freely. Production is published by a person. |
| 3 | Agents publish to staging freely, and to production asking each time. |
| 4 | Agents publish to staging and production freely. |

## The template

```markdown
# {Site name}: Webflow working folder

The site is built and hosted in Webflow, and Webflow is the source of truth. Read pages, classes, components and CMS items live from the site before changing them. Nothing in this folder is deployed.

## Facts

- **Site:** {site name} (`{site ID}`)
- **Production:** {production URL}
- **Staging:** {staging URL, ending in .webflow.io}
- **Webflow MCP server:** `webflow-{name}`. Reach this site through this server only, and confirm the site ID above before the first read or change.
- **Naming convention:** {the convention your classes follow, or "none yet"}
- **Style Guide page:** {URL of the site's Style Guide page}

## Publishing

These levels govern agents. A publish a person makes by hand is that person's own.

- **Site: level {0-4}.** {sentence from the scale}
- **CMS: level {0-4}.** {sentence from the scale}

## Building rules

1. Build new work on a draft page, never on a live page.
2. Before creating anything, look for an existing piece, in this order:
   1. An existing component
   2. An existing class
   3. A combo class on an existing class
   4. A new class, only after a person approves its name
   5. Custom code, only for what Webflow cannot do
3. List every new class, component or CMS field you want to create, and wait for a yes before creating it.
4. Keep component instances linked. To change a component, change its definition, and say which pages that affects first.
5. Check every section at desktop, tablet, mobile landscape and mobile portrait before calling it done.
6. Finish every job with a report: what was created, what was changed, what was reused, and anything you could not verify.

## Review before publish

A person checks each of these on staging before anything goes to production:

- [ ] The page uses existing components and matches the Style Guide.
- [ ] No class was created without approval.
- [ ] There is one H1, and the headings run in order.
- [ ] Every image has alt text, and the page has an SEO title and description.
- [ ] The page looks right at all four screen sizes.
- [ ] Forms submit, and links go where they say.
- [ ] No other page changed. Check any page that shares a component with this one.

## Outside systems

- **{System, such as HubSpot or Google Tag Manager}:** {what it does for the site}. Account owned by {person}.

Passwords and API keys stay out of this folder. Write down where each one is kept.

## Known quirks

- {Something about this site that has already cost someone time, and the workaround.}
```

## Three rules I would not remove

1. **One MCP server per site.** The line that ties this folder to one named connection is what keeps an agent from editing the wrong site.
2. **The reuse order.** Without it, an agent builds every section from scratch, and your site fills with one-off classes.
3. **A person publishes to production.** The Webflow MCP saves hours. It still needs someone checking what it changed.
