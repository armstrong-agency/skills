---
name: wf-audit
description: Review a Webflow site's style guide, colors, and class naming. Use when the user asks to audit, review, inspect, or catalog the design system of a Webflow site. Writes a project context file for later plan, prototype, and build work. Does not change the site.
---

# Webflow audit

**Version 0.1.0**

Look at the site. Record the style guide, colors, and classes. Confirm with the user. Write `webflow-context.md` so plan, prototype, and build can reuse it.

A public URL is enough. A connected Webflow MCP session can add class and variable names the published HTML doesn't show.

## Walkthrough

Do the whole pass, then write the file. Ask only if you cannot find the site.

1. **Where** — use the public URL they gave, or the connected Webflow site. Ask only if neither is available.
2. **Style guide** — find a Style Guide page or equivalent. Name it. If none, say so.
3. **Naming** — Client-First, Mast, mixed, or none. If it matches `framework-grammar/client-first.md` or `framework-grammar/mast.md`, read that file. Infer from class names; don't wait for the user to name the convention.
4. **Colors** — the palette actually in use (hex or variable names).
5. **Type** — families and the recurring sizes you can see.
6. **Classes** — structure, utilities, and components the project already has. This is the reuse list for later skills.
7. **Buttons and controls** — primary / secondary (and any other states you can see).

## Write `webflow-context.md`

At the project root (or a path the user names):

```markdown
# Webflow context

Grammar: client-first | mast | mixed | none
Style guide:
Colors:
Type:
Classes:
Controls:
Notes:
```

Use observed values. If the user corrects you after seeing the file, write their version.

## Done

Show the file. Next skill is usually `wf-plan`.
