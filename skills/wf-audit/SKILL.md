---
name: wf-audit
description: Review a Webflow site's style guide, colors, and class naming. Use when the user asks to audit, review, inspect, or catalog the design system of a Webflow site. Writes a project context file for later plan, prototype, and build work. Does not change the site.
---

# Webflow audit

**Version 0.1.0** — work in progress

Look at the site. Record the style guide, colors, and classes. Confirm with the user. Write `webflow-context.md` so plan, prototype, and build can reuse it.

A public URL is enough. A connected Webflow MCP session can add class and variable names the published HTML doesn't show.

## Walkthrough

Work like a wizard. After each chunk, show what you found and ask if it's right before continuing.

1. **Where** — public URL, and Webflow connection if they have one.
2. **Style guide** — is there a Style Guide page or equivalent? Name it.
3. **Naming** — Client-First, Mast, mixed, or none. If it matches `framework-grammar/client-first.md` or `framework-grammar/mast.md`, read that file. Ask the user to confirm.
4. **Colors** — the palette actually in use (hex or variable names). "Is this the brand set?"
5. **Type** — families and the recurring sizes you can see.
6. **Classes** — structure, utilities, and components the project already has. This is the reuse list for later skills.
7. **Buttons and controls** — primary / secondary (and any other states you can see). "Is this the right button?"

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

Use observed values. If the user corrects you, write their version.

## Done

Show the file. Next skill is usually `wf-plan`.
