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
- **Source of truth:** which of live Webflow, Figma, a screenshot or a written brief is authoritative for what. When Figma is a source, follow [figma.md](references/figma.md) before the first Figma call.
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

Work component-forward. Before placing a heading, button, link, icon or spacer, search the site's components and use the one whose job matches, so an `Atom / Heading` component wins over a new heading class. Judge the fit: a component that is close but wrong for the job stays unused, and the gap goes in the report.

For a prototype, stop at rung 3 and note what the system could not do. Read [finsweet-attributes.md](references/finsweet-attributes.md) for a section with `fs-*` attributes, [swiper.md](references/swiper.md) for a Swiper slider, and [shared-components.md](references/shared-components.md) before changing a shared component. Create and adjust interactions and settings freely on the sandbox page, checking them in Preview.

Done when every section in the brief exists on the page.

## 5. Review, one section at a time

Follow [review.md](references/review.md): review each section yourself against the brief and its design source, then present each to the user and stop for approval.

Done when the user has approved every section.

## 6. Complete

Done when every section is approved and these hold, naming any surface you could not reach:

- Shared definitions and unrelated instances are intact.
- No legacy implementation runs beside its replacement.

Report the result first, then what was created, changed and reused, anything unverified, and whether the work is staged or published.

## Build rules

- Style through Designer's Style panel fields or the MCP properties that map to them.
- Keep custom code to a minimum: behavior Webflow cannot express, and CSS only for a value Designer cannot set. Put custom CSS where the grammar file says, and with no rule there, ask the user where it goes.
- Text goes on a Text Block, Heading, Paragraph or Text Link, never a Div Block, even when it's bound to the CMS. When copying an existing row, check its element types first, and fix any Divs holding text.
- Keep component instances linked, and fix the definition.
- Use Webflow Label elements only for form controls.
- Fix one element's stacking locally, leaving global utilities unchanged.
