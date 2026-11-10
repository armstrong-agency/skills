# Mast

Naming and structure for sites that follow No-Code Supply Co. Mast (v2.4-era style guide).

Every class follows Mast. A Mast underscore (`blog_header-title`) marks context, not a folder.

## Structure

```text
page-wrapper
  Custom Code                         (existing global canvas CSS — leave it)
  Navigation
  page-main                           <main>
    section
      container
        row
          col [+ span / modifiers]
            [content / components]
  Footer
```

`page-wrapper` is theme / global color. `section` is the vertical band, `container` max-width + gutters, `row` the flex parent, `col` the padded column.

Build Mode uses Section / Grid Row / Grid Col in slots the same way. Prefer the components actually installed on **this** site.

## Classes

**Base** — no prefix: `section`, `container`, `row`, `col`, `button`, `card`, `h1`…`h6`, `paragraph-xl` / `paragraph-lg` / `paragraph-sm`, `eyebrow`, `rich-text`.

**Utility** — `u-` prefix, one job: `u-mb-sm`, `u-pt-0`, `u-text-center`, `u-d-none`, `u-bg-primary`, `u-mode-dark`, `u-img-cover`. Cap stacks around four. After that, a custom class.

**Custom** — spare. Underscore between context levels, hyphen within a name: `blog_header-title`, `nav-logo_link`. Not `cc-foo` unless it's a combo.

**Combo** — `cc-` on a base or custom class: `section cc-home`, `container cc-narrow`. Not a standalone `cc-hero`. Not on a utility.

`styles__` classes are style-guide only.

## Grid

Spans: `col-{bp}-{1-12}` for `lg` (desktop), `md` (tablet), `sm` (mobile landscape), `xs` (mobile portrait). Only name a breakpoint where the width changes. Totals over 12 wrap.

Row: `row-align-center` / `row-align-end`, `row-justify-center` / `between` / `around`, `row-gap-md` / `sm` / `0`.

Column: `col-{bp}-offset-{0-6}`, `col-{bp}-first` / `last`, `col-shrink`, `col-lg-contain-left` / `right`.

CMS: `row` on the Collection List, `col` on each item.

## Variables

Theme, Typography, Components, Layout, Color — customize variables before restyling every instance. Color via `u-bg-*` / `u-text-*` and `u-mode-dark` / `u-mode-light`. The heading element sets the document level and the heading class sets the look. Prefer `rich-text` for body. Prefer EM type margins.

## Components (confirm they exist on this site)

Button, Form (`input-group`, `input`), Accordion, Modal (trigger is the next sibling), Slider, Inline Video, Marquee, Tabs (`cc-active` default). Content: Eyebrow, Heading, Rich Text, Card, Image, Content Wrap. Global: Nav, Footer, Theme Toggle, Custom Code (visibility props per page).

Build Mode kit: Section, Grid Row, Grid Col, Spacer, Border.

## Docs

- [Style guide](https://mast-framework.webflow.io/)
- [Cloneable starter](https://webflow.com/made-in-webflow/website/mast-framework)
- [Docs](https://www.nocodesupply.co/mast/docs)
