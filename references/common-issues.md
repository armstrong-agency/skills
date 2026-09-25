# Common issues (Webflow MCP)

Operational quirks for `wf-audit` / `wf-plan` / `wf-prototype` / `wf-build`. Not naming rules — those live in `framework-grammar/`.

Keep this file short. Add a bullet only after it burned real time on a job. No client names, site IDs, or project patterns.

## Classes and combos

- Two combos with the same name on different bases (e.g. `is-secondary` on `button` and on something else) can attach to the wrong class. After creating a combo, read the element's classes back.
- Applying two utilities as one MCP style write (e.g. `padding-global` + `padding-section-*` in a single empty dual combo) can create a useless empty class. Prefer two style names on the element, or create/apply each utility the way the Designer would.
- Underscore = virtual folder for custom classes. Don't invent deep stacks of wrappers that only exist to hold a name.



## Elements and nesting

- **Text Link** (`Link`) generally cannot nest Div / HtmlEmbed children. For a clickable row that needs an icon, chevron, or other nested block: use a **Link Block**, or put the icon as a **sibling** and style/position it.
- Put text on headings, paragraphs, and text links. A generic Div is not for text content.
- Images, icons, and embeds sit beside text — not inside headings or paragraphs as spans.
- Don't unlink a component to work around a failed insert. Insert into a parent, then reorder.



## Attributes and props

- Binding custom attributes (`data-*`, etc.) to component string/id props via MCP often fails or is rejected. Prefer runtime JS to stamp attrs, or bind in the Designer UI when the API won't.
- Page links set at create time can save as `#`. Set the link, then read it back.
- Don't create a Webflow variable for a one-off height or width. Variables are shared tokens.



## Variables

- Variable aliases stay in the same collection. Cross-collection aliases fail.
- Creating a collection is usually a one-way door — keep primitives and semantics together unless the project already splits them.



## Designer / MCP session

- Saved draft, Designer canvas, Preview, and the published staging/live site can disagree. Ask the user to refresh the canvas, or get permission before publishing to staging.
- Designer MCP needs an active Designer tab with the MCP app running. If tools time out or say they can't connect, stop and ask the user to reopen Designer — don't invent a workaround that scrapes the published site as if it were the canvas.
- When editing a **component definition**, the canvas may report a different `pageId` than the host page you opened from. Use the `pageId` returned by select/get-current for writes inside that component view; pass `scope_component_id` when tools require it.
- Large nested creates get truncated. Several medium writes beat one giant one.
- Discover Webflow MCP tool names in-session. Don't hardcode names from memory or old docs.
- Webflow native Tab elements sometimes have issues adding new tabs. Either add a fresh tab item and restyle + add content, or ask the user for help; do not duplicate an exisiting tab item.
- Use only CSS properties that map to Designer controls. Modern `column-gap` / `row-gap` won't display in Designer's Gap field; use `grid-column-gap` / `grid-row-gap` instead. If a property doesn't appear in the Style panel after writing it, switch to the property name Designer expects.



## Breakpoints and state

- Style changes on `main` cascade; overrides on `medium` / `small` / `tiny` only where needed. Confirm the breakpoint you intended after an update.
- Open/active UI state that JS toggles (`is-active`, etc.) must match the class the script actually sets. If the script targets a child and the markup puts the icon as a sibling (or the reverse), rotate/open styles won't fire — align markup and script, or use a selector that matches the real DOM.



## Publishing

- Never publish production unless the user explicitly asks. Prefer draft.
- Stage publish is still a real publish to a staging domain. Confirm with the user at the beginning of the workstream if publishes to staging are allowed. Changes save automatically in Webflow so no need to say "Saved." 



## Retries, tree dumps and hung commands inflate agent runs

Symptom: a run spends many calls on validation-error retries, whole element or style trees come back into context, or a render command hangs until the harness timeout.
Fix: read the tool's input schema before the first call and record the working shape. Read by ID or name, scoped to the section root. Put a timeout on every render or terminal command. See wf-build/references/agent-runs.md.



## Criteria to add to this file

1. A mistake cost real time on a real job.
2. It's about platform/MCP/Designer behavior, not one client's design system.
3. One short bullet; link to official docs when they exist instead of pasting long excerpts.

