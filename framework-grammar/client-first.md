# Client-First

Naming and structure for sites that already follow Finsweet Client-First. Follow the project's style guide when it disagrees with these defaults.

Authority: user → project instructions → what's already on the site → this file.

## Structure

```text
page-wrapper
  main-wrapper                         <main>
    section_[identifier]               <section>
      padding-global padding-section-[size]
        container-[size]
          [section content]
```

`padding-global` and `padding-section-[size]` go on the same wrapper. Container sits inside it. Section root is `section_[identifier]`. Component root is `[folder]_component`.

Each wrapper needs a job (layout, size, position, overflow, group). Skip empty ones.

## Classes

**Custom** — underscore between folder and element. Hyphens inside a name. Name the role.

```text
feature-grid_component
feature-grid_item
feature-grid_image-wrapper
section_feature-grid
```

**Utility** — hyphens, global behavior: `padding-global`, `padding-section-large`, `container-large`, `max-width-full`, `overflow-hidden`.

**Combo** — `is-` on a base class: `button is-secondary`, `feature-grid_item is-featured`.

When the cloneable has them: `heading-style-h1`…`h6`, `text-size-*`, `text-weight-*`, `text-color-*`, `text-align-*`, `button` + `is-secondary` / `is-small` / `is-link`. Structure: `container-large|medium|small`, `padding-section-small|medium|large`, `spacer-*`.

Heading **element** is the document level. Heading **class** is the look.

## Variables

1. **Primitives** — scale groups (`Neutral / 900`). Don't bind a style directly to a primitive.
2. **Semantics** — purpose names, aliased to primitives in the **same** collection. `Category / Name` → `--category--name`.
3. **Structure** — Client-First classes, not variables. Spacing stays on utilities.

Dark mode belongs on the semantic collection, natively.

Human docs: https://finsweet.com/client-first/docs/intro
