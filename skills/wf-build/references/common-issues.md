# Common issues (Webflow MCP)

Known Webflow MCP and Designer behavior that costs time if you don't expect it.

## Classes and combos

- Two combos with the same name on different bases can attach to the wrong class. After creating a combo, read the element's classes back.
- Applying two utilities as one MCP style write can create a useless empty class. Prefer two style names on the element, or create/apply each utility the way the Designer would.
- Webflow's visible class list and its native selector-chain metadata are separate facts: a readback of several class names does not prove the intended chain. Create and repair stacks through a Webflow-native path, verify the expanded selector list in Designer, and confirm the persisted records.

## Elements and nesting

- The MCP reports Div Blocks and Text Blocks both as `Block`, so readback can't tell them apart. Choose the right type when building, and confirm in Designer.
- **Text Link** (`Link`) generally cannot nest Div / HtmlEmbed children. For a clickable row with an icon, chevron, or other nested block, use a **Link Block**.
- The MCP can't create a native **Navbar** (`w-nav`), even with the Designer bridge open. Dropdown, Tabs, and Slider work. Navbar markup sent as HTML lands as plain Divs and Links with the `w-` classes dropped, so there is no collapse or menu button. Ask the user to add a Navbar in Designer, then build inside it.
- Native Tabs can fail to take a new tab. Add a fresh tab item and restyle it, or ask the user for help.

## Attributes and props

- Binding custom attributes (`data-*`, etc.) to component string/id props via MCP often fails or is rejected. Prefer runtime JS to stamp attrs, or bind in the Designer UI when the API won't.
- Page links set at create time can save as `#` or with no link at all. Set the link, then read it back.
- `set_text` rejects a Div that wraps a text node, and the builder can ignore it on a Text Block, leaving Webflow's default text. Target the child String node's ID, and read it back.
- The API can't read or set date formats or option-based conditional visibility. Replacing a bound element loses both, so warn the user before rebuilding it.

## Variables

- A variable can alias a variable in another collection, through both create and update.
- The MCP can create a variable collection but not delete one, so create collections only as the grammar or the approved Style Guide lays them out.

## Designer / MCP session

- Saved draft, Designer canvas, Preview, and the published staging/live site can disagree. Ask the user to refresh the canvas, or get permission before publishing to staging.
- `element_snapshot_tool` can time out while other Designer calls still work. After two timeouts, ask for approval to stage, then check the staged page per [staging-check.md](staging-check.md).
- Designer MCP needs an active Designer tab with the MCP app running. If tools time out or say they can't connect, stop and wait for the user to reopen Designer. The published site is a different surface from the canvas.
- When editing a **component definition**, the canvas may report a different `pageId` than the host page you opened from. Use the `pageId` returned by select/get-current for writes inside that component view; pass `scope_component_id` when tools require it.
- Large nested creates get truncated. Several medium writes beat one giant one.
- `column-gap` / `row-gap` don't display in Designer's Gap field; write `grid-column-gap` / `grid-row-gap`. If a written property doesn't appear in the Style panel, switch to the name Designer expects.

## Breakpoints and state

- Style changes on `main` cascade; overrides on `medium` / `small` / `tiny` only where needed. Confirm the breakpoint you intended after an update.
- Open/active UI state that JS toggles must match the class the script actually sets. If the script targets a child and the markup puts the icon as a sibling (or the reverse), rotate/open styles won't fire, so align markup and script, or use a selector that matches the real DOM.

## Publishing

- To stage without touching custom domains, call `publish_site` with `customDomains: []` and `publishToWebflowSubdomain: true`, then confirm the production pages still lack the change. A stage publish is still a real publish.
- API readback isn't published output. Confirm form names, visibility and date formats in the published HTML: a radio group can read back as one shared `groupName` while the published `name` attributes stay `radio`, `radio-2`, `radio-3`.

## Keeping runs small

- Read a tool's input schema before the first call and reuse the shape that worked. If a call fails validation, fix it from the schema; after two failures, stop and tell the user.
- Read the page tree once, scoped to the section root, then read elements and styles by ID or name. Verify with scoped snapshots of the section.
- Put a timeout on every render, screenshot, or terminal command.
- `webflow_guide_tool` and `list_pages` can return more than the tool output limit and spill to a file. Take the `ses_` session ID from the guide's first text block, and read page IDs with `grep`.
