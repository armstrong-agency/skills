# Client-First

Naming and structure for sites that already follow Finsweet Client-First. This file teaches the structure and class usage Client-First expects — short on purpose. Full pedagogy stays in Finsweet's docs.

Client-First puts the client's interests first in the Webflow build: a project that scales, can be handed off, and uses class names a non-expert can read. Details: [Intro](https://finsweet.com/client-first/docs/intro).

It is built for Webflow Designer workflow and organization — not a traditional HTML/CSS methodology.

**Authority:** user → project instructions / site style guide → what's already on the site → this file. When the project's style guide disagrees with these defaults, follow the style guide.

Sizes in Client-First are in **rem** (relative to the root font size). Prefer rem over px for layout and type. [Sizes and rem](https://finsweet.com/client-first/docs/sizes-and-rem).

## Structure

```text
page-wrapper
  main-wrapper                         <main>
    section_[identifier]               <section>
      padding-global padding-section-[size]
        container-[size]
          [section content]
```

- `page-wrapper` — outermost wrap for all page content
- `main-wrapper` — primary content; use the `<main>` tag
- `section_[identifier]` — one section band; use the `<section>` tag; groups Navigator
- `padding-global` — site-wide left and right padding
- `padding-section-[size]` — site-wide top and bottom section padding (`small` | `medium` | `large`)
- `container-[size]` — content max-width (`small` | `medium` | `large`)

`padding-global` and `padding-section-[size]` are **two utility classes on the same Div** — not a combo class. Container sits inside that Div. Section root is `section_[identifier]`. Component root is `[folder]_component`.

Each wrapper needs a job (layout, size, position, overflow, group). Skip empty ones. Prefer nested layers over stacking many unrelated utilities on one element ([Classes strategy 2](https://finsweet.com/client-first/docs/classes-strategy-2)).

Spacing utilities (`margin-*`, `padding-*`, spacers): use the Client-First spacing system. [Spacing strategy](https://finsweet.com/client-first/docs/spacing-strategy).

## Classes

**Custom** — underscore `_` between folder and element. That underscore also creates a virtual folder in Finsweet's Folders. Hyphens inside a name. Name the role.

```text
feature-grid_component
feature-grid_item
feature-grid_image-wrapper
section_feature-grid
```

**Utility** — no underscore. Global CSS behaviors reused across the site: `padding-global`, `padding-section-large`, `container-large`, `max-width-full`, `overflow-hidden`, `text-size-*`, `text-color-*`, etc.

**Global** — any class (custom or utility) meant to stay unified site-wide. Utilities are always global; a custom class can be global when the same component or pattern is reused everywhere (for example a recurring `header_content`).

**Combo** — `is-` stacked on a base class: `button is-secondary`, `feature-grid_item is-featured`. The `is-` class only works together with its base.

Prefer **utility** classes for shared CSS properties. Prefer **custom** classes for specific components or elements. Don't deep-stack unrelated utilities on one element — nest layers or make one meaningful class instead.

When the cloneable has them: `heading-style-h1`…`h6`, `text-size-*`, `text-weight-*`, `text-color-*`, `text-align-*`, `button` + `is-secondary` / `is-small` / `is-link`. Structure: `container-large|medium|small`, `padding-section-small|medium|large`, `spacer-*`.

## Typography

Prefer default styles on the HTML tags (`body`, `p`, `h1`–`h6`) with **no class**. Add `heading-style-*` or `text-*` utilities only when the instance must differ from the default. Heading **element** is the document/SEO level; heading **class** is the look. [Typography strategy](https://finsweet.com/client-first/docs/typography-strategy).

## Webflow Variables

Use when the project has a Variables panel set up.

1. **Primitives** — the raw scale (for example Neutral / 900).
2. **Semantics** — purpose names that point at primitives in the same collection (for example Text / Primary).

Bind styles to **semantics**. Don't use primitives on elements unless the project has no semantics yet.

For structure and spacing, prefer Client-First utility classes (`padding-global`, `padding-section-*`, `spacer-*`, and the rest). Don't invent spacing or layout variables when a utility already covers it.

Dark mode belongs on the semantic collection when the project uses it.

## Docs

- [Intro](https://finsweet.com/client-first/docs/intro)
- [Core structure](https://finsweet.com/client-first/docs/core-structure-strategy)
- [Classes strategy 2](https://finsweet.com/client-first/docs/classes-strategy-2)
- [Typography](https://finsweet.com/client-first/docs/typography-strategy)
- [Spacing](https://finsweet.com/client-first/docs/spacing-strategy)
- [Sizes and rem](https://finsweet.com/client-first/docs/sizes-and-rem)
