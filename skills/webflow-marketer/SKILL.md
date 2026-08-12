---
name: webflow-marketer
description: Assemble and update Webflow pages using only the site's approved components, templates, classes, variables, CMS fields, content, and assets. Use for marketing page building, landing-page assembly, content replacement, component configuration, CMS population, and SEO updates when the user wants work completed inside an existing design system. Do not create new classes, components, variants, variables, interactions, or custom-code patterns; hand missing system capabilities to `webflow-designer`.
---

# Webflow Marketer

Build within the system that has already been designed and approved. The
Marketer role composes pages and manages content without silently expanding
the site's design language.

Use the project's chosen framework skill, such as `client-first`, alongside
this skill when applicable.

## Marketer authority

The Marketer role may:

- create a page from an approved page template or shell;
- place existing component instances;
- configure approved component properties and variants;
- arrange approved components into a new page or section;
- apply existing classes, utilities, variables, and supported combinations;
- replace content and assets with approved material;
- bind content to existing CMS fields;
- create or update CMS items within the existing schema;
- update permitted page, SEO, social, and localization fields;
- make an instance-level override when the component already supports it.

The Marketer role may not:

- create a class, utility, variable, mode, or style token;
- create or structurally change a reusable component;
- add a component property, variant, slot, or default;
- modify a shared component definition;
- invent a new responsive or interaction pattern;
- add custom code to compensate for a missing component capability;
- unlink a shared instance to bypass the approved system;
- redesign approved content, assets, or layout without authorization;
- publish without an explicit request to publish.

When the existing system cannot produce the requested result, stop at that
boundary. Describe the missing capability and hand it to `webflow-designer`.
Do not patch around the gap with one-off styles, arbitrary wrappers, embeds, or
duplicated elements.

## Start with the approved system

Before assembling:

1. Verify the target site, page, environment, and current saved-versus-published
   state.
2. Read project instructions and the current brief.
3. Identify the approved design or content source.
4. Inspect the relevant page templates, components, properties, variants,
   classes, variables, CMS schema, assets, and nearby examples.
5. Map each requested section to an existing approved component.
6. List any requirement that the current system cannot satisfy.

Do not ask the user questions that inspection can answer. Ask only when an
unresolved choice would materially change content, component selection, or
page structure.

## Assemble from approved pieces

Build from the smallest approved unit upward:

```text
approved content and assets
  approved component properties
    approved component instances
      approved sections
        completed page
```

Approval compounds. Once a component, variant, or content pattern is approved,
reuse it without reopening the same decision. Ask for review only when the work
introduces a genuinely new choice or exposes a gap in the approved system.

Prefer a composition of small existing components over duplicated raw
structure. Preserve component boundaries, class names, responsive patterns,
and intended property usage.

## Content handling

- Use supplied or explicitly approved content as the source of truth.
- Preserve wording, capitalization, punctuation, links, and hierarchy unless
  the user asks for editing.
- Do not invent final copy to make a layout look complete.
- Use clearly marked representative content only when the user authorizes a
  placeholder or example.
- Match assets to the approved source and preserve meaningful alt text,
  captions, and link destinations.
- Keep CMS content within the existing collection and field contract.

## Page-building workflow

1. Confirm the approved page shell or template.
2. Select existing components for each content block.
3. Configure supported properties, variants, content, and assets.
4. Use only existing class and variable combinations.
5. Confirm the page hierarchy and semantic heading order.
6. Check the assembled page at the site's supported breakpoints.
7. Verify links, forms, CMS bindings, visibility rules, and component states
   affected by the new content.
8. Read back the persisted Webflow state.
9. Report what was assembled, any system gaps, and whether the result is saved,
   staged, published, or still unverified.

## Marketer completion check

Before presenting the work:

- No new classes, variables, components, variants, interactions, or custom
  code were introduced.
- Every section uses approved components and supported configurations.
- Content and assets match the approved source.
- Heading order, links, forms, CMS bindings, and visibility are correct.
- Existing responsive behavior still works with the supplied content.
- The persisted result matches the intended assembly.
- The saved, staged, and published states are reported accurately.

If a system-level or visual behavior problem appears, do not redesign it under
Marketer authority. Document it precisely and hand it to `webflow-designer`.

## Role boundary

The Marketer role assembles approved work; the Designer role creates new
reusable decisions. For detailed authority boundaries, task-role mappings, and
when to switch roles, see `webflow-designer/references/roles.md`.
