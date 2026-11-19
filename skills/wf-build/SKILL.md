---
name: wf-build
description: Build pages, sections, components, interactions and the Style Guide on a Webflow site over the MCP. Use when building, changing, planning, prototyping, naming classes or components, or writing a site's agent instructions in Webflow.
---

# Webflow Build

The Webflow site is the record: read context from it, keep the brief and reviews in the conversation, and keep its Style Guide to the site's reusable foundations.

The **four breakpoints** are desktop (checked at 1440 px), tablet (991), mobile landscape (767) and mobile portrait (390).

## 1. Check context

Done when you can state:

- **Connection:** the MCP reaches the intended workspace, using the tool names this session exposes. If it is missing, run `wf-mcp-setup`.
- **Target:** the site and page.
- **Source of truth:** which of live Webflow, Figma, a screenshot or a written brief is authoritative for what. Figma node data proves structure, text styles, variables and measurements; a raster proves only that capture, so calibrate its scale before measuring from it. When Figma is a source, follow [figma.md](references/figma.md) before the first Figma call.
- **Style Guide:** present or missing.
- **Grammar:** identified through [grammars.md](references/grammars.md).
- **Site instructions:** the agent rules and skills stored on the site, each one read.

Read [common-issues.md](references/common-issues.md) before the first write.

## 2. Route

- **Routine change** (copy swap, CMS item edit, instance-prop change, assembling approved pieces): make it under Build rules, read it back, and report.
- **Style Guide missing:** follow [style-guide.md](references/style-guide.md), then agree the brief.
- **Component library:** to name, describe or audit components, follow [components.md](references/components.md). To write the site's agent instructions, follow [site-instructions.md](references/site-instructions.md).
- **Everything else:** agree the brief.

## 3. Agree the brief

Write it per [brief.md](references/brief.md) and stop until the user approves. Its invent list is the complete set of new pieces: anything that surfaces later comes back for review before it is created.

## 4. Build the page, one section at a time

Build each section in brief order on the brief's destination, the sandbox page by default, and move to the next without stopping for review. Climb the reuse ladder from the top:

1. Existing component
2. Existing class
3. Combo class on an existing class
4. New class from the invent list
5. Custom code, for what Webflow cannot express

Rung 1 covers atoms. Before placing a heading, button, link, icon or spacer, search the site's components for it and place an instance of the match, so an `Atom / Heading` component wins over a new heading class.

For a prototype, stop at rung 3 and note what the system could not do. When a section uses Finsweet Attributes List (`fs-list-*`), read [finsweet.md](references/finsweet.md). Before changing a shared component, follow [shared-components.md](references/shared-components.md). Create and adjust interactions and settings freely on the sandbox page, checking them in Preview.

Done when every section in the brief exists on the page.

## 5. Agent review, one section at a time

Review each section in order against the brief and its design source, fix what fails, and re-check until it passes. Dispatch a reviewer subagent per section when the harness allows, so the read is fresh; give it the brief, the section's design source and the page, and fix what it finds. When canvas snapshots fail or a check needs published output, follow [staging-check.md](references/staging-check.md). A section passes when:

- **Complete:** every element, state and interaction in its design source exists, and nothing outside the brief was added.
- **Faithful:** Canvas and Preview match the acceptance checks at the four breakpoints, from Figma node data where it exists.
- **Working:** states, interactions and keyboard order behave where they exist.
- **Persisted:** readback matches the intended structure.

Done when every section passes, or each remaining gap is logged with the reason it cannot close.

## 6. Human review, one section at a time

Present each section in order at desktop and mobile, with its agent-review result and any logged gaps, and stop until the user approves it. Apply requested changes and re-run the agent review on that section before presenting it again. After approval, suggest converting the section to a component if it is not one, named and described per [components.md](references/components.md). When it introduced a reusable piece, such as a variable, utility, or base class meant for other sections, propose adding that piece to the Style Guide. Classes that belong to one section stay on that section.

Approval covers the sandbox page only. Overwriting page content and moving work onto a real page each need their own explicit yes. Publishing follows the publishing levels in the project's `AGENTS.md`. Where it has none, each publish to staging or production needs its own explicit yes, and you ask about staging publishes at the start of the workstream.

## 7. Complete

Done when every section is approved and these hold, naming any surface you could not reach:

- Shared definitions and unrelated instances are intact.
- No legacy implementation runs beside its replacement.

Report the result first, then what was created, changed and reused, anything unverified, and whether the work is staged or published. Webflow saves automatically, so saving is the baseline, not a step.

## Build rules

- Style through Designer's Style panel fields or the MCP properties that map to them.
- Keep custom code to a minimum: behavior Webflow cannot express, and CSS only for a value Designer cannot set. Put custom CSS where the grammar file says, and with no rule there, ask the user where it goes.
- Text goes on a Text Block, Heading, Paragraph or Text Link, never a Div Block, even when it's bound to the CMS. When copying an existing row, check its element types first, and fix any Divs holding text.
- Place Image, icon and embed nodes as siblings of text nodes.
- Keep component instances linked: fix the definition, or insert into a parent and reorder when an insert fails.
- Use Webflow Label elements only for form controls.
- Leave Navigator labels unset unless the user asks.
- Fix one element's stacking locally, leaving global utilities unchanged.
