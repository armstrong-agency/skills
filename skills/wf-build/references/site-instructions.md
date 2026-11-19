# Write the site's agent instructions

Webflow stores agent instructions on the site, where Webflow's AI Assistant and every MCP-connected agent read them. A **rule** is read before every action. A **skill** is read when the task matches its description or the user names it. Use the pair to make agents build from the component library: the rule carries the reflex, and the skill carries the map.

Two things must hold when you finish:

- **Component-forward:** the instructions tell every agent to search the components before it builds, and to use the one whose job matches. The agent judges the fit. A component that is close but wrong for the job stays unused, and a component or atom that does the job always wins over a new class.
- **Every component documented:** each component says where to use it, in its own description and in a row of the skill's index.

[Webflow's guide](https://help.webflow.com/hc/en-us/articles/52536649709971-Create-and-manage-AI-agent-instructions) covers the Instructions panel, import and export.

## 1. Read what exists

Search the site's instructions and read each one. Instructions installed from a Shared Library change on the source site.

Done when you can list every rule and skill on the site, and whether each is on.

## 2. Prepare the library

Instructions point at components, so they work only as well as the components' search surface. Run the audit in [components.md](components.md) first.

Done when every component has a description that says where to use it.

## 3. Write one rule

A rule spends context on every action, so it holds the reflex and nothing else. Store it at `rules/component-forward.md`, naming the site's own atoms:

```md
Work component-forward. Before building an element, search the site's components and read the description of each match. Use the component whose job matches, and set its props and variants. Headings, buttons, links, icons and spacers each have an atom. When a component is close but wrong for the job, leave it as it is, build from existing classes, and name the gap in your report. Create a new class only for a job that no component or atom does.
```

## 4. Write the library skill

Store it at `<skill-name>/SKILL.md`, with a lowercase kebab-case name that uses the site's word for its system, such as `component-library`. Its description is the trigger, so lead with the task: "Choose and compose components when building or changing any page, section or element."

The body holds what no single component description can:

- **Ladder:** the order to try, from component to existing class to combo class to asking the user, and how to judge fit: a component fits when its job matches, even where its content or variant must change.
- **Index:** one row for every component, giving the need it answers and where it is used. "A heading or title" maps to `Atom / Heading`, used in every section and card.
- **Composition:** which components go inside which slots, and the order of pieces in a standard section.
- **Edges:** the needs with no component, and what to build for each.

Insert each component as a reference rather than typed text. Webflow resolves references when an agent reads the skill, so props, variants and descriptions stay current and the skill never copies them. To learn the reference syntax, read an existing instruction with references unresolved. Where the site has none, write each component's exact name and ask the user to swap the names for references in the editor.

Keep the body to one screen. Split a larger library by tier into companion files, such as `<skill-name>/references/atoms.md`, each named in the body with when to read it.

Webflow can generate a Design System skill from the site. Generation spends the workspace's AI credits, so ask the user first. Treat the draft as raw material, and cut it to the shape above.

## 5. Turn on and test

Create both as drafts and show them to the user. New instructions start off, and the user turns each on in the Instructions panel.

Then run the **cold test**: a fresh agent with no brief, on the sandbox page, asked to add a section with a heading, a paragraph and a button. It passes when readback shows a component instance for each atom and no new classes. When it fails, sharpen the missed component's description first, then the skill's index, then the rule.

Done when both are on, every component has a description and an index row, and the cold test passes.

## Keep current

When a component is added, renamed or removed, write or update its description and its index row in the same job.
