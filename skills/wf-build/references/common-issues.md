# Common issues (Webflow MCP)

Known Webflow MCP and Designer behavior that costs time if you don't expect it.

## Classes and combos

- Two combos with the same name on different bases can attach to the wrong class. After creating a combo, read the element's classes back.
- Applying two utilities as one MCP style write can create a useless empty class. Prefer two style names on the element, or create/apply each utility the way the Designer would.
- Webflow's visible class list and its native selector-chain metadata are separate facts: a readback of several class names does not prove the intended chain. Create and repair stacks through a Webflow-native path, verify the expanded selector list in Designer, and confirm the persisted records.

## Elements and nesting

- **Text Link** (`Link`) generally cannot nest Div / HtmlEmbed children. For a clickable row that needs an icon, chevron, or other nested block: use a **Link Block**, or put the icon as a **sibling** and style/position it.
- Put text on headings, paragraphs, and text links. A generic Div is not for text content.
- Don't unlink a component to work around a failed insert. Insert into a parent, then reorder.
- The MCP can't create a native **Navbar** (`w-nav`), even with the Designer bridge open. Dropdown, Tabs, and Slider work. Navbar markup sent as HTML lands as plain Divs and Links with the `w-` classes dropped, so there is no collapse or menu button. Don't fake it with an always-open menu: ask the user to add a Navbar in Designer, then build inside it.

## Attributes and props

- Binding custom attributes (`data-*`, etc.) to component string/id props via MCP often fails or is rejected. Prefer runtime JS to stamp attrs, or bind in the Designer UI when the API won't.
- Page links set at create time can save as `#`. Set the link, then read it back.

## Variables

- Variable aliases stay in the same collection. Cross-collection aliases fail.
- Creating a collection is usually a one-way door — keep primitives and semantics together unless the project already splits them.

## Designer / MCP session

- Saved draft, Designer canvas, Preview, and the published staging/live site can disagree. Ask the user to refresh the canvas, or get permission before publishing to staging.
- Designer MCP needs an active Designer tab with the MCP app running. If tools time out or say they can't connect, stop and ask the user to reopen Designer — don't invent a workaround that scrapes the published site as if it were the canvas.
- When editing a **component definition**, the canvas may report a different `pageId` than the host page you opened from. Use the `pageId` returned by select/get-current for writes inside that component view; pass `scope_component_id` when tools require it.
- Large nested creates get truncated. Several medium writes beat one giant one.
- Webflow native Tab elements sometimes have issues adding new tabs. Either add a fresh tab item and restyle + add content, or ask the user for help; do not duplicate an existing tab item.
- Use only CSS properties that map to Designer controls. Modern `column-gap` / `row-gap` won't display in Designer's Gap field; use `grid-column-gap` / `grid-row-gap` instead. If a property doesn't appear in the Style panel after writing it, switch to the property name Designer expects.

## Breakpoints and state

- Style changes on `main` cascade; overrides on `medium` / `small` / `tiny` only where needed. Confirm the breakpoint you intended after an update.
- Open/active UI state that JS toggles must match the class the script actually sets. If the script targets a child and the markup puts the icon as a sibling (or the reverse), rotate/open styles won't fire — align markup and script, or use a selector that matches the real DOM.

## Publishing

- Stage publish is still a real publish to a staging domain. Confirm with the user at the beginning of the workstream if publishes to staging are allowed. Webflow saves changes automatically; don't report "saved" as if it were a step.

## Keeping runs small

- Read a tool's input schema before the first call and reuse the shape that worked. If a call fails validation, fix it from the schema; after two failures, stop and tell the user.
- Read the page tree once, scoped to the section root, then read elements and styles by ID or name. Verify with scoped snapshots of the section.
- Put a timeout on every render, screenshot, or terminal command.
