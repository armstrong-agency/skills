---
name: wf-build
description: Implement a planned Webflow section in Webflow MCP using existing classes first, native Style panel fields, and one section at a time. Use when building or putting a prototype into Webflow. Pair with framework-grammar files for class names. Never publish unless the user explicitly asks.
---

# Webflow build

**Version 0.1.0** — work in progress

Put a planned (and usually prototyped) section into Webflow.

You can start here with no prior skills. Ask first — it's slower without `webflow-context.md` from audit and plan.

## Before you write

Read `webflow-context.md` if it exists. Read `framework-grammar/client-first.md` or `framework-grammar/mast.md` for the site's convention.

If context is thin, ask:

1. Which site and page (default: a new unpublished draft page).
2. Which section, this pass only.
3. Grammar — or wait until they point at audit/plan.
4. Destination from the plan: draft, staging, or production. Don't publish unless they explicitly ask now.

List the Webflow MCP tools this session actually exposes. Use those names. Official Webflow MCP docs cover how the tools work.

## One section at a time

Don't take the whole page in one bite. Finish a section, show it, then ask for the next.

Reuse in this order: existing component → existing class → combo on an existing class → new class (only if the plan already justified it).

## Native styling

Set appearance with Designer Style panel fields (or MCP properties that map to them): size, margin, padding, display, flex, grid, position, typography, background, border, radius, shadow, overflow, opacity.

Prefer longhand (`margin-top`) so a shorthand write doesn't clobber siblings.

No custom CSS, embeds, or page `<style>` for layout or decoration. If Designer can't set it, say so.

No Navigator labels / display names. Class names are the names. Relabeling elements in the Navigator is confusing and unused.

Images, icons, and embeds sit beside text, not inside headings or paragraphs.

Don't create a Webflow variable for a one-off Height or Width. Variables are shared tokens.

## Shared components

If you would change a component definition, say so and work on a duplicate on a draft page first.

**Collection Lists cannot live inside a component.** Put the Collection List outside. Bind CMS fields onto the component instance as props.

## Common issues

- Variable aliases stay in the same collection. Cross-collection aliases fail. Creating a collection is usually a one-way door — keep primitives and semantics together.
- Put text on headings, paragraphs, and text links. A generic Div often ignores text.
- Two combos with the same name (`is-secondary` on different bases) can attach to the wrong class. Check after creating one.
- Page links set at create time can save as `#`. Set the link, then read it back.
- Don't unlink a component to work around a failed insert. Insert into a parent, then reorder.
- Saved draft, Designer canvas, Preview, and the live site can disagree. Publishing is not how you take a screenshot.
- Large nested creates get truncated. Several medium writes beat one giant one.

## Check

- Grammar file was used for names
- This section only
- Native Style panel only
- No Navigator labels
- Desktop and smaller breakpoints
- Saved vs published called out honestly

## After

Update `webflow-context.md` with what was created, reused, and still open. Lead with the page the user can open, not a list of tool calls.
