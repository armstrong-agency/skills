# Lumos

Naming and structure for sites that follow Timothy Ricks' Lumos v2. Sizes are in **rem**, and layouts respond through variables and container queries instead of breakpoints.

## Structure

```text
[name]_wrap u-section                  <section>
  [name]_contain u-container
    [name]_layout
      [name]_content u-margin-trim
```

- `u-section` carries the theme background, text color and section padding. The first section on a page uses the page-top section space to clear the nav.
- `u-container` sets max width and site margin, and is the query container. Put grid and flex layout on the child `_layout`, and leave the container's own layout alone.

## Classes

**Component:** `[component]_[type]_[element]`, broadest part first, as in `card_testimonial_title`. Underscores separate parts, hyphens join words inside one part, and a name holds at most three underscores. Prefer `_title`, `_text` and `_img`. `_wrap` marks the root of a component or subcomponent, and any element whose children carry component classes ends in `_wrap`. Deeper nesting starts a new subcomponent name.

**Utility:** `u-` prefix, applied after the component class: `hero_title u-text-style-h2`. Every element carries a component class, so a utility always has one beside it.

**Combo:** `is-` on a component class, as in `hero_card_wrap is-reversed`. `is-active` is the state class scripts toggle. Webflow removes unused classes, so a styled combo that only a script applies needs a placeholder element inside a `[component]_hidden u-display-none` Div.

## Typography

`u-text-style-display`, `u-text-style-h1`…`h6` and `u-text-style-large|main|small`. The heading element sets the document level and the utility sets the look.

The parent of a run of text carries `u-margin-trim`, and `u-alignment-center` on that parent centers it. Text that needs a max width sits in a Div with `u-heading` or `u-text`.

Buttons have no utility. Style each on its component class, inside a Div with `u-button-wrapper`.

## Variables

- **Theme:** `u-theme-light`, `u-theme-dark` or `u-theme-brand` on a section or card switches every theme variable: background, text, border, link, primary button and secondary button. Every color binds to a theme variable, and buttons bind to the button variables.
- **Spacing:** space steps 1 to 8, with 3 and up for text. Section space is `none`, `small`, `main`, `large` or `page-top`.
- **Size:** max width `small`, `main` or `full`, site margin and gutter, radius `small`, `main` or `round`, and one main border width.
- **Typography:** font weights and letter spacing come from the typography variables.

## Responsive

Responsive variables switch display, direction, alignment and position by container width, so most components need no breakpoint styles. Use a container query against `u-container`, sized in em, only for a change the variables cannot express.

## Trigger and state

`data-trigger` (hover, focus) and `data-state` (current, open, expanded, checked) on a parent flip the trigger and state variables. Children read those variables for their hover and active styles.

## Custom CSS

Component CSS goes in an embed as the first child of the component's `_wrap`, and its script as the last child. Selectors are single classes.

## Docs

- [Docs](https://lumos.timothyricks.com/)
- [Cloneable starter and style guide](https://webflow.com/made-in-webflow/website/lumos-v2-beta)
- [Lumos skill](https://github.com/lumosframework/skill)
