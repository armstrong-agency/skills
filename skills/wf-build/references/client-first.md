# Client-First

Naming and structure for sites that follow Finsweet Client-First v3, which is built around Webflow Variables. Sizes are in **rem**; prefer rem over px for layout and type.

## Version

A v3 site has the Base, Theme, Typography, Layout and Sizes variable collections, section padding bound to variables on the section class, and one-class spacing (`padding-bottom-medium`). A v2 site has a `padding-global` layer in every section, two-class spacing (`padding-bottom` + `padding-medium`) and `spacer-*` classes. Build in the version the site uses, and tell the user when a site mixes them.

## Structure

```text
page-wrapper
  main-wrapper                         <main>
    section_[identifier]               <section>, the native Section element
      container-[size]
        [section content]
```

- `page-wrapper` is the outermost wrap for page content. Style it lightly, and keep `body` styles to typography and background color.
- `main-wrapper` holds the primary content with the `<main>` tag. Nav and footer sit outside it.
- `section_[identifier]` is one section band. Its left and right padding bind to the global padding variable, and its top and bottom padding bind to variables in the Section Padding group. For uneven spacing, bind top and bottom to different variables. When one section needs unique padding, set it on that section's class.
- `container-[size]` (`large` | `medium` | `small`) sets content max-width. Keep padding off it so padding and max-width work independently. Use `max-width-*` for narrower content inside it.
- The component root is `[folder]_component`.

The layered structure stays valid when a section needs more control: a Div carrying `padding-global` and `padding-section-[size]` (or `padding-section-[top|bottom]-[size]`) as two utility classes, between the section and its container. Use these classes only on that layer, never as combos on the section class, and use `padding-global` for page gutters only, not for spacing content items.

For a full-height hero, keep the section padding and set the height (for example `min-height: 100vh`) on a wrapper inside the section, so content never touches the top or bottom edge on short screens.

Each wrapper needs a job (layout, size, position, overflow, group), so skip empty ones. Prefer nested layers, or one meaningful class, over stacking many unrelated utilities on one element.

## Spacing

Spacing values live in the Layout collection and change per breakpoint through variable modes, so a spacing class needs no breakpoint override. Edit responsive values in the Variables panel.

One class carries direction and size:

- `padding-[size]` / `margin-[size]` for all sides.
- `padding-[direction]-[size]` / `margin-[direction]-[size]`, with direction `top`, `bottom`, `left`, `right`, `horizontal` or `vertical`.
- `gap-[size]` on flex and grid parents.
- `spacing-clean` removes spacing.

Sizes, smallest to largest: `0`, `xxtiny`, `xtiny`, `tiny`, `xxsmall`, `xsmall`, `small`, `medium`, `large`, `xlarge`, `xxlarge`, `huge`, `xhuge`, `xxhuge`. Padding, margin and gap share one scale; section padding has its own.

Choose by job:

- **Spacing block:** an empty Div with `padding-[direction]-[size]` between two siblings. It adds the fewest levels, so prefer it for simple spacing.
- **Spacing wrapper:** a Div with `margin-[direction]-[size]` around a child.
- **Gap:** evenly spaced children, such as link lists, card internals and button rows.
- **Custom class:** recurring elements that share one value, breakpoint-specific sizes and one-offs, bound to a Layout variable where one exists.

Keep spacing classes off headings and paragraphs; space them with a block or wrapper. Size inner elements with a custom class rather than utility padding. Follow the spacing pattern the project's existing pages use, and with no precedent, ask the user.

## Classes

**Custom:** underscore `_` between folder and element, which also creates a virtual folder in Finsweet's Folders. Hyphens inside a name. Name the role.

```text
feature-grid_component
feature-grid_item
feature-grid_image-wrapper
section_feature-grid
```

**Utility:** no underscore. Global CSS behaviors reused across the site, drawing their values from variables.

**Global:** any class meant to stay unified site-wide. Utilities are always global; a custom class is global when the same pattern recurs everywhere, such as a shared `header_content`.

**Combo:** two strategies, both valid.

- **Custom + utility:** apply the custom class first, then a utility on top (`feature-grid_list grid-autofit`). This changes the instance without editing the utility.
- **`is-` combo** on a base class: `button is-secondary`, `feature-grid_item is-featured`. The `is-` class works only with its base.

Prefer utilities for shared CSS properties and custom classes for specific components or elements.

**Utility systems** (when the cloneable has them):

- **Typography:** `heading-style-h1`…`h6`, `text-size-large|medium|regular|small|tiny`, `text-weight-xbold|bold|semibold|medium|normal|light`, `text-align-left|center|right`, `text-color-primary|secondary|alternate`.
- **Text style:** `text-style-allcaps`, `-italic`, `-link`, `-muted`, `-nowrap`, `-quote`, `-strikethrough`, `-balance`, `-pretty`, `-1line`, `-2lines`, `-3lines`.
- **Inherit:** `text-color-inherit`, `text-size-inherit`, `text-weight-inherit`, `text-decoration-inherit`, `border-radius-inherit`.
- **Grid:** `grid-autofit` / `grid-autofit-[size]` stretch items to fill the row; `grid-autofill-[size]` keeps empty columns so items hold their size. `grid-span-full` spans every column. These are responsive without breakpoint overrides.
- **Layout:** `max-width-*` (with `max-width-full` per-breakpoint variants), `hide`, `hide-tablet`, `hide-mobile-landscape`, `hide-mobile-portrait`, `display-inline`, `display-inline-flex`, `display-contents`.
- **Color:** `background-color-primary|secondary|tertiary|alternate`.
- **Misc:** `overflow-hidden|scroll|auto|clip|visible`, `z-index-1|2`, `pointer-events-none|auto`, `aspect-ratio-square|portrait|landscape|widescreen`, `icon-height-*`, `icon-1x1-*`, `disable-select`, `text-area-vertical`.
- **Button:** `button`, `button is-secondary`, `button is-text`.

v3 removed `layer` and no longer recommends `spacer-*`.

## Typography

Style the HTML tags (`body`, `p`, `h1`–`h6`) as the defaults, and leave most headings and text with no class. Add a `heading-style-*` or `text-*` utility only where an instance differs from the default. The heading **element** is the document level; the heading **class** is the look. Text that needs heading styles without being a heading is a Text Block with a custom class.

Typography values live in the Typography collection, with modes for Desktop, Tablet and Mobile Landscape: font size, weight, line height and letter spacing, plus heading margins such as `h2-bottom-margin` when the project has a consistent heading system.

## Variables

Five collections:

| Collection | Holds |
| --- | --- |
| Base | Primitives: raw values, mostly colors and some font values |
| Theme | Semantic colors, in groups such as Background, Border, Text and Link |
| Typography | Semantic type, with responsive modes |
| Layout | Spacing, Section Padding, Max Width and Container, with responsive modes |
| Sizes | Element sizing |

**Naming:**

- Groups are sentence case (`Background`, `Text`); variables are lowercase and hyphenated (`primary`, `secondary`).
- Primitives are named by value (`blue-600`, `red-100`).
- Semantic variables are named by purpose, with the group carrying the context: Background › `primary`, Text › `secondary`. Leave the group name out of the variable (`primary`, not `background-primary`), except where the Style panel needs context, such as `h2-font-size`.
- Name semantics by role, never by color, so they hold across light and dark modes.

**Binding:** semantic variables point at primitives, and styles bind to semantics: backgrounds to Background, text to Text, borders to Border, padding and gaps to Layout spacing. Bind a primitive directly only when it is used once. Prefer a utility class; a custom class bound to the same variable is the second choice.

Every color uses a variable, with one exception: alpha values of pure black or white (for example `rgba(0, 0, 0, 0.4)`) used as an overlay, gradient, scrim or shadow may stay raw. Any opaque or tinted color binds to a semantic variable.

**Modes:** light and dark themes are modes on the Theme collection, switched in the Style panel or with a `theme-dark` / `theme-light` class. Breakpoint modes on Typography and Layout carry responsive values.

## Components

Name components `Group Name / Component Identifier`. The slash does not create the group, so create the group in the Components panel and match the name to it. The v3 page template ships `Global / Styles` (global styles), `Template / Section` and `Template / Core Structure` (unlink to start a section or page).

Custom CSS goes in a native embed inside `Global / Styles`, never in Site or Page Settings. Finsweet's defaults and project CSS sit in separate embeds, so add project CSS to its own embed and leave the defaults unchanged.

## Interactions

Name interactions `Element [Action State]`, with State only when it adds context: `Sort Button Arrow [Rotate Open]`. Keep names short enough to fit Designer's Interactions panel.

## Docs

- [Style guide](https://client-first.webflow.io/)
- [Cloneable starter](https://webflow.com/made-in-webflow/website/client-first-cloneable)
- [Intro](https://finsweet.com/client-first/docs/intro)
- [What's new in v3](https://finsweet.com/client-first/docs/whats-new)
- [Core structure](https://finsweet.com/client-first/docs/core-structure-strategy)
- [Variables](https://finsweet.com/client-first/docs/variables)
- [Spacing](https://finsweet.com/client-first/docs/spacing-strategy)
- [Utility class systems](https://finsweet.com/client-first/docs/utility-class-systems)
- [Typography](https://finsweet.com/client-first/docs/typography-strategy)
- [Classes strategy 1](https://finsweet.com/client-first/docs/classes-strategy-1)
- [Classes strategy 2](https://finsweet.com/client-first/docs/classes-strategy-2)
- [Folders](https://finsweet.com/client-first/docs/folders)
- [Component naming](https://finsweet.com/client-first/docs/component-naming)
- [Interactions naming](https://finsweet.com/client-first/docs/interactions-naming)
- [Sizes and rem](https://finsweet.com/client-first/docs/sizes-and-rem)
- [Global styles embed](https://finsweet.com/client-first/docs/global-styles-embed)
- [Client-First for AI](https://finsweet.com/client-first/docs/client-first-skill)
- [Launch checklist](https://finsweet.notion.site/client-first-launch-checklist)
- [Changelog](https://finsweet.com/client-first/docs/changelog)
