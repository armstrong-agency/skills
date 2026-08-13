# Mast components and Build Mode

Inventory-oriented notes for agents. Always prefer the components and props
actually installed in the current Webflow project; names and props evolve
across Mast versions (this skill targets the Mast 2.4-era style guide).

Canonical docs: https://www.nocodesupply.co/mast/docs  
Components guide: https://mast-framework.webflow.io/components

## Working modes

| Mode | Prefer |
| --- | --- |
| Design / static | Base classes + utilities + custom classes; components where they already exist |
| Build Mode | Section, Grid Row, Grid Col, Spacer, Border + content components in slots |

Build Mode intentionally mirrors static structure so clients and collaborators
can assemble pages without inventing a second layout language.

## Interactive (common)

- **Button** — primary/secondary, optional icons (`btn-text`, `btn-icon` innards);
  base `button` class also used on submits / modal triggers.
- **Form** — `form`, `input-group`, `input-label`, `input`, radio/check variants,
  `cc-light` / `cc-select` / `cc-textarea` / `cc-toggle` combos as present.
- **Accordion** — details/summary based; group name association; optional GSAP
  open/close from project custom code.
- **Modal** — native dialog patterns; trigger should be the immediate next
  sibling of the modal per Mast JS expectations.
- **Slider** — Swiper-based; slides-per-breakpoint and gap props; CMS path wraps
  a collection list of Slider Slide into the Slider slot.
- **Inline Video** — lazy/poster/play-on-view/hover/desktop-only props.
- **Marquee** — CSS loop; duplicate identical groups in each marquee slot.
- **Tabs** — Tabs + Tabs Menu + Tabs Link + Tabs Pane (+ optional Play/Pause);
  `cc-active` for default tab; hash IDs for deep links.

## Content

- **Eyebrow**, **Heading** (semantic tag vs visual size), **Rich Text**,
  **Plain Text**, **Breadcrumb**, **Icon** (Phosphor or swapped CSS icon set),
  **Image** (aspect / fit), **Card** + Card Body, **Table**, **Content Wrap**
  (alignment, list role, id, `data-animate`).

## Global

- **Nav** / **Nav Banner** / **Footer** — start from the cloneable; restyle via
  variables and project classes.
- **Theme Toggle** — depends on Theme variables + Custom Code theme CSS/JS;
  disable by hiding that embed group and simplifying Theme variables.
- **Custom Code** — single source for global CSS/JS and per-component script
  groups; use visibility props so unused libraries stay off a page. Canvas QA
  props (when present) highlight missing custom code for placed components.

## Build Mode kit

- **Section** — themed section + container + slot
- **Grid Row** / **Grid Col** — same 12-column idea as class-based grid
- **Spacer** / **Border** — rhythm helpers for non-dev editors
- Mix in Button, Icon, Rich Text, Heading, Accordion, etc.

## Agent checklist when using a component

1. Confirm the component exists in **this** project (not only in upstream Mast).
2. Prefer props/slots/variants over detaching or restyling internals ad hoc.
3. Ensure required Custom Code group visibility is on for that page.
4. Keep accessibility affordances (labels, dialog/summary structure, skip link).
5. Do not publish; leave publication-state checks to the designer QA skill.
