# Write the site's agent instructions

Webflow stores agent instructions on the site, where Webflow's AI Assistant and every MCP-connected agent read them. A **rule** is read before every action. A **skill** is read when the task matches its description or the user names it. Use the pair to make agents build from the component library: the rule carries the reflex, and the skill carries the map.

[Webflow's guide](https://help.webflow.com/hc/en-us/articles/52536649709971-Create-and-manage-AI-agent-instructions) covers the Instructions panel, import and export.

## 1. Read what exists

Search the site's instructions and read each one. A missing-scope error means the connection was authorized before instructions existed, so reauthorize it with `wf-mcp-setup`. Instructions installed from a Shared Library change on the source site.

Done when you can list every rule and skill on the site, and whether each is on.

## 2. Prepare the library

Instructions point at components, so they work only as well as the components' search surface. Run the audit in [components.md](components.md) first.

## 3. Write one rule

A rule spends context on every action, so it holds the reflex and nothing else. Store it at `rules/components-first.md`, naming the site's own atoms:

```md
Build from the component library. Before adding an element, search the site's components for it and place an instance of the match, then set its props and variants. Headings, buttons, links, icons and spacers each have a component. Add an element with a class only when the search returns no fit, and name that gap in your report.
```

## 4. Write the library skill

Store it at `<skill-name>/SKILL.md`, with a lowercase kebab-case name that uses the site's word for its system, such as `component-library`. Its description is the trigger, so lead with the task: "Choose and compose components when building or changing any page, section or element."

The body holds what no single component description can:

- **Ladder:** the order to try, from component to existing class to combo class to asking the user.
- **Index:** one row per component, mapping the need to the component. "A heading or title" maps to `Heading`.
- **Composition:** which components go inside which slots, and the order of pieces in a standard section.
- **Edges:** the needs with no component, and what to build for each.

Insert each component as a reference rather than typed text. Webflow resolves references when an agent reads the skill, so props, variants and descriptions stay current and the skill never copies them. To learn the reference syntax, read an existing instruction with references unresolved. Where the site has none, write each component's exact name and ask the user to swap the names for references in the editor.

Keep the body to one screen. Split a larger library by tier into companion files, such as `<skill-name>/references/atoms.md`, each named in the body with when to read it.

Webflow can generate a Design System skill from the site. Generation spends the workspace's AI credits, so ask the user first. Treat the draft as raw material, and cut it to the shape above.

## 5. Turn on and test

Create both as drafts and show them to the user. New instructions start off, and the user turns each on in the Instructions panel.

Then run the **cold test**: a fresh agent with no brief, on the sandbox page, asked to add a section with a heading, a paragraph and a button. It passes when readback shows a component instance for each atom and no new classes. When it fails, sharpen the missed component's description first, then the skill's index, then the rule.

Done when both are on and the cold test passes.

## Keep current

When a component is added, renamed or removed, update its description and its index row in the same job.
