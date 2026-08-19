# Naming conventions — Client-First (Finsweet)

Use this grammar only when a project has chosen **Finsweet Client-First** or a
documented Client-First-derived system. Preserve another established framework
rather than mixing naming systems.

The bundled `client-first` skill is authoritative. This file is a compact
reference for shared implementation details.

## Class grammar

- **Custom classes:** `[folder]_[element]` with underscores — e.g. `hero_heading`, `feature-card_icon`, `footer_link-list`. The folder groups related classes in the Style panel.
- **Utility classes:** `[property]-[value]` with dashes — e.g. `text-size-large`, `padding-section-medium`, `margin-bottom-small`, `background-color-secondary`.
- **Combo / modifier classes:** `is-[modifier]` — e.g. `button is-secondary`, `section_header is-dark`. Max 3 combo levels; combo naming matches the base format.
- No abbreviations, correct spelling, descriptive purpose-based names (never value-based: `background-color-primary`, never `background-white`).

## Page structure — the six-layer hierarchy

```
page-wrapper
  main-wrapper
    section_[name]
      padding-global padding-section-[size]
        container-[size]
          [content]
```

Apply horizontal page padding and vertical section padding to the same wrapper.
The container sits inside that wrapper.

## Variables ⇄ tokens

Three tiers:

1. **Base primitives** — value-scale-named variable groups (`Neutral / …`, `Teal / …`) in the **same collection** as the semantic tokens: JSON `base.<scale>.<step>` → Variable **`Neutral / 900`** → CSS **`--neutral--900`**. Value-based naming is correct here and only here. Never apply a base variable to a style directly.
2. **Semantic tokens** — purpose-based names only; every color is an **alias** to a base variable (JSON `alias`, Webflow `existing_variable_id`).
3. **Component structure** — Client-First classes, not variables. The spacing system stays pure Client-First.

**Modes:** color tokens may carry `modes.dark` (a base ref). Deployed as a **Dark** variable mode on the semantic collection; applied Designer-natively per style/section (`set_style_variable_mode`) or site-wide — never via custom code. Non-color categories don't take modes.

- Token JSON key `category.name` → Webflow Variable **`Category / Name`** (Title Case, spaces) → CSS **`--category--name`**.
  - `/` becomes `--`, spaces become `-`, all lowercased. Example: `spacing.medium` → `Spacing / Medium` → `--spacing--medium`.
- This mapping is bidirectional and predictable; it's why Client-First was chosen over other frameworks (best machine-readability).
- **Shadow and atmosphere tokens** (e.g. `shadow.card` → `--shadow--card`, `atmosphere.overlay` → `--atmosphere--overlay`) can be defined in token systems but do **not** deploy as Webflow Variables (no shadow/image variable types) — they're applied as style values. Tokens at source, styles at destination.

## Structure classes (Client-First canonical)

`page-wrapper`, `main-wrapper`, `container-large` / `container-medium` / `container-small`, `padding-global`, `padding-section-small` / `-medium` / `-large`, `spacer-*`, `padding-*`, `margin-*`.

## Typography / buttons (utility)

- `heading-style-h1` … `h6`, `text-size-tiny/small/regular/medium/large`, `text-weight-*`, `text-color-*`, `text-align-*`.
- `button` base + `is-secondary` / `is-small` / `is-link` combos.

## Migration cautions

- Do not introduce `button-primary`-style variants into a project that uses
  Client-First's `button` plus `is-` combo pattern.
- Do not add temporary naming prefixes to finished class systems.
- Keep the Style Guide representative of the tags, components, and utilities
  the site actually uses.
