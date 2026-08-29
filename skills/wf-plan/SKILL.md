---
name: wf-plan
description: Plan Webflow work with the user before anything is built — what to make, mobile behavior, reuse vs new classes, and whether the destination is draft, staging, or production. Use when the user asks to plan, scope, or figure out a Webflow page or section. Does not write to Webflow.
---

# Webflow plan

**Version 0.1.0**

Talk to the user until the job is specific and context is clear. Plan the classes you want to use. Confirm and get permission. Stop before building. Nothing is written to Webflow from this skill.

## Start from context

Read `webflow-context.md` if it exists. Audit may already have grammar, colors, and classes.

Once the naming convention is determined, find the appropriate convention file in the `framework-grammar` folder and use it for naming.

If context is missing, ask the user or run `wf-audit` first.

## Ask

1. **What are we building?** Page, section, extra behavior (forms, CMS, motion).
2. **Mobile.** What should change at tablet and phone.
3. **Destination.** Unpublished draft, staging, or production — when they eventually ship. Plan does not publish. Build will follow this answer.

Screenshots and Figma files are useful visual guides for understanding user intent. Use them to sample color values, text sizes, spacing, and other style details as accurately as possible.

## Classes

Using the grammar file and the class list in context:

- **Reuse** — existing components, classes, combos, variables.
- **New** — only when reuse can't do the job. Proposed name (from the grammar file) and why.

Go through this with the user. Don't invent a class they haven't confirmed.

## Write

Update `webflow-context.md` with:

```markdown
## Plan

Sections (in order):
- [name]: reuse […] / new […] — why if new
Mobile:
Destination: draft | staging | production
Open questions:
```

## Next

`wf-prototype` for an HTML pass of a section (motion, breakpoints, faster than Webflow). `wf-build` to put it in Webflow. Skipping prototype is allowed; build is slower without a plan and a prototype.
