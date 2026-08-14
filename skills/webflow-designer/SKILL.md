---
name: webflow-designer
description: Design, build, extend, and refactor Webflow pages and reusable systems with agency-grade review built into completion. Use for new components, sections, classes, variables, variants, responsive patterns, interactions, custom behavior, shared-component changes, Figma implementation, or any request the existing approved system cannot satisfy. Reuse existing work first, build from small approved components, and complete visual, responsive, interaction, component-instance, and persisted-state QA before presenting the result.
---

# Webflow Designer

Create or change reusable design decisions without weakening the system that is
already there. The Designer role has broader authority than
`webflow-marketer`, but that authority begins with discovery and reuse--not with
creating new classes.

Use the project's framework skill (`client-first` or `mast`) alongside this
skill when applicable. Use Webflow's official skills or current platform
guidance for tool mechanics; this skill governs implementation judgment, review
boundaries, and what counts as complete.

## Designer authority

Use this role when the work requires:

- a new reusable component or section pattern;
- a new class, variable, mode, or design token;
- a new component property, variant, slot, or default;
- a shared-component structural change;
- a new responsive or interaction pattern;
- a new component-scoped custom behavior;
- a refactor or consolidation of repeated patterns;
- translation of an approved design into new Webflow structure;
- repair of a defect that exposes a missing system capability.

Designer authority is not permission to replace the existing system
wholesale. Preserve approved components, content, conventions, and decisions
that remain valid.

## Discover before designing

Before creating anything:

1. Verify the exact site, page, component, environment, and
   saved-versus-published state.
2. Read project instructions and identify the approved design and content
   sources.
3. Inspect existing components, instances, properties, variants, slots,
   classes, variables, modes, layouts, responsive patterns, interactions,
   assets, CMS relationships, and custom-code contracts.
4. Inspect nearby approved implementations and the style guide.
5. Map the requested design to existing pieces.
6. Identify the smallest capability the current system is actually missing.

Do not create a class, wrapper, component, or behavior until its unique
responsibility can be stated. Reuse an existing piece when its responsibility
and meaning match, not merely because it looks similar.

## Build approval upward

Break new work into the smallest coherent, reusable units:

```text
existing approved foundations
  new or approved primitive
    new or approved component
      new or approved section
        completed page or experience
```

Approval compounds. A larger item should be composed from smaller approved
items, so reviewing the larger item focuses on composition and the few
remaining decisions rather than reopening every underlying choice.

Use these rules:

- Reuse an approved unit without asking for the same approval again.
- Isolate a genuinely new visual, structural, content, or behavior decision so
  the user can evaluate it clearly.
- Prefer small components with one clear responsibility and an explicit
  interface.
- Avoid a large unreviewed component that hides several unrelated decisions.
- Do not turn every wrapper into a component; create a boundary only when the
  unit is reusable, independently understandable, or needs controlled content
  or behavior.
- Treat approval as a design-decision boundary, not a confirmation prompt for
  every mechanical implementation step.

## Native Webflow first

Use native Style panel fields (or MCP style properties that map to them)
before variables, and variables before custom CSS. Height, Width, Max Width,
Margin, Padding, Display, Position, Background, typography, borders, radius,
shadows, overflow, z-index, and opacity belong on the class in Designer.

See `references/native-styling.md`.

Build layout, sizing, positioning, visibility, responsive behavior, and
reusable presentation with those native fields wherever practical. The
normal Designer canvas should communicate the component's base structure
and appearance without relying on page-level scripts or hidden CSS.

Do not create a Webflow variable for a one-off value a native field already
accepts. Variables are reusable system tokens, not a styling backdoor.

If Designer has no control for a CSS feature, do not fake it with an embed
or `<style>` block. Approximate with supported tools or tell the user it is
not available natively.

Custom code is only for behavior Webflow cannot express, never for ordinary
presentation or to dodge framework or Designer rules. When custom behavior
is needed:

- keep base content, layout, and appearance usable without JavaScript;
- scope the controller to a component root;
- use `data-*` attributes as behavior hooks instead of styling classes;
- provide sensible local defaults and use explicit wiring for overrides or
  cross-component relationships;
- make initialization safe to run more than once;
- include keyboard, focus, Escape, touch, reduced-motion, and ARIA behavior
  where applicable;
- remove or disable the superseded implementation so legacy and replacement
  behavior do not run together.

## Create the fewest new system decisions

For each need, prefer:

1. Existing component.
2. Existing component property or variant.
3. Existing global or project class.
4. Existing framework utility.
5. Existing custom class with the same responsibility.
6. Existing combo or state class.
7. New component-specific class.
8. New reusable utility or token only when several contexts need it.

Keep class stacks readable in Designer. If many utilities collectively express
one stable component responsibility, a clear component-specific class may be
more maintainable. Do not create a new class for a value that an approved
variable, utility, or component already owns.

## Shared-component safety

A component definition change can affect pages outside the visible task.
Before changing one:

1. Inventory its instances, variants, properties, slots, nested components,
   default content, and known consumers.
2. Distinguish a definition change from an instance override.
3. Record which existing behavior must remain unchanged.
4. Prototype structural work on a duplicate placed on a Sandbox or development
   page when the blast radius is material.
5. Validate the isolated version before promoting the change.
6. Verify the original and unrelated instances after promotion.

If a nested transformation cannot be performed safely inside the definition,
use a controlled duplicate, insert, unlink, and inner-to-outer transformation
workflow. Never unlink an instance merely to avoid understanding the shared
component.

## Diagnose before repairing

When something appears broken:

1. Reproduce the behavior.
2. Verify the site, page, component, instance, breakpoint, and environment.
3. Determine whether the discrepancy exists in persisted data, Designer,
   Preview, staging, or production.
4. Isolate structure, responsive inheritance, component state, CMS data,
   interaction logic, custom code, or publication state as the cause.
5. Demonstrate the failure before choosing a repair.
6. Apply the smallest repair that preserves the existing contract.

If the user requested diagnosis only, report the cause and proposed repair
without making the change.

## Completion gate before presentation

Do not present a Designer task as complete until the relevant checks below have
been performed. If a verification surface is unavailable, state that clearly
instead of implying it passed.

### Structure and system

- The implementation uses the existing system wherever suitable.
- Every new class, variable, component, variant, slot, or behavior has a
  distinct responsibility.
- Components are small enough to understand, reuse, and approve.
- Shared definitions and unrelated instances remain intact.
- The Navigator, semantic elements, and class stacks are understandable.
- Legacy and replacement implementations are not running simultaneously.
- Presentation uses native Style panel fields (see `references/native-styling.md`).
- No unsupported CSS (for example repeating radial backgrounds Designer cannot set).
- No one-off custom properties standing in for Height, Width, Margin, Padding,
  Display, Position, or Background.
- No new Custom Code embed, page CSS, or Global Canvas CSS dump as a workaround.

### Visual and responsive

- The normal Designer canvas matches the intended base presentation.
- Preview or runtime behavior matches the intended result.
- Desktop, tablet, mobile landscape, and mobile portrait have been checked.
- Text wrapping, media ratios, overflow, stacking, visibility, and decorative
  positioning work with representative content.
- The result has been compared with the approved design source at the relevant
  viewport sizes.

### Interaction and accessibility

- Default, hover, focus, active, open, closed, selected, disabled, loading, and
  error states relevant to the component have been checked.
- Keyboard order and activation are usable.
- Focus is visible and managed correctly.
- Escape, touch, reduced motion, and ARIA state are handled where applicable.
- Links, buttons, headings, labels, alternative text, and target sizes use
  appropriate semantics.

### Evidence and state

- Persisted Webflow readback matches the intended structure and settings.
- Native class stacks and selector chains are valid.
- Original and unrelated shared-component instances were checked after shared
  changes.
- Saved draft, staging, Webflow subdomain, and production state are
  distinguished accurately.
- Publication is treated as a separate action and occurs only when explicitly
  requested.

## Supporting references

- `references/native-styling.md` -- Designer-native style fields; no embed or custom-property workarounds.
- `references/figma-to-webflow.md` -- Figma, node, or screenshot -> Webflow implementation judgment.
- `references/preview-and-state.md` -- Designer Preview, runtime custom behavior, and publication-state evidence.
- `references/platform-facts.md` -- Verified Webflow platform capabilities, Shadow DOM behavior, and Code Component facts.
- `references/headless-quirks.md` -- MCP tool edge cases, workarounds, and time-sensitive observations.
- `references/roles.md` -- Marketer vs Designer authority boundaries and when to switch roles.

## Handoff

Report:

- what was created, changed, or reused;
- which new decisions were approved and which existing approvals were reused;
- the QA surfaces actually checked;
- anything still unverified;
- the current saved, staged, and published state;
- any remaining user decision.

Lead with the completed result. Do not make the user reconstruct completion
from a list of tool calls.
