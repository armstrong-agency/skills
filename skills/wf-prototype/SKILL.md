---
name: wf-prototype
description: Prototype in Webflow on a draft or sandbox page using only existing components, classes, combos, and variables. Use when exploring, mocking, assembling, trying a layout, or validating a plan without inventing new system classes or publishing. Uses wf-reference for naming grammar.
---

# Webflow Prototype

Explore in Webflow without changing the design system. Default destination is a **new unpublished draft/sandbox page**. Promote nothing from this skill.

If the work needs new classes, components, variables, or interactions, stop and send that to `wf-plan` / `wf-build`. Do not invent during a prototype.

## Grammar first

Load the `wf-reference` skill and follow its convention check before assembling classes. If `wf-reference` is not installed, stop and tell the user to run `npx skills add armstrong-agency/skills --skill wf-reference`.

## Discover tools, then act

Do not assume Webflow MCP tool or action names. List the tools and actions exposed in this session and use those. Revalidate a named action before depending on it. Read `common-issues.md` in `wf-reference` for combo attachment, nesting, Designer session, and related MCP quirks.

## Destination

- Prefer a new unpublished draft or sandbox page.
- Do not write onto a live page.
- Do not add sections to a real/live page.
- Do not publish to staging or production.

Approving a prototype section does not promote or publish it.

## Assemble only

May use:

- existing components
- existing classes
- already-approved combos
- already-approved variables and modes
- instance-prop overrides the component already supports

May not:

- create system classes, components, variables, or interactions
- unlink components to bypass the system
- add custom code to patch missing capabilities
- overwrite existing page content on a real page

When the system cannot produce the requested result, stop and describe the missing capability. Do not patch around it with one-off styles, extra wrappers, or duplicated elements.

## Native styling still applies

Use Designer-native Style panel fields (or MCP properties that map to them). Do not invent unsupported CSS, one-off custom properties for Height/Width/Margin/Padding/Display/Position/Background, or Custom Code / page `<style>` / Global Canvas CSS dumps for presentation.

## Structure habits

- Do not set Webflow labels (Navigator display names) unless the user asked for them.
- Do not nest Image, icon, or embed nodes inside text elements (span, paragraph, heading). Place them as sibling nodes.
- Work one section at a time.
- For risky shared-component experiments, duplicate the component onto the sandbox page. Never unlink to “just try it.”

## When the prototype is enough

Copy swaps, instance-prop tweaks, and assembling approved pieces: reuse, show the sandbox, report. Skip a full plan/build loop.

## Handoff

```text
Sandbox/draft page:
Grammar used:
Assembled:
System could not do:
Checked: [canvas / Preview / none]
Needs wf-build: [invent | promote | no]
Published: no
```

Lead with the prototype the user can look at. Do not make them reconstruct it from tool calls.
