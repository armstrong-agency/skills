---
name: wf-site-rules
description: Write one short build-rules entry into a Webflow site's own agent rules, so a client's agent or another developer builds the way the site was built. Use when handing a site over, finishing a build, or the user says "site rules", "agent rules", "write the rules to the site" or asks what the next agent on this site needs to know.
---

# Webflow Site Rules

Write one short rules entry into the site's agent rules: the build knowledge a stranger's agent needs and cannot read off the site. The entry lives on the site, so it reaches every agent that opens the site, with no working folder.

This skill writes that one entry and nothing else. It adds no on-site skills, and it leaves Webflow's generated guideline drafts (brand, design system, assets, CMS) as it finds them: neither generated, edited nor removed.

## 1. Check context

Done when you can state:

- **Connection:** the MCP reaches the intended workspace, using the tool names this session exposes. If it is missing, run `wf-mcp-setup`.
- **Target:** the site.
- **Rules surface:** which tool in this session reads and writes the site's agent rules, found in-session. If none does, stop and tell the user; write the draft into the conversation for them to paste in.
- **Existing rules:** every entry already on the site, read in full.

## 2. Read the site

Gather only what the entry needs, from the site itself:

- **Naming:** the convention in use, identified through `wf-build`'s [grammars.md](../wf-build/references/grammars.md), and where the site departs from it.
- **Reuse:** the Style Guide page, the components meant for reuse, and the variable collections that hold the tokens.
- **Do not touch:** shared components with many instances, legacy classes kept for a reason, custom code and attribute-driven pieces that break when restructured, and pages or collections the user names.

Ask the user for anything on the do-not-touch list that the site cannot show, such as a section kept for a campaign.

## 3. Draft the entry

One entry, at most 20 short lines, under these three headings in this order:

```text
Naming
- <convention and version>. <where this site departs from it>.

Reuse before inventing
- Style Guide: <page name>.
- Components: <names, with what each is for>.
- Tokens: <variable collections>.

Do not touch
- <piece>: <reason in a few words>.
```

Each line passes when:

- **Not readable off the site:** an agent listing classes, components and variables would not learn it. Point at the Style Guide; never restate its values.
- **Stable:** it stays true through ordinary page work. Leave out anything about the current job, brief or review.
- **About building:** brand voice, copy rules and CMS editorial rules belong elsewhere.
- **Public-safe on the site:** no credentials, no notes about people, nothing the client should not read.

If the draft runs past 20 lines, cut the lines an agent would get right anyway.

## 4. Agree it

Show the draft and stop until the user approves it. When the site already has rules:

- **An earlier entry from this skill:** show a diff against it and replace it on approval.
- **Anyone else's entry:** leave it unchanged. If it conflicts with the draft, show both and let the user decide which gives way.

## 5. Write and read back

Write the approved entry, read it back, and confirm it matches. Writing rules does not publish the site, and nothing here needs a publish.

Report the entry as written, any existing entries left in place, and anything you could not read on the site.

## Keeping it true

Update the entry when a line in it stops being true: a renamed component, a new do-not-touch piece, a change of convention. Other work on the site leaves it alone.
