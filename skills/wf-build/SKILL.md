---
name: wf-build
description: Implement a planned Webflow section in Webflow MCP using existing classes first, native Style panel fields, and one section at a time. Use when building or putting a prototype into Webflow. Pair with framework-grammar files for class names. Never publish unless the user explicitly asks.
---

# Webflow build

**Version 0.1.0**

Put a planned (and usually prototyped) section into Webflow.

You can start here with no prior skills. Ask first — it's slower without `webflow-context.md` from audit and plan.

## Before you write

Read `webflow-context.md` if it exists. Read the framework grammar file to find the appropriate convention.

If context is thin, ask:

1. Which site and page (default: a new unpublished draft page).
2. Which section, this pass only.
3. Framework — or wait until they point at audit/plan.
4. Destination from the plan: draft, staging, or production. Don't publish unless they explicitly ask.

List the Webflow MCP tools this session actually exposes. Use those names. Official Webflow MCP docs cover how the tools work.

## One section at a time

Don't take the whole page in one bite. Finish a section, show it, then ask for the next.

Reuse in this order: existing component → existing class → combo on an existing class → new class (only if the plan already justified it).

## Native styling

Set appearance with Designer Style panel fields (or MCP properties that map to them): size, margin, padding, display, flex, grid, position, typography, background, border, radius, shadow, overflow, opacity.

No custom CSS, embeds, or page `<style>` for layout or decoration. If Designer can't set it, say so. User may approve custom css but default is to work natively in Webflow.

No Navigator labels / display names. Class names are the names. Relabeling elements in the Navigator is confusing and unnecessary.

Images, icons, and embeds sit beside text, not inside headings or paragraphs as <span> elements.

Don't create a Webflow variable for a one-off Height or Width. Variables are shared tokens and should be part of the full design system. 


## Common issues

- Variable aliases stay in the same collection. Cross-collection aliases fail. Creating a collection is usually a one-way door — keep primitives and semantics together.
- Put text on headings, paragraphs, and text links. A generic Div is not for text content.
- Two combos with the same name (`is-secondary` on different bases) can attach to the wrong class. Check after creating one.
- Page links set at create time can save as `#`. Set the link, then read it back.
- Don't unlink a component to work around a failed insert. Insert into a parent, then reorder.
- Saved draft, Designer canvas, Preview, and the live site can disagree. Ask the user to refresh their canvas or get permission to publish to staging. 
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
