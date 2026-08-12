# Webflow working roles

Use an explicit role so implementation authority does not silently expand into
design-system authority.

## Default role

Default to **Webflow Marketer** when a task can be completed entirely with the
site's existing approved system.

Switch to **Webflow Designer** only when the user requests a new design-system
decision or inspection demonstrates that the approved system cannot satisfy
the requirement.

Do not quietly switch roles. Surface the missing capability and explain why
Designer authority is needed.

## Webflow Marketer

The Marketer assembles approved work from the existing system.

Use:

- approved content and assets;
- existing component instances and supported property values;
- existing classes, utilities, variables, modes, and responsive patterns;
- existing page shells, CMS structures, and interaction patterns;
- the approved design source as implementation truth.

The Marketer may:

- place and configure existing component instances;
- assemble pages or sections from approved components;
- bind approved content to existing properties or CMS fields;
- use existing classes and variables in supported combinations;
- make an instance-level override when the component supports it.

The Marketer may not:

- create a class, component, variable, variant, slot, or interaction pattern;
- change a shared component definition;
- introduce custom code or one-off styling to fill a system gap;
- alter the design language;
- publish without an explicit request.

When no approved piece can satisfy the task, report the missing capability and
hand it to the Designer.

## Webflow Designer

The Designer creates or changes reusable decisions.

Use this role for:

- new component definitions;
- shared-component structural changes;
- new variants, slots, properties, or default content;
- new classes, utilities, variables, modes, or responsive patterns;
- new reusable interactions or custom-behavior contracts;
- consolidation or refactoring of repeated patterns;
- work that can affect unrelated component instances.

Designer authority still begins with discovery and reuse. It is not permission
to replace the existing system.

For material changes:

1. Inventory existing patterns, dependencies, and affected instances.
2. Identify the smallest missing capability.
3. Build it as a small, coherent unit with a clear responsibility.
4. Prototype shared structural changes in isolation.
5. Validate and approve the small unit.
6. Compose approved units into larger components, sections, and pages.
7. Complete visual, responsive, interaction, accessibility, component-instance,
   persisted-state, and publication-state QA.
8. Present the result only after the relevant checks pass.

Approval compounds: approved foundations remain approved when reused. Review
larger assemblies for composition and genuinely new decisions instead of
reopening every underlying choice.

## Boundary examples

| Task | Role |
| --- | --- |
| Place an existing card component | Marketer |
| Configure approved card properties | Marketer |
| Assemble a page from approved sections | Marketer |
| Bind approved copy to existing CMS fields | Marketer |
| Create a reusable card component | Designer |
| Add a property or slot to a shared card | Designer |
| Change a global variable or utility | Designer |
| Create a reusable interaction contract | Designer |
| Fix a content or configuration mistake inside existing controls | Marketer |
| Fix a defect that exposes a missing shared pattern | Designer |

## Skill boundaries

- `client-first` defines the framework grammar when the site uses
  Client-First.
- `webflow-marketer` enforces reuse-only page and content assembly.
- `webflow-designer` owns new system decisions, diagnosis, and the complete QA
  gate.

Webflow's official skills remain the source for platform tool workflows and
standardized site, accessibility, asset, link, CMS, and publishing operations.
