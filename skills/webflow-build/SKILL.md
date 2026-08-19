---
name: webflow-build
description: Build in Webflow using section-based workflow, reuse ladder, native styling, QA gates, and confirmation checkpoints. Use for any Webflow implementation work—from assembling pages with approved components to creating new design-system decisions. Pair with a framework skill (framework/client-first or framework/mast) for class naming and structure grammar.
---

# Webflow Build

Build in Webflow with deliberate reuse, native Designer styling, and completion gates that prevent shipping incomplete work. This skill governs the workflow—how to start, when to ask, what to reuse, and when work is complete. Pair it with a framework skill for naming rules.

Use Webflow's official skills for platform operations (MCP tools, publishing, CMS workflows, technical audits). Use this skill for implementation judgment and quality gates.

## On new work, ask first: where do you want this built?

Default when the user does not pick: a **new unpublished draft/sandbox page**. Do not write onto a live page by default.

## Hard confirmation gates

User confirmation is required before:

- overwriting existing page content
- adding sections to a real/live page
- publishing to staging
- publishing to production

Approving a section on the draft does not promote or publish it.

## Reuse ladder (strict order)

Before creating anything, work through this sequence:

1. **Existing component** — use a component that already owns the responsibility
2. **Existing class** — use a global or project class
3. **Combo class** on an existing class — modify an existing base with a variant
4. **New class** — create only when justified, named to the site style guide or framework
5. **Custom code** — last resort, only for behavior Webflow cannot express

Before creating a new class: confirm a utility or existing pattern cannot do it. Write the justification in the **section plan** before building.

**Style guide wins over framework on class names.** If they disagree, follow the style guide and notify the user.

## Native Webflow styling only

Use Designer-native Style panel fields (or MCP style properties that map to them):

- Height, Width, Max Width
- Margin, Padding
- Display, Position, Flex, Grid (as Webflow exposes them)
- Background (color, image, gradients Designer supports)
- Typography, borders, radius, shadows (as Designer supports)
- Overflow, z-index, opacity, object-fit

**Never invent CSS/Webflow-non-native properties.** Do not use Custom Code embeds, page `<style>`, or Global Canvas CSS to work around Designer restrictions. If Designer cannot set it, approximate with supported tools or tell the user it is unavailable natively.

Custom code is only for behavior Webflow cannot express, never for presentation.

Variables are reusable system tokens, not a backdoor for one-off values that native fields already accept.

See `references/native-styling.md`.

## Never add Webflow labels / Navigator display names

Do not set Webflow labels (the Navigator display name / node name shown in the Webflow Designer Navigator panel) on elements unless the user specifically asked for them. Labeling nodes is a forbidden habit. The Navigator element tree and class names must be sufficient.

## Images are siblings, not children of text

Do not nest Image, icon, or embed nodes inside text elements (span, paragraph, heading, or any other text node). Place images as their own sibling Image / embed / icon node, positioned next to the text rather than nested within it.

## When the full review loop runs

Run the complete **page-plan + section loops** only for:

- a new page
- a new section
- when a new class, combo, or component is needed

**Routine reuse skips the loops.** Copy swaps, CMS item edits, instance-prop changes, and assembling from approved pieces: reuse and report.

## Full loop (nested)

### Page level (outer)

1. **Plan**: List sections + identify reuse opportunities (existing components/classes/utilities; Figma visual-similar search when a Figma source is provided; corresponding live/Webflow sections).
2. Then enter each section, one at a time.

### Section level (inner)

For each section:

1. **Plan / approve** — Surface any new class or combo here, with the reuse trail and written justification. Pause for approval.
2. **Build / approve** — Desktop and mobile. Pause for review.
3. **Component / final approval** — If approved and not already a component, **suggest** turning it into a component; wait for yes. Then move on.

Work one section or component at a time by default.

## Assemble vs invent

### Assemble (light path)

May use:
- existing components
- existing classes
- approved combos
- approved variables and modes
- instance-prop overrides the component supports

May **not**:
- create system classes, components, variables, or interactions
- unlink components to bypass the system
- add custom code to patch around missing capabilities

When the system cannot produce the requested result, stop and describe the missing capability. Do not patch around it with one-off styles, arbitrary wrappers, or duplicated elements.

### Invent (full loop required)

Only when the full page/section loop is active:

- new components, variants, slots, properties
- new classes, variables, modes, or responsive patterns
- new interactions or custom behaviors
- shared-component structural changes
- refactors or consolidations

Still **reuse-first**. Invent authority begins with discovery and reuse, not with creating new classes.

## Shared-component safety

Before changing a shared component definition:

1. Inventory instances, variants, properties, slots, nested components, default content, and consumers.
2. Distinguish definition changes from instance overrides.
3. Record which existing behavior must remain unchanged.
4. Prototype structural work on a duplicate placed on a Sandbox or development page when the blast radius is material.
5. Validate the isolated version before promoting.
6. Verify the original and unrelated instances after promotion.

Never unlink an instance merely to avoid understanding the shared component.

## Diagnose before repairing

When something appears broken:

1. Reproduce the behavior.
2. Verify site, page, component, instance, breakpoint, and environment.
3. Determine whether the discrepancy exists in persisted data, Designer, Preview, staging, or production.
4. Isolate structure, responsive inheritance, component state, CMS data, interaction logic, custom code, or publication state as the cause.
5. Demonstrate the failure before choosing a repair.
6. Apply the smallest repair that preserves the existing contract.

If the user requested diagnosis only, report the cause and proposed repair without making the change.

## Completion gate before presentation

Do not present work as complete until the relevant checks below have been performed. If a verification surface is unavailable, state that clearly instead of implying it passed.

### Structure and system

- The implementation uses the existing system wherever suitable.
- Every new class, variable, component, variant, slot, or behavior has a distinct responsibility.
- Components are small enough to understand, reuse, and approve.
- Shared definitions and unrelated instances remain intact.
- The Navigator, semantic elements, and class stacks are understandable.
- Legacy and replacement implementations are not running simultaneously.
- Presentation uses native Style panel fields (see `references/native-styling.md`).
- No unsupported CSS (e.g. repeating radial backgrounds Designer cannot set).
- No one-off custom properties for Height, Width, Margin, Padding, Display, Position, or Background.
- No new Custom Code embed, page CSS, or Global Canvas CSS dump as a workaround.

### Visual and responsive

- The normal Designer canvas matches the intended base presentation.
- Preview or runtime behavior matches the intended result.
- Desktop, tablet, mobile landscape, and mobile portrait have been checked.
- Text wrapping, media ratios, overflow, stacking, visibility, and decorative positioning work with representative content.
- The result has been compared with the approved design source at relevant viewport sizes.

### Interaction and accessibility

- Default, hover, focus, active, open, closed, selected, disabled, loading, and error states relevant to the component have been checked.
- Keyboard order and activation are usable.
- Focus is visible and managed correctly.
- Escape, touch, reduced motion, and ARIA state are handled where applicable.
- Links, buttons, headings, labels, alternative text, and target sizes use appropriate semantics.

### Evidence and state

- Persisted Webflow readback matches the intended structure and settings.
- Native class stacks and selector chains are valid.
- Original and unrelated shared-component instances were checked after shared changes.
- Saved draft, staging, Webflow subdomain, and production state are distinguished accurately.
- Publication is treated as a separate action and occurs only when explicitly requested.

## Supporting references

- `references/native-styling.md` — Designer-native style fields; no embed or custom-property workarounds
- `references/figma-to-webflow.md` — Figma implementation judgment
- `references/preview-and-state.md` — Designer Preview, runtime custom behavior, and publication-state evidence
- `references/platform-facts.md` — Verified Webflow platform capabilities, Shadow DOM behavior, and Code Component facts
- `references/headless-quirks.md` — MCP tool edge cases, workarounds, and time-sensitive observations

## Handoff

Report:

- what was created, changed, or reused
- which new decisions were approved and which existing approvals were reused
- the QA surfaces actually checked
- anything still unverified
- the current saved, staged, and published state
- any remaining user decision

Lead with the completed result. Do not make the user reconstruct completion from a list of tool calls.
