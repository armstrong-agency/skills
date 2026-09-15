---
name: wf-design-system
description: Catalog design tokens from a public URL, Figma, or existing Webflow site into a markdown file (default DESIGN.md) — colors, fonts, type, spacing, radii, buttons, forms, and control states. Use when the user asks for a style guide, tokens, type scale, or design system. Pair with a grammar skill for naming. Write the markdown catalog only; do not write to Webflow or publish. Use wf-audit to check whether a Style Guide or naming convention already exists.
---

# Webflow Design System

Catalog the foundational system into `DESIGN.md` at the project workspace root, unless the user names another file. That file is a catalog for humans and later `wf-build` work. It is not a write to Webflow.

Do not write to Webflow. Do not publish. Do not build pages.

Use `wf-audit` to check whether a Style Guide or naming convention already exists.

## Grammar first

Do this before proposing token or class names in the catalog:

1. Inspect the source Style Guide, existing classes, or project instructions.
2. Name the convention: Client-First, Mast, mixed, or none.
3. If a matching `grammar/*` skill is installed, **read that skill now**. This skill records values and roles; grammar records how they would appear as classes.
4. If the convention is unclear, say so in Notes. Do not pick a grammar because it is installed.

## Sources

The user names one or more. State which source is authoritative for each claim. If they conflict, surface it; do not silently mix. Do not copy content, CMS, images, logos, components, or interactions.

**Public URL.** Normalize, follow redirects, respect `robots.txt`. Prefer a sitemap. Render unique static pages plus one representative per template (cap 20 pages; without a sitemap, depth 2 and at most 100 URLs). Computed styles at desktop, tablet, mobile landscape, and mobile portrait are the evidence of record. Do not authenticate or bypass bot protection.

**Figma.** Resolve file, node, and viewport. Node data can prove structure, text styles, variables, and measurements. A screenshot proves that capture only. Calibrate screenshot scale; do not treat a raster as CSS pixels until anchors agree.

**Existing Webflow.** Inspect the Style Guide, variables, modes, tags, and foundation classes. Prefer existing names. Record names and IDs in the catalog only — a connected site does not authorize writes.

## What to catalog

Style Guide foundations only:

- Color: primitives plus semantic roles (text, background, border, link, focus, success, warning, error). Bind roles to primitives. Do not invent extra themes.
- Type: families, weights, sizes, line height, recurring letter spacing. Keep semantic heading level separate from visual size. Use literal source values; do not invent a scale.
- Space: smallest practical scale, gutters, section padding, containers, truly global gaps. One-offs stay off the token list.
- Shape: recurring radii, border widths, simple shadows.
- Controls: buttons, links, form fields, and hover / focus-visible / active / disabled / error / success when evidenced.
- Responsive: only values that actually change.

Do not catalog cards, nav, footer, accordions, tabs, page sections, CMS, assets, or interactions. Preserve observed values. Note contrast or focus problems as optional recommendations. Missing fonts: name the family, the fallback, and the gap.

## File

Show a short preview (sources, counts, gaps). If `DESIGN.md` exists, wait before overwriting. Then write one file:

```markdown
# Design tokens

Source:
Date:
Grammar to pair: [client-first | mast | unspecified]

## Color
### Primitives
### Semantic roles

## Typography
## Spacing and layout
## Shape
## Controls
## Responsive
## Notes
```

Use exact observed values (hex, rem/px, family names). Unresolved items go in Notes, not as fake tokens.

## Handoff

```text
Wrote: [path or not written]
Grammar: [client-first | mast | unspecified]
Sources:
Counts: colors / type / space / controls
Gaps:
Conflicts between sources:
```
