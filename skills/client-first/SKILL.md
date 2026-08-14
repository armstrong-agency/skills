---
name: client-first
description: Apply Finsweet Client-First rules to Webflow structure, class naming, utilities, components, responsive behavior, and Navigator organization. Use whenever a Webflow project follows Client-First or Relume conventions, including page assembly, component work, refactoring, and class cleanup. Preserve the site's existing implementation of Client-First before introducing any new class or pattern.
---

# Client-First Rules

Use Client-First as the shared grammar that keeps a Webflow site understandable,
reusable, and maintainable. This skill governs structure and naming. Pair it
with `webflow-marketer` for approved page assembly or `webflow-designer` for
new design-system decisions.

## Confirm the framework

Apply these rules when the project uses Client-First or a documented
Client-First-derived system.

Do not convert a site from another established framework merely because
Client-First is available. Preserve the site's chosen system unless the user
explicitly requests a migration. If the framework is unclear, inspect the
style guide, existing classes, components, and project instructions before
creating anything.

## Authority order

When conventions differ, follow:

1. Explicit user direction for the current task.
2. Project instructions and documented site conventions.
3. Patterns already established in the actual site and style guide.
4. These Client-First defaults.
5. General Webflow or CSS convention.

Surface a material conflict instead of silently mixing systems.

## Reuse before creation

Before adding a class or element:

1. Inspect nearby sections, components, variables, modes, and responsive
   patterns.
2. Search for an existing component that owns the responsibility.
3. Search for an existing global or project class.
4. Search for an existing Client-First utility.
5. Check whether a valid `is-` combo class already expresses the variant.
6. Create a component-specific class only in the Designer role and only when
   no suitable approved pattern exists.
7. Create a utility only when the behavior is genuinely global and reusable.

Do not assume a familiar Client-First or Relume class exists. Verify it in the
current site.

The Marketer role may use existing classes and approved class combinations but
may not create new ones. A missing class, variable, variant, or component is a
Designer decision.

## Native Webflow styles

Set Height, Width, Margin, Padding, Display, Position, Background, and other
presentation on the class through Designer-native Style panel fields (or MCP
properties that map to them). Do not invent a CSS custom property for a
one-off value those fields already accept.

Do not implement Client-First structure or decoration with custom CSS, a
Custom Code embed, page `<style>`, or Global Canvas CSS. If Designer has no
control for a CSS feature, approximate with supported tools or tell the user
it is not available natively -- do not embed a workaround.

See `webflow-designer` -> `references/native-styling.md`.

## Core structure

Use the current Client-First section structure:

```text
page-wrapper
  main-wrapper                         <main>
    section_[identifier]               <section>
      padding-global padding-section-[size]
        container-[size]
          [section content]
```

Apply `padding-global` and `padding-section-[size]` to the same wrapper. Place
the container inside that wrapper.

Use `section_[identifier]` for a section root and `[folder]_component` for a
real component root. Do not add wrappers mechanically; each wrapper must own a
layout, sizing, positioning, overflow, or grouping responsibility.

## Class taxonomy

### Custom classes

Use an underscore between the folder and element:

```text
feature-grid_component
feature-grid_item
feature-grid_image-wrapper
section_feature-grid
```

Use hyphens within a folder or element name. Name the element's role, not an
incidental CSS value.

### Utility classes

Use hyphens only for reusable global behavior:

```text
padding-global
padding-section-large
container-large
max-width-full
text-style-3lines
overflow-hidden
```

### Combo classes

Use `is-` for a variant or state that depends on a base class:

```text
button is-secondary
label is-dark
feature-grid_item is-featured
```

Do not introduce BEM `--` modifiers or an additional modifier system.

## Keep class stacks readable

Utilities improve consistency until the class stack becomes difficult to
understand or manage in Designer. Avoid deep stacks assembled from many
single-purpose utilities.

When an element needs several utilities to express one stable component
responsibility, prefer a clear component-specific class in the Designer role.
Separate a genuine layout responsibility into another wrapper only when that
wrapper improves the structure. Do not create a new class merely to shorten a
stack that is already clear and established.

Treat Webflow's visible class list and its native selector-chain metadata as
separate facts that both need to be valid. A data readback showing several
class names does not prove that Webflow created the intended sequential
selector chain. Create and repair stacks through a Webflow-native path, verify
the expanded selector list in Designer, and confirm the persisted records.

Never change a global utility to solve one element's stacking problem.

## Elements and semantics

- Use semantic `<main>` and `<section>` structure.
- Use Heading elements at the correct document level; control appearance with
  existing heading classes or components.
- Use Paragraph elements for paragraph copy.
- Use links for navigation and buttons for actions.
- Use Webflow Label elements only for form controls.
- Use Div Blocks for layout wrappers and purely decorative objects.
- Reuse a design-system component named "Label," "Button," or similar instead
  of recreating its visual parts with raw elements.
- Remove anonymous or redundant wrappers. A wrapper should have a clear class
  or a clear structural purpose.

## Typography, spacing, and variables

- Prefer global tag styles and existing typography components.
- Reuse established `heading-style-*`, `text-size-*`, `text-weight-*`,
  `text-color-*`, and alignment utilities when they exist.
- Keep semantic heading level separate from visual heading size.
- Reuse the site's spacing scale, layout gaps, and padding or margin utilities.
- Keep page gutters, section padding, and maximum width on their proper core
  structure classes.
- Use existing variables and variable modes instead of duplicating values.
- Create a variable only in the Designer role and only when it represents a
  reusable system decision.
- Prefer longhand properties when writing styles through Webflow tooling so a
  shorthand update does not overwrite an unrelated value.

## Responsive rules

- Start from the main breakpoint and adapt downward deliberately.
- Reuse the site's established breakpoint utilities and combinations.
- Preserve semantic and reading order on mobile.
- Check text wrapping, media ratios, overflow, interactive target sizes, and
  decorative positioning.
- Avoid fixed heights unless the content and established design require them.
- Do not treat the desktop result as completion.

## Client-First completion check

Before handing the work back:

- The project was confirmed to use Client-First.
- Existing components, classes, utilities, variables, and modes were reused
  wherever suitable.
- Every new class was created under Designer authority and has a distinct,
  defensible responsibility.
- Custom classes use underscores, utilities use hyphens, and combos use `is-`.
- Class stacks remain understandable and have valid native selector chains.
- Section structure, semantics, typography, spacing, and responsive behavior
  follow the site's established Client-First system.
- Styles were set via native Style panel fields; no workaround embeds or
  unsupported CSS.
- The Navigator remains understandable without inspecting CSS.

Use the broader completion gate in `webflow-designer` for visual, responsive,
interaction, component-instance, persisted-state, and publication-state QA.

## Supporting references

- `references/conventions.md` -- detailed naming rules, token mapping, and migration cautions.
- `webflow-designer/references/native-styling.md` -- native Style panel first; no embed loophole.

## Canonical references

- https://finsweet.com/client-first/docs/intro
- https://finsweet.com/client-first/docs/classes-strategy-1
- https://finsweet.com/client-first/docs/core-structure-strategy
- https://finsweet.com/client-first/docs/utility-class-systems
- https://finsweet.com/client-first/docs/folders
