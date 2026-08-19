---
name: client-first
description: Apply Finsweet Client-First naming, structure, and class taxonomy to Webflow projects. Use this skill for the grammar—class names, combo patterns, section structure, and semantic conventions—when a project follows Client-First. Pair with webflow-build for the implementation workflow (reuse ladder, native styling, QA gates).
---

# Client-First Grammar

Use Client-First as the shared grammar that keeps a Webflow site understandable, reusable, and maintainable. This skill governs structure and naming only. Pair it with `webflow-build` for workflow, reuse, and completion gates.

## When to apply

Use this grammar when the project follows Client-First or a documented Client-First-derived system.

Do not convert a site from another established framework merely because Client-First is available. Preserve the site's chosen system unless the user explicitly requests a migration. If the framework is unclear, inspect the style guide, existing classes, components, and project instructions before creating anything.

## Authority order

When conventions differ, follow:

1. Explicit user direction for the current task.
2. Project instructions and documented site conventions.
3. Patterns already established in the actual site and style guide.
4. These Client-First defaults.
5. General Webflow or CSS convention.

**Surface a material conflict instead of silently mixing systems.** If the style guide disagrees with these Client-First defaults, follow the style guide and notify the user.

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

- Apply `padding-global` and `padding-section-[size]` to the same wrapper.
- Place the container inside that wrapper.
- Use `section_[identifier]` for a section root.
- Use `[folder]_component` for a component root.

Do not add wrappers mechanically; each wrapper must own a layout, sizing, positioning, overflow, or grouping responsibility.

## Class taxonomy

### Custom classes

Use an underscore between the folder and element:

```text
feature-grid_component
feature-grid_item
feature-grid_image-wrapper
section_feature-grid
```

Use hyphens within a folder or element name. Name the element's role, not an incidental CSS value.

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

Utilities improve consistency until the class stack becomes difficult to understand or manage in Designer. Avoid deep stacks assembled from many single-purpose utilities.

When an element needs several utilities to express one stable component responsibility, prefer a clear component-specific class. Separate a genuine layout responsibility into another wrapper only when that wrapper improves the structure. Do not create a new class merely to shorten a stack that is already clear and established.

Treat Webflow's visible class list and its native selector-chain metadata as separate facts that both need to be valid. A data readback showing several class names does not prove that Webflow created the intended sequential selector chain. Create and repair stacks through a Webflow-native path, verify the expanded selector list in Designer, and confirm the persisted records.

Never change a global utility to solve one element's stacking problem.

## Elements and semantics

- Use semantic `<main>` and `<section>` structure.
- Use Heading elements at the correct document level; control appearance with existing heading classes or components.
- Use Paragraph elements for paragraph copy.
- Use links for navigation and buttons for actions.
- Use Webflow Label elements only for form controls.
- Use Div Blocks for layout wrappers and purely decorative objects.
- Reuse a design-system component named "Label," "Button," or similar instead of recreating its visual parts with raw elements.
- Remove anonymous or redundant wrappers. A wrapper should have a clear class or a clear structural purpose.

## Typography, spacing, and variables

- Prefer global tag styles and existing typography components.
- Reuse established `heading-style-*`, `text-size-*`, `text-weight-*`, `text-color-*`, and alignment utilities when they exist.
- Keep semantic heading level separate from visual heading size.
- Reuse the site's spacing scale, layout gaps, and padding or margin utilities.
- Keep page gutters, section padding, and maximum width on their proper core structure classes.
- Use existing variables and variable modes instead of duplicating values.
- Create a variable only when it represents a reusable system decision (see `webflow-build` for workflow authority).
- Prefer longhand properties when writing styles through Webflow tooling so a shorthand update does not overwrite an unrelated value.

## Responsive rules

- Start from the main breakpoint and adapt downward deliberately.
- Reuse the site's established breakpoint utilities and combinations.
- Preserve semantic and reading order on mobile.
- Check text wrapping, media ratios, overflow, interactive target sizes, and decorative positioning.
- Avoid fixed heights unless the content and established design require them.
- Do not treat the desktop result as completion.

## Client-First completion check

Before handing the work back:

- The project was confirmed to use Client-First.
- Existing components, classes, utilities, variables, and modes were reused wherever suitable.
- Every new class was created with a distinct, defensible responsibility.
- Custom classes use underscores, utilities use hyphens, and combos use `is-`.
- Class stacks remain understandable and have valid native selector chains.
- Section structure, semantics, typography, spacing, and responsive behavior follow the site's established Client-First system.
- Styles were set via native Style panel fields (see `webflow-build/references/native-styling.md`).
- The Navigator remains understandable without inspecting CSS.

Use the broader completion gate in `webflow-build` for visual, responsive, interaction, component-instance, persisted-state, and publication-state QA.

## Supporting references

- `references/conventions.md` — detailed naming rules, token mapping, and migration cautions

## Canonical references

- https://finsweet.com/client-first/docs/intro
- https://finsweet.com/client-first/docs/classes-strategy-1
- https://finsweet.com/client-first/docs/core-structure-strategy
- https://finsweet.com/client-first/docs/utility-class-systems
- https://finsweet.com/client-first/docs/folders
