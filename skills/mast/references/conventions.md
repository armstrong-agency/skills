# Mast conventions

Use this grammar only when a project has chosen **Mast** (No-Code Supply Co.)
or a documented Mast-derived system. Preserve another established framework
rather than mixing naming systems.

The bundled `mast` skill is authoritative. This file is a compact reference
for shared implementation details. Prefer the live project style guide and the
canonical docs over memorized class lists.

Canonical docs: https://www.nocodesupply.co/mast/docs
Style guide: https://mast-framework.webflow.io/

## Class types

| Type | Prefix | Role |
| --- | --- | --- |
| Base | _(none)_ | Foundational layout/UI (`section`, `row`, `col`, `button`, ...) |
| Utility | `u-` | Finite modifiers; stack lightly |
| Custom | project name | Unique components; own their styles; **not** named `cc-...` |
| Combo | `cc-` | Variants on base or custom only |
| Style-guide only | `styles__` | Documentation helpers; not for production UI |

Rules of thumb:

- Utilities may sit beside base classes.
- Do **not** pair utilities with a custom class for styles that belong on the
  custom class (avoids accidental combo pollution of global utilities).
- Combos (`cc-`) attach to base or custom classes -- not to utilities.
- Cap utility stacks around four; prefer a custom class beyond that.
- Prefer at most one extra utility solely for a lower breakpoint.
- Custom classes are allowed sparingly. They are not forbidden.

## Combo vs custom

A **custom class** is a unique component or element class. Name it for the
thing, not as a combo. Put the styles on that class.

```text
blog_header-title
pricing_card-badge
```

A **combo** is a `cc-` variant attached to a base or custom class:

```text
container cc-narrow
section cc-footer
tabs-link cc-active
```

Do not name a new unique component `cc-hero`. Do not use Client-First `is-`.

The underscore in `blog_header-title` is Mast context (levels inside a
component or page). It is not Client-First folder grammar. Do not treat every
underscore as a CF class.

## Forbidden on Mast jobs

Do not use Client-First names or structure:

- `is-secondary`, `is-dark`, `is-featured`, or any `is-` combo
- `section_hero`, `section_feature-grid` (CF `section_[identifier]`)
- `padding-global`, `main-wrapper`, `container-large`

Use Mast `page-wrapper` / `page-main` / `section` / `container` / `row` /
`col` only.

## Native styles -- no embed loophole

Set Height, Width, Margin, Padding, Display, Position, and Background on the
class through Designer-native fields. Do not invent a one-off CSS custom
property for a value those fields already accept.

Do not add a Custom Code embed, page `<style>`, or Global Canvas CSS dump to
implement layout or decoration Designer or this skill would reject. The
existing Mast Global Canvas CSS component stays as-is.

See `webflow-designer` -> `references/native-styling.md`.

## Naming grammar

- Lowercase; CSS-safe characters so Designer matches published CSS.
- `-` within a multi-word token or size/breakpoint fragment.
- `_` between context levels inside a component/page (`blog_header-title`).
  That is Mast, not Client-First folders.
- Meaningful short names; abbreviate long words when clarity survives.

### Breakpoint infixes

Used in column spans, offsets, reorder, and some display utilities:

| Infix | Webflow breakpoint |
| --- | --- |
| `-lg-` | Desktop |
| `-md-` | Tablet |
| `-sm-` | Mobile landscape |
| `-xs-` | Mobile portrait |

Example: `col-lg-8`, `col-md-12`, `u-sm-d-none`.

Column width combos cascade downward -- only add a breakpoint where the span
changes.

### Size postfixes

T-shirt sizing keeps names stable across brands even when values differ:

`-sm`, `-md`, `-lg`, `-xl` (and project-specific extras like `-xs` when present
on the style guide).

Examples: `paragraph-xl`, `u-mb-md`, Icon size variants.

## Variables

Collections commonly used in Mast v2.x:

1. **Theme** -- background/text/border/accent across base, invert, optional
   accents; often driven from `page-wrapper` plus mode utilities / Theme Toggle.
2. **Typography** -- fonts and fluid heading/body/eyebrow sizes (min/max +
   clamp).
3. **Components** -- high-level section, container, card, button, input tokens.
4. **Layout** -- grid gaps, margins, fluid layout values, column count when
   present.
5. **Color** -- only swatches the project actually uses.

Webflow variable labels use Title Case + spaces for scanning; CSS custom
property names are derived by Webflow. Customize variables before restyling
every component instance by hand. Do not create a variable for a one-off
Height, Width, or similar native field.

## Typography notes

- Heading **element** (H1-H6) controls semantics; heading **class** / Heading
  component controls visual size.
- Default bottom margins on type are intentional (Already Styled). Prefer EM
  margins that scale with type size over per-breakpoint margin utilities.
- Use `rich-text` / Rich Text for most body content; Plain Text when CMS plain
  binding is the point.

## Color utilities

Color is applied as utilities (`u-bg-*`, `u-text-*`) and theme modes
(`u-mode-dark`, `u-mode-light`). Keep the palette minimal -- add brand colors
when they appear in UI, not every swatch from a brand PDF.

## Interactions and motion

- Prefer project `data-animate` attribute patterns (e.g. `stagger-children`)
  bound on Section / Row / Column / Content Wrap when available.
- Target classes in interactions for reuse; avoid element-only triggers.
- Respect `prefers-reduced-motion`. Avoid `transition: all`.

## Migration cautions

- Do not introduce Client-First `is-` modifiers or `section_name` /
  `padding-global` structure into a Mast site.
- Do not rename Mast `button` back to legacy `btn` unless the project still
  ships that older nomenclature.
- When pasting Mast into an existing non-Mast project, follow the official
  paste order and `old_` rename guidance in the Mast docs; Variables may not
  copy cleanly into older projects.
- Clear unused classes only after checking the prevent-delete / custom-code
  retention area on the Components style-guide page.
