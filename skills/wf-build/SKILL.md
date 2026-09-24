---
name: wf-build
description: Implement Webflow work with the reuse ladder, native Designer styling, confirmation gates, and completion evidence. Use when building pages, creating justified new classes or components, promoting approved sandbox work, or making system decisions. Pair with a framework grammar skill for naming. Never publish unless the user explicitly asks.
---

# Webflow Build

Implement in Webflow with deliberate reuse, native Designer styling, and gates that keep incomplete work from being treated as shipped. Use `wf-plan` when the page/section plan is missing. Use `wf-prototype` when the user only wants a sandbox assemble.

Use Webflow's official skills for platform operations (MCP tool mechanics, publishing workflows, CMS operations, technical audits). This skill is implementation judgment.

If this build runs through a long-lived coding agent (a cloud or local worker), follow references/agent-runs.md for briefing, the turn budget, the handoff file and scoped reads.

## Grammar first

Do this before naming or creating a class:

1. Inspect the Style Guide, existing classes, and project instructions.
2. Name the convention: Client-First, Mast, mixed, or none.
3. If a matching `grammar/*` skill is installed, **read that skill now**. Do not write class names from memory or from a different grammar.
4. If the convention is unclear, say so and wait. Do not pick a grammar because it is installed.

**Style guide wins over framework on class names.** If they disagree, follow the style guide and notify the user.

## Discover tools, then act

Do not assume Webflow MCP tool or action names. List the tools and actions exposed in this session and use those. Revalidate a named action before depending on it. Read `references/common-issues.md` for combo attachment, nesting, Designer session, variable scoping, and publishing quirks.

## Destination and confirmation

Ask where to build if `wf-plan` did not already lock it. Default for new work: a **new unpublished draft/sandbox page**.

User confirmation is required before:

- overwriting existing page content
- adding sections to a real/live page
- publishing to staging
- publishing to production

Approving a section on a draft does not promote or publish it.

## Reuse ladder (strict order)

Before creating anything:

1. **Existing component** — use a component that already owns the responsibility
2. **Existing class** — use a global or project class
3. **Combo class** on an existing class
4. **New class** — only when justified, named to the style guide or loaded grammar
5. **Custom code** — last resort, only for behavior Webflow cannot express

Write the justification in the section plan before building a new class. Confirm a utility or existing pattern cannot do it.

## Native Webflow styling only

Use Designer-native Style panel fields (or MCP style properties that map to them): Height, Width, Max Width, Margin, Padding, Display, Position, Flex, Grid as Webflow exposes them, Background (color, image, gradients Designer supports), typography, borders, radius, shadows as Designer supports, Overflow, z-index, opacity, object-fit.

Never invent CSS Webflow cannot set. Do not use Custom Code embeds, page `<style>`, or Global Canvas CSS to work around Designer restrictions. If Designer cannot set it, approximate with supported tools or tell the user it is unavailable natively.

Custom code is only for behavior Webflow cannot express, never for presentation. Variables are reusable system tokens, not a backdoor for one-off values native fields already accept.

## Hard structure rules

- **No Navigator labels** unless the user asked. Class names and the element tree must be enough.
- **Images are siblings, not children of text.** Do not nest Image, icon, or embed nodes inside span, paragraph, heading, or other text nodes. Place them as their own sibling nodes next to the text.

## Elements and semantics

- Use semantic `<main>` and `<section>` structure.
- Heading elements at the correct document level; control appearance with classes or components.
- Paragraph elements for paragraph copy.
- Links for navigation, buttons for actions.
- Webflow Label elements only for form controls.
- Div Blocks for layout wrappers and purely decorative objects.
- Reuse a design-system component named "Label," "Button," or similar instead of recreating its visual parts with raw elements.
- Remove anonymous or redundant wrappers. A wrapper should have a clear class or a clear structural purpose.

## Class stacks

Utilities improve consistency until the stack is hard to understand in Designer. Avoid deep stacks of single-purpose utilities.

When several utilities express one stable component responsibility, prefer a component-specific class. Split a genuine layout responsibility onto another wrapper only when that wrapper improves the structure. Do not create a class merely to shorten a stack that is already clear.

Treat Webflow's visible class list and its native selector-chain metadata as separate facts. A data readback of several class names does not prove the intended sequential selector chain. Create and repair stacks through a Webflow-native path, verify the expanded selector list in Designer, and confirm the persisted records.

Never change a global utility to solve one element's stacking problem.

## Responsive

- Start from the main breakpoint and adapt downward deliberately.
- Reuse the site's established breakpoint utilities and combinations.
- Preserve semantic and reading order on smaller breakpoints.
- Check text wrapping, media ratios, overflow, interactive target sizes, and decorative positioning.
- Avoid fixed heights unless the content and established design require them.
- Do not treat the desktop result as completion.

## When the full loop runs

Run page-plan + section loops only for a new page, a new section, or when a new class, combo, or component is needed. Routine reuse (copy swaps, CMS item edits, instance-prop changes, assembling approved pieces) skips the loops: reuse and report.

If no plan exists yet, run `wf-plan` (or the same planning steps) before inventing.

### Page level

1. Plan: list sections and reuse opportunities.
2. Enter each section one at a time.

### Section level

1. **Plan / approve** — new class or combo, reuse trail, written justification. Pause.
2. **Build / approve** — desktop and mobile. Pause.
3. **Component / final approval** — if approved and not already a component, **suggest** converting; wait for yes.

## Invent (only with the loop)

New components, variants, slots, properties, classes, variables, modes, responsive patterns, interactions, shared-component structural changes, refactors. Still reuse-first. Invent starts with discovery, not with a new class.

## Shared-component safety

Before changing a shared definition:

1. Inventory instances, variants, properties, slots, nested components, default content, and consumers.
2. Distinguish definition changes from instance overrides.
3. Record which existing behavior must remain unchanged.
4. Prototype structural work on a duplicate on a sandbox page when blast radius is material.
5. Validate the isolated version before promoting.
6. Verify the original and unrelated instances after promotion.

Never unlink an instance merely to avoid understanding the shared component.

## Completion gate before presentation

Do not present work as complete until the relevant checks have been performed. If a verification surface is unavailable, say so.

### Structure and system

- Grammar skill was loaded; style guide followed on names
- Existing system used wherever suitable
- Every new class, variable, component, variant, slot, or behavior has a distinct responsibility
- Shared definitions and unrelated instances remain intact
- Navigator, semantics, and class stacks are understandable
- Legacy and replacement implementations are not both running
- Native Style panel only
- No unsupported CSS, one-off custom properties for native fields, or embed/CSS dumps

### Visual, interaction, evidence

- Designer canvas and Preview/runtime match intent at desktop, tablet, mobile landscape, and mobile portrait
- Relevant hover/focus/open/disabled states, keyboard order, and semantics checked
- Persisted Webflow readback matches the intended structure
- Saved draft, staging, Webflow subdomain, and production are distinguished
- Publication only when explicitly requested

See `references/common-issues.md` when canvas, Preview, publication state, MCP, or platform limits matter.

## Handoff

```text
Result:
Grammar: [client-first | mast | mixed | none]
Created / changed / reused:
Approvals given:
Checked: [canvas / Preview / readback / breakpoints]
Unverified:
Saved vs staged vs published:
Remaining user decisions:
```

Lead with the completed result. Do not make the user reconstruct completion from a list of tool calls.
