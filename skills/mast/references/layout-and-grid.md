# Mast layout and grid

Compact reference for page structure and the 12-column system. Verify class
names against the project style guide — sites may extend or trim the defaults.

Canonical docs: https://www.nocodesupply.co/mast/docs  
Styles (live examples): https://mast-framework.webflow.io/styles

## Page chrome

| Piece | Role |
| --- | --- |
| `page-wrapper` | Outermost wrap; global theme / background / text |
| Custom Code | Global canvas CSS + shared embeds; top of Navigator |
| Navigation | Global nav component (often sticky) |
| `page-main` | Semantic `<main>` for primary content |
| Footer | Global footer after main |

Build Mode pages often place a page slot inside `page-main` so collaborators
can reorder Section components.

## Section → container → grid

```text
section
  container
    row [+ align/justify/gap modifiers]
      col [+ span/offset/reorder/shrink/contain]
        …
```

- **`section`** — vertical band padding (fluid in recent Mast versions). Trim
  with `u-pt-0` / `u-pb-0` when stacking sections visually.
- **`container`** — centered max-width + gutters. Optional combos such as
  `cc-narrow` or nav-specific combos when the project defines them.
- **`row`** — flex parent for columns.
- **`col`** — padded column; equal width by default; collapses on the smallest
  breakpoint unless spans are set.

## Responsive column spans

Base: `col`  
Spans: `col-{bp}-{1-12}` for `lg` / `md` / `sm` / `xs`.

Only declare breakpoints where the width changes. Totals over 12 wrap to a new
line.

Webflow's class typeahead may only suggest the first responsive combo; typed
additional combos still apply when spelled correctly.

## Row modifiers

**Align (vertical):** `row-align-center`, `row-align-end`,
`row-content-center`, `row-content-end`, `row-content-between`

**Justify (horizontal):** `row-justify-center`, `row-justify-end`,
`row-justify-around`, `row-justify-between`

**Gap:** `row-gap-md`, `row-gap-sm`, `row-gap-button`, `row-gap-0`  
(Values come from Layout / Grid gap variables.)

Older projects may still show `row-gutterless`; prefer the gap variables/classes
present in the active style guide.

## Column modifiers

- **Offset:** `col-{bp}-offset-{0-6}` (confirm available offsets in the guide)
- **Reorder:** `col-{bp}-first`, `col-{bp}-last`
- **Shrink:** `col-shrink`
- **Bleed to viewport while opposite side stays contained:**
  `col-lg-contain-left`, `col-lg-contain-right`

## CMS / native lists

Apply `row` to a Collection List (or similar parent) and `col` to each item so
CMS grids share the same system as static layouts.

## Utilities commonly paired with layout

- Spacing: `u-mt-*`, `u-mb-*`, `u-pt-0`, `u-pb-0`, `u-m-0`, `u-mlr-auto`
- Display: `u-d-none`, `u-d-block`, `u-d-flex`, `u-d-inline-flex`,
  `u-d-contents`, plus `u-{md,sm,xs}-d-none` / `d-block`
- Position / overflow: `u-position-relative`, `u-position-sticky`,
  `u-overflow-hidden`
- Helpers: `u-img-cover`, `u-link-cover`, `u-aspect-1x1` / `16x9` / `4x3`,
  `u-sr-only`, `u-border`, `u-z-index-1`

When utility stacks grow past ~4 classes, switch to a custom class (Designer
role) instead of deepening the stack.
