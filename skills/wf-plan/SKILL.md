---
name: wf-plan
description: Plan Webflow work before writing — page and section inventory, reuse discovery, Figma mapping, and written justifications for anything new. Use whenever the user asks to plan, map, estimate, scope, or figure out how to build in Webflow before implementation. Uses wf-reference for naming grammar. Do not mutate the site from this skill.
---

# Webflow Plan

Decide what to build, what to reuse, and what needs approval — then stop. This skill does not create classes, components, or page content.

Use `wf-prototype` or `wf-build` only after the plan is approved.

## Grammar first

Load the `wf-reference` skill and follow its convention check before recommending a class name. If `wf-reference` is not installed, stop and tell the user to run `npx skills add armstrong-agency/skills --skill wf-reference`.

If the style guide and framework disagree, flag it in the plan.

Skim `common-issues.md` in `wf-reference` for MCP/Designer constraints that affect feasibility (nesting limits, variable scoping, component unlinking, Designer session state).

## Ask first

1. **Where should this live?** Default recommendation: a new unpublished draft/sandbox page. Do not assume a live page.
2. **What is the source of truth?** Live Webflow, Figma, a screenshot, a written brief, or a mix. State which evidence is authoritative for each claim.
3. **Which framework?** Answered by Grammar first. Do not skip it.

## Page plan

List sections in order. For each section record:

- responsibility (what the band is for)
- closest existing Webflow component, class, utility, or live section
- Figma node or screenshot crop when a design source exists
- assemble vs invent: can this ship from existing pieces, or does it need a new class/component/variable?
- open questions and risks (shared-component blast radius, CMS, interactions)

Do not enter a section build loop from this skill.

## Reuse discovery (required)

Before recommending anything new, inventory:

- components, variants, props, and slots that already own the job
- global and project classes, combos, variables, and modes
- nearby approved pages or style-guide specimens
- Figma visual-similar search when a Figma source is provided

A familiar name is only a candidate. Inspect actual responsibility, breakpoints, consumers, and behavior.

## Justifications for new work

If a new class, combo, component, variable, or interaction is needed, write the justification in the plan *before* anyone builds:

- what existing piece was considered and why it fails
- the distinct responsibility of the new piece
- proposed name using the grammar already read
- where it will be prototyped (draft/sandbox) before any live page

No justification, no invent recommendation.

## Figma

When Figma, a node, or a supplied screenshot is the approved source, calibrate screenshot scale before mapping. Do not treat a raster as CSS pixels until anchors agree. Node data can prove structure, text styles, variables, and measurements; a screenshot proves that capture only.

## Shared-component caution

If the plan would change a shared component definition, inventory instances, variants, slots, and consumers. Recommend prototyping on a duplicate on a sandbox page. Do not recommend unlinking to dodge that work.

## Handoff

Return a plan the next skill can execute. Use this skeleton:

```text
Destination: [sandbox / named page] — not written
Source of truth:
Grammar: [client-first | mast | mixed | none | unclear]
Sections:
- [name]: reuse [x] / invent [y] — justification if invent
Approvals still needed:
Unproven:
```

Do not present a plan as completed implementation.
