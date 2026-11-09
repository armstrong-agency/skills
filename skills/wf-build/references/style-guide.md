# Set up a Style Guide

Use this when the site has no Style Guide. The Style Guide comes before the first section, because every later class and variable builds on it.

## 1. Start from the grammar

Open the style guide linked in the grammar file's Docs section and use its structure and page layout. On a site cloned from that starter, extend what is already there. With no grammar, ask the user which one to use.

## 2. Collect foundations

Take literal values from the source. State which source is authoritative for each value, and surface conflicts between sources.

- **Figma:** node data for styles, variables and measurements. Calibrate screenshots before trusting them.
- **Live site:** computed styles at desktop, tablet, mobile landscape and mobile portrait.

Collect only recurring foundations:

- **Color:** primitives plus semantic roles (text, background, border, link, focus, success, warning, error), with each role bound to a primitive.
- **Type:** families, weights, sizes, line height and recurring letter spacing, keeping heading level separate from visual size.
- **Space:** the smallest practical scale, gutters, section padding and containers.
- **Shape:** recurring radii, border widths and simple shadows.
- **Controls:** buttons, links and form fields, with hover, focus-visible, active, disabled, error and success states where the source shows them.
- **Responsive:** only values that change between breakpoints.

For a missing font, name the family, the fallback and the gap.

## 3. Propose

Show the foundations with their proposed variable and class names in the site's grammar, and flag gaps and conflicts. Stop until the user approves.

## 4. Create

Create the approved variables and classes in Webflow, then the Style Guide page with a specimen of each. Read them back to confirm they persisted.
