# Webflow headless quirks catalogue

This file records verified MCP behaviors that are not obvious from tool
descriptions. Prefer the currently exposed MCP tools and their documentation;
use these notes to anticipate edge cases and work around known limitations.


- `data_variable_tool` aliases (`existing_variable_id`) resolve **only within the same collection** — cross-collection refs fail with "Referenced variable not found". There is also no delete/rename-collection action, so `create_variable_collection` is a one-way door. Consequence: keep base primitives and semantic tokens in one collection (primitives as `Neutral / …` groups). Non-default collections also prefix CSS names (`--_base-colors---neutral--0`); the default collection yields clean `--neutral--0`.
- `data_element_builder` type `TextBlock` actually creates a div **Block**, and its `set_text` silently no-ops on it. Set/read text via `data_element_tool > set_settings` key `text` (static or prop binding). `Heading`/`Paragraph`/`TextLink` set_text works fine.
- `set_text`/`set_link` actions only work on genuinely text/Link-capable elements. `NavbarLink` (and similar) take their target via `set_settings` key `link` (`static_link` mode `page`).
- Image elements bind image props via settings key **`assetId`**; alt text via `altText`.
- `ComponentSlot` can only be created **inside a component definition**, cannot hold default children from the builder, and is filled **per instance** — insert component instances via `data_component_builder > insert_in_slot` (default slot name `Slot`). Wrap slot content in a micro-component (e.g. `Logo - Item`).
- `element_snapshot_tool` needs a live Designer session — no headless visual verification; defer to later stages.
- **The CF base's custom tag styles are rich-text-scoped.** What looks like the `h1`/`h4`/`h5`/`h6` tag style publishes as `.text-rich-text h1` etc.; the bare tag defaults are separate `default-*` styles, and `update_style` by name may hit either. Consequence: bindings applied to the "tag" can silently not affect page headings (invisible until a font change exposes it). Rule: **typography lives on classes** (`hero_heading`, `section_heading`, `heading-style-h*`) — tag styles are a fallback, never the only carrier.
- Keep single MCP calls modest: very large nested `element_builder` payloads get truncated in transit. A few medium calls beat one giant one.
- Creating pages early (as drafts) lets nav/footer links bind real page ids from the start — no placeholder-link sweep later.
- `asset_tool > upload_image_by_url` is a **Designer** tool (needs a live Designer session). The headless path is `data_assets_tool > create_asset` (file name + MD5) → multipart POST of the bytes to the returned presigned S3 URL (map the camelCase uploadDetails keys to their S3 form-field names: `xAmzAlgorithm` → `X-Amz-Algorithm`, `successActionStatus` → `success_action_status`, `contentType` → `Content-Type`, `cacheControl` → `cache-control`). Works from Bash with curl.
- Icon sourcing headlessly: the Iconify CDN serves any Remix Icon pre-colored (`https://api.iconify.design/ri/<name>.svg?color=%23<hex>`) — download, hash, upload. Apache 2.0; list on `/licenses`.
- Image props: component **defaults** take the asset id via `update_prop.default_text.value`; **instance overrides** take it via `set_component_instance_prop_values` with `type: "string", string_value: <assetId>`.
- OG images can be set headlessly: `update_page_settings.openGraph.imageAssetId`. Favicon/webclip are site settings — human step in the dashboard.
- **`data_element_builder`'s `set_link` with `link_type: "page"` silently writes `{mode: "url", to: "#"}`** — a broken link that only shows up on the published site. Only `url` mode works at creation. Always set page links afterward via `data_element_tool > set_settings` key `link` with `static_link {mode: "page", to: <pageId>}`, and verify with `get_settings` (query-result summaries display page links as `linkType: "none"`, which is normal).
- **Combo-class name collisions make `set_style` resolution nondeterministic**: two combos named `is-secondary` (ours under `button`, the CF base's under `fs-styleguide_color-sample`) caused some elements to get the wrong chain plus a stray parent class. After creating an `is-*` combo, check whether the base site already has a combo with that name; sweep affected elements by querying for the stray parent class.
- `curl` the published site and grep for `href="#"`, placeholder copy, and expected markers — cheapest end-to-end verification; the Data API view can look right while the published output is wrong.
- **Visual verification that actually works headless:** plain `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --screenshot=<out.png> --window-size=1440,2400 --hide-scrollbars <url-or-file://>` — reliable where the agent-browser daemon was not. Use it for specimen gates and build→screenshot→adjust loops against the published staging URL. Never build pages blind again.

## Observed 2026-07-27 — revalidate before use

The following MCP and Designer behaviors are time-sensitive observations, not
stable platform contracts. Recheck the currently exposed capabilities before
depending on them.

- **Component instances may reject relative insertion anchors.** In current
  public-MCP behavior, inserting `before` or `after` a component instance can
  fail even when the target id is valid. Insert into a supported editable
  parent, use the available native move/reorder operation on siblings, then
  reread the complete sibling order. Do not unlink a component or leave it in
  the wrong location merely to work around the anchor limitation.
- **WHTML transport and persisted representation are different facts.**
  `data_whtml_builder` can materialize editable Webflow elements, classes, and
  linked library assets, but raw `var()` references may emit
  `unknown_variable` warnings even when the browser later resolves the CSS
  custom property. Prefer variable-aware native style actions when exposed;
  otherwise verify the persisted nodes, selectors, breakpoint rules, and
  computed Preview values before accepting the result.
- **Fuzzy style searches can return misleading candidates.** A plausible name
  is not reuse evidence. Inspect declarations, breakpoints, variable bindings,
  consumers, and behavior before changing a class; use exact-name or
  locally-filtered inventory when fuzzy results are noisy.
- **Preview custom-code compilation can block runtime QA without blocking
  native visual QA.** Temporarily disabling execution can isolate layout and
  styling, but Finsweet Attributes, active states, scroll offsets, and other
  custom behavior remain unverified. Do not publish as a workaround for a
  stuck compiler.
