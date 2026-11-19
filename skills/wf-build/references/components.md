# Name and describe components

A component's name, group and description are its **search surface**. The MCP's component query matches keywords as substrings against those three fields, and every keyword must match. An agent whose search returns nothing builds the piece from elements and new classes, so a component with a weak search surface goes unused.

Follow this when creating a component, converting a section to one, or auditing a library.

## Name

Follow the grammar file's component naming and the names already on the site. Within those:

- **Component:** the plain word a builder asks for, such as `Heading`, `Button` or `Pricing Card`. One responsibility gets one component.
- **Group:** the tier, so the group says how the component is used. Atoms are single elements such as a heading, button, icon or spacer. Blocks are built from atoms, such as a card or form field. Sections are full page sections. Global holds the nav, footer and styles. Use the site's own group names where it has them.
- **Variant:** the Style Guide's word for the look, such as `Primary` or `H2`.
- **Prop:** what the control changes on the page, such as `Heading tag`, `Style` or `Show icon`. Give related props one prop group.

## Describe

Write one or two sentences, in this order:

1. **Coverage:** what the component is for, led by the word an agent searches with. Add the synonyms the name lacks, such as title, headline or CTA.
2. **Use:** the props or variants that matter, and what each decides.
3. **Edge:** the nearest case that belongs to another component, with that component named.

The component already holds its prop list, defaults and classes, so the description carries only what an agent cannot read from it: when to reach for it.

| Component | Description |
| --- | --- |
| `Heading` | Every heading, title and headline. Heading tag sets the document level and Style sets the size, so choose each on its own. Body copy uses Rich Text. |
| `Button` | Every button and call-to-action link. Style picks primary, secondary or text. A link inside a sentence uses Text Link. |
| `Spacer` | Vertical space between blocks inside a section. Size picks the step from the spacing scale. Space above and below a whole section comes from Section. |

Give each prop a tooltip of one line saying which value to choose and when. For `Heading tag`: "Document outline level, one H1 per page. Style sets the size."

## Audit a library

1. List every component with its group, description, props and tooltips.
2. Run the **search test** on each: query the plain word a builder would use and confirm the component comes back. Test the synonyms too.
3. Mark library components from an installed Shared Library. Their changes happen on the source site.
4. Propose the names, groups, descriptions and tooltips as one table, and stop until the user approves. These are shared definitions.
5. Write the approved values, read them back, and rerun the search test.

Done when every component has a group and a description, and every search test returns its component.

When the site has agent instructions that index the library, update them in the same job per [site-instructions.md](site-instructions.md).
