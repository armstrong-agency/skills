---
name: mast
description: Apply No-Code Supply Co. Mast naming, structure, and class taxonomy to Webflow projects. Use this skill for the grammar—class names, base classes, utilities, custom-class conventions, and layout structure—when a project follows Mast. Pair with webflow-build for the implementation workflow (reuse ladder, native styling, QA gates).
---

# Mast Grammar

Use Mast as the shared grammar that keeps a Webflow site lean, reusable, and developer-efficient. This skill governs structure, naming, and framework taxonomy. Pair it with `webflow-build` for workflow, reuse, and completion gates.

Mast is a lightweight, component-first framework by No-Code Supply Co. It is intentionally minified: use base classes, utilities, and components for ~80% of layouts. The remaining ~20% is custom classes plus Designer-native styles—not custom CSS/JS embeds.

## When to apply

Use this grammar when the project follows Mast or a documented Mast-derived system (look for `page-wrapper`, `section` / `container` / `row` / `col`, `u-` utilities, `cc-` combos, and a Mast-style style guide).

Do not convert a site from Client-First, Lumos, or another established framework merely because Mast is available. Preserve the site's chosen system unless the user explicitly requests a migration. If the framework is unclear, inspect the style guide, existing classes, components, variables, and project instructions before creating anything.

## Authority order

When conventions differ, follow:

1. Explicit user direction for the current task.
2. Project instructions and documented site conventions.
3. Patterns already established in the actual site and style guide.
4. These Mast defaults (aligned to current Mast docs / style guide).
5. General Webflow or CSS convention.

**Surface a material conflict instead of silently mixing systems—especially Client-First `is-` modifiers or CF folder underscores with Mast `cc-` / `u-` patterns.**

## Mindset

- **80/20:** Default Mast classes and components cover common layouts. The remaining work is custom classes plus Designer-native styles—not utility stacks and not embed CSS.
- **DRY:** Reuse classes, variables, and components before inventing parallel ones.
- **Reduce cognitive load:** Prefer the same mental model for static builds and Build Mode (section → row → column → content).
- **Already styled:** Mast ships intentional defaults (heading bottom margins, column gaps, fluid type). Prefer adjusting variables and base classes over fighting defaults with one-off utilities on every instance.

## Core page structure

```text
page-wrapper
  Custom Code                         (existing global canvas CSS—do not dump into it)
  Navigation                          (global component)
  page-main                           <main>
    section
      container
        row
          col [+ responsive combos]
            [content / components]
  Footer                              (global component)
```

- Put `page-wrapper` around the whole page (theme / global color control).
- Put primary content in semantic `page-main` (`<main>`).
- Include the existing global Custom Code component on every page when the project uses it. Do not add layout or decoration CSS to it.
- For Build Mode-heavy pages, wrap main sections in a page slot so collaborators can reorder sections safely.

## Class taxonomy

### Base classes

Foundational layout and UI without a prefix. May take `cc-` combos and limited utilities:

```text
section
container
row
col
button
card
h1 ... h6
paragraph-xl / paragraph-lg / paragraph-sm
eyebrow
rich-text
```

### Utility classes

Prefix `u-`. Finite, single-purpose (or small helper) modifiers. Stack sparingly alongside base classes—not on custom classes that already own the styles:

```text
u-mb-sm
u-pt-0
u-text-center
u-d-none
u-bg-primary
u-mode-dark
u-img-cover
```

### Custom classes

Project-specific classes for unique components. Allowed sparingly. Put needed styles on the custom class itself rather than stacking utilities onto it. The custom class is **not** named `cc-foo` unless it is a combo.

Official Mast custom class examples from No-Code Supply Co. docs:

```text
blog_header-title
nav-logo_link
nav-menu_container
footer-social_list
```

The underscore separates **context levels** within a component or page scope. The hyphen connects words **within** a multi-word name. This is stock Mast grammar from official No-Code Supply Co. documentation—**not** Client-First BEM patterns or folder underscores.

### Combo classes

Prefix `cc-`. A **modifier** on a base or custom class only—never a stand-alone unique component name. Official Mast examples:

```text
section cc-home
section cc-footer
container cc-narrow
```

`cc-` is always a **variant** on something else (`section`, `container`, `card`, or a custom class). Do not name a new unique component `cc-hero`. Do not use Client-First `is-` (`is-secondary`, `is-dark`, ...).

## No Client-First grammar on Mast jobs

Do not mix Client-First names into a Mast project:

- no `is-` combos (`is-secondary`, `is-dark`, `is-featured`)
- no CF section pattern (`section_hero`, `section_feature-grid`)
- no `padding-global`, `main-wrapper`, or `container-large`

Use Mast `page-wrapper` / `page-main` / `section` / `container` / `row` / `col` only.

A Mast underscore (`blog_header-title`) is context, not a CF folder. A CF underscore (`section_hero`, `feature-grid_component`) is a different grammar—do not use it here.

## Naming grammar

Official Mast naming rules from No-Code Supply Co. documentation:

- Lowercase only; use CSS-safe characters so Designer names match live CSS.
- Hyphen `-` **within** a multi-word name or size/breakpoint token.
- Underscore `_` **between** context levels inside a component or page scope (`blog_header-title`, `nav-menu_container`). This is stock Mast naming, not Client-First BEM patterns or folder grammar.
- Purpose prefixes: `u-` utilities, `cc-` combo modifiers on base/custom classes, `styles__` for style-guide-only helpers.
- Breakpoint infixes on layout/utilities: `-lg-` desktop, `-md-` tablet, `-sm-` mobile landscape, `-xs-` mobile portrait (e.g. `col-lg-8`, `u-md-d-none`).
- Size postfixes use t-shirt sizing: `-sm`, `-md`, `-lg`, `-xl` (e.g. `paragraph-xl`, `u-mb-md`).

## Layout system (summary)

1. `section` — vertical padding for a page band; utilities like `u-pt-0` / `u-pb-0` trim rhythm when needed.
2. `container` — max-width + horizontal containment; optional `cc-` variants.
3. `row` + `col` — Flexbox 12-column grid. Start with `col`; add responsive width combos only where the span changes (`col-lg-8`, `col-md-12`, ...). Width cascades downward—do not repeat the same span at every breakpoint.
4. Row modifiers: alignment (`row-align-center`, ...), justification (`row-justify-between`, ...), gaps (`row-gap-md`, `row-gap-sm`, `row-gap-button`, `row-gap-0`).
5. Column modifiers: offsets, first/last reorder, `col-shrink`, `col-lg-contain-left` / `col-lg-contain-right`.

Collection lists can use `row` on the list and `col` on items.

See `references/layout-and-grid.md`.

## Class management

1. Avoid stacking more than about four utilities on one element.
2. Avoid more than one extra utility solely for a lower breakpoint when a custom class would be clearer.
3. Do not combine custom classes with utilities for styles the custom class should own—that accidental combo can poison global utility reuse.
4. Clear unused classes when finishing work. Preserve anything documented in the style guide "Prevent style clean up" / prevent-delete area used by custom code.

## Variables

Prefer Mast variable collections over hard-coded one-offs—and only for reusable system tokens, not as a backdoor for one element's Height or Width:

- **Theme** — base / invert (and project accent modes if kept); usually applied via `page-wrapper` and mode utilities/components.
- **Typography** — fluid type via min/max + `clamp()`.
- **Components** — section, container, cards, buttons, inputs, etc.
- **Layout** — grid gaps, margins, fluid layout values.
- **Color** — only brand colors actually used; group by primary / secondary / neutral as the brand requires.

Variable names in Webflow use Title Case + spaces for legibility. Update variables before restyling every instance of a component.

## Typography

- Semantic heading level and visual size are independent: set the HTML heading level for document outline, then apply `h1`...`h6` (or Heading component props) for visual size.
- Prefer existing paragraph size classes and `rich-text` / Rich Text component for body content.
- Trust default bottom margins in EM; do not neutralize them site-wide without a deliberate system decision.

## Components and Build Mode

- Prefer Mast components already in the project (Nav, Footer, Button, Form inputs, Accordion, Modal, Slider, Tabs, Image, Icon, Card, Table, Theme Toggle, Inline Video, Marquee, etc.) over rebuilding equivalents.
- Build Mode uses the same mental model via components: Section, Grid Row, Grid Col, Spacer, Border, plus content components (Rich Text, Heading, Button, Icon, ...).
- Respect component props, slots, and visibility flags for custom code groups (performance: hide unused component JS/CSS groups per page when the project supports it).
- For animations, prefer the project's `data-animate` attribute patterns and IX3/GSAP interactions already installed—target classes, not one-off elements.

See `references/components.md`.

## Custom code

- The existing Mast Global Canvas CSS component stays as-is. Do not add layout, sizing, or decoration CSS to it, to a new embed, or to page `<style>`.
- Custom code is only for behavior Webflow cannot express natively.
- Prefer attribute/ID targeting in JS over class targeting when possible.
- Never publish. Never invent private client secrets into the public skill repo. Host shared component JS as the project already does (CDN / embeds).

## Mast completion check

Before handing the work back:

- The project was confirmed to use Mast.
- Existing components, base classes, utilities, combos, variables, and modes were reused wherever suitable.
- Custom classes are few and justified; each was created with a clear responsibility; utilities were not stacked onto those custom classes.
- Combos are `cc-` on a base or custom class—not a unique class named `cc-hero`, and not Client-First `is-`.
- No Client-First names (`is-secondary`, `section_hero`, `padding-global`, `main-wrapper`, `container-large`).
- Naming uses `u-` / `cc-` / Mast underscore-context / hyphen-tokens correctly.
- Styles were set via native Style panel fields (see `webflow-build/references/native-styling.md`).
- Section → container → row → col structure (or Build Mode equivalents) is intact; Navigator remains readable.
- Responsive column spans only declare breakpoints that change.
- Unused classes that are safe to remove were considered; prevent-delete classes were left alone.

Use the broader completion gate in `webflow-build` for visual, responsive, interaction, component-instance, persisted-state, and publication-state QA.

## Supporting references

- `references/conventions.md` — naming, class types, combo vs custom, forbidden CF names
- `references/layout-and-grid.md` — page structure and 12-column system
- `references/components.md` — component inventory and Build Mode notes

## Canonical references

- https://www.nocodesupply.co/mast/docs
- https://www.nocodesupply.co/mast
- https://mast-framework.webflow.io/ (style guide v2.4+)
- https://mast-framework.webflow.io/styles
- https://mast-framework.webflow.io/components
