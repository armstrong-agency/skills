---
name: wf-prototype
description: Build a standalone HTML prototype of one Webflow section for layout, mobile, and motion timing before using Webflow MCP. Use when exploring, mocking, timing animation, or checking breakpoints. Faster than building in Webflow. Does not write to Webflow.
---

# Webflow prototype

**Version 0.1.0** — work in progress

HTML for **one section**. This sits between plan and build. It's for layout, mobile, and animation timing — faster than Webflow MCP.

No Webflow MCP in this skill. If they want it in Webflow, that's `wf-build`.

## Start from context

Read `webflow-context.md` and the matching `framework-grammar/` file. Use the classes and structure already planned. If those files are missing, ask, or send them to `wf-audit` / `wf-plan`.

## Make the prototype

Write a self-contained HTML file in the project, for example `prototype/<section>.html`, with CSS in the same file or beside it.

Match the planned class names so build can translate them. Include the mobile behavior from the plan. If motion matters, put the timing in CSS so the user can feel it.

Open it in the browser so they have a page to click (local file or a local preview URL).

One section per pass. Don't prototype the whole site in one file.

## When it's right

Update `webflow-context.md`:

```markdown
## Prototype

Section:
File:
What to carry into Webflow:
```

Then stop. `wf-build` takes this into Webflow, one section at a time.
