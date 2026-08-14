# Native Webflow styling

Hard rules for **any** Webflow job -- Client-First, Mast, or another
documented system. Pair this file with the active framework skill
(`client-first` or `mast`). Never mix those grammars.

## Native Style panel first

Set presentation with Designer-native style fields, or MCP style properties
that map to them:

- height, width, max-width
- margin, padding
- display, flex, and grid as Webflow exposes them
- position
- object-fit
- background color, image, and gradients Designer supports
- typography fields
- borders, radius, and shadows Designer supports
- overflow, z-index, opacity

Prefer longhand native properties so a shorthand write does not clobber
siblings (for example, set `margin-top` rather than `margin` when only the
top value should change).

## Variables are tokens, not a backdoor

Do not create a Webflow variable (CSS custom property) for a one-off value
the native field already accepts. Example: do not make `--card-height` to
set one card's height; set Height on the class.

Variables are for reusable system tokens -- type scale, brand color, shared
radius -- not a styling escape hatch.

## No unsupported CSS, no embed loophole

If Webflow has no control for a CSS feature (repeating-radial-gradient,
arbitrary extra background layers, unsupported functions), do not fake it
with an embed or `<style>` block. Approximate with supported tools (image,
simple gradient, extra element) or tell the user it is not available
natively.

Custom Code, embeds, page `<style>`, and Global Canvas CSS are not a
loophole around framework or Designer rules. Do not add CSS there to
implement layout, sizing, or decoration the skill forbids in the Style
panel.

Custom code is only for behavior Webflow cannot express -- never for
ordinary presentation.
