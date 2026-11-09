---
name: wf-build
description: Build pages, sections, components, interactions and the Style Guide on a Webflow site over the MCP. Use when building, changing, planning, prototyping or naming classes in Webflow.
---

# Webflow Build

The Webflow site is the record: read context from it, keep the brief and reviews in the conversation, and leave finished work documented in its Style Guide.

## 1. Check context

Done when you can state:

- **Connection:** the MCP reaches the intended workspace, using the tool names this session exposes. If it is missing, run `wf-mcp-setup`.
- **Target:** the site and page.
- **Source of truth:** which of live Webflow, Figma, a screenshot or a written brief is authoritative for what.
- **Style Guide:** present or missing.
- **Grammar:** identified through [grammars.md](references/grammars.md).

Read [common-issues.md](references/common-issues.md) before the first write.

## 2. Route

- **Routine change** (copy swap, CMS item edit, instance-prop change, assembling approved pieces): make it under Build rules, read it back, and report.
- **Style Guide missing:** follow [style-guide.md](references/style-guide.md), then agree the brief.
- **Everything else:** agree the brief.

## 3. Agree the brief

Write it per [brief.md](references/brief.md) and stop until the user approves. Its invent list is the complete set of new pieces: anything that surfaces later comes back for review before it is created.

## 4. Build one section at a time

Work on the sandbox page, climbing the reuse ladder from the top:

1. Existing component
2. Existing class
3. Combo class on an existing class
4. New class from the invent list
5. Custom code, for behavior Webflow cannot express

For a mock-up, stop at rung 3 and report what the system could not do. Before changing a shared component, follow [shared-components.md](references/shared-components.md). When interactions or settings need iteration, create and adjust them freely on the sandbox page and check them in Preview.

## 5. Review each section

Present the section at desktop and mobile against the acceptance checks, and stop until the user approves it. Then add its new classes and variables to the Style Guide, and suggest converting it to a component if it is not one.

Approval covers the sandbox page only. Overwriting page content, moving work onto a real page, and publishing to staging or production each need their own explicit yes.

## 6. Complete

Verify each of these, and name any surface you could not reach:

- Canvas and Preview match the brief at desktop, tablet, mobile landscape and mobile portrait.
- States, interactions and keyboard order work where they exist.
- Persisted readback matches the intended structure.
- Shared definitions and unrelated instances are intact, and no legacy implementation runs beside its replacement.

Report the result first, then what was created, changed and reused, anything unverified, and whether it is saved, staged or published.

## Build rules

- Style through Designer's Style panel fields or the MCP properties that map to them. If Designer cannot set a value, approximate it with supported tools or tell the user.
- Custom code carries behavior only, so keep presentation out of embeds, page `<style>` and Global Canvas CSS.
- Leave Navigator labels unset unless the user asks.
- Place Image, icon and embed nodes as siblings of text nodes.
- Use Webflow Label elements only for form controls.
- Fix one element's stacking locally, leaving global utilities unchanged.
