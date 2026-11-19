# Name and describe components

A component's name, group and description are its **search surface**. The MCP's component query matches keywords as substrings against those three fields, and every keyword must match. An agent whose search returns nothing builds the piece from elements and new classes, so a component with a weak search surface goes unused.

Follow this when creating a component, converting a section to one, or auditing a library.

## Name

A site with a consistent convention of its own keeps it. Otherwise name every component `Tier / Thing`, and place it in the group named for its tier in the plural: `Atom / Heading` sits in Atoms.

| Tier | Holds | Example |
| --- | --- | --- |
| `Atom` | Any piece used inside a section or another component | `Atom / Heading`, `Atom / Button`, `Atom / FAQ Item` |
| `Card` | A repeated content unit for a grid or list | `Card / Customer` |
| `Layout` | An arrangement of slots with no content of its own | `Layout / Media Grid` |
| `Section` | A full page section | `Section / Hero` |
| `Nav`, `Form` | Navigation pieces and forms | `Nav / Platform`, `Form / Demo` |
| `Global` | One-per-site pieces | `Global / Footer`, `Global / Styles` |
| `Utility` | Structural helpers | `Utility / Spacer` |

Two separators extend a name, and each has one meaning:

- **Slash nests.** `Section / Hero / Form` is the form inside the hero, the way a slash makes an inner folder.
- **Dash modifies.** `Section / Hero - Form` is the hero in its form version, a sibling of `Section / Hero`. Use a dash name when the structure differs, and a variant on one component when only the look differs.

A bracket tag at the end marks behavior: `[Global]` for content shared by every instance, `[CMS]` for a CMS-bound version, `[Flexible]` for a section assembled from slots.

Rename a retired component `Legacy / …` and move it out of its group until its last instance is gone.

Name a variant with the Style Guide's word for the look, such as `Primary` or `H2`.

## Properties

A property is the control an editor or agent uses on an instance. Expose what changes from one instance to the next, and keep the rest fixed in the definition.

- **Name:** what the control changes on the page, such as `Heading tag`, `Style` or `Show icon`. Give related properties one group.
- **Content:** a text, rich text, image, link or video property for each piece that differs per instance.
- **Variant:** a different look on the same structure.
- **Visibility:** an optional part gets an on/off property bound to its visibility, so each instance shows or hides it with one switch. Conditional visibility is a different tool that follows CMS or option values. The API cannot read or set it, so the user sets it in Designer.
- **Slot:** content the component cannot predict.

The MCP creates some property types and only reads others. Before the brief promises a property, check the types the property tool offers in this session, and list the rest for the user to add in Designer. Known property and binding failures are under Attributes and props in [common-issues.md](common-issues.md).

## Describe

Write one or two sentences, in this order:

1. **Coverage:** what the component is for, led by the word an agent searches with. Add the synonyms the name lacks, such as title, headline or CTA.
2. **Use:** the props or variants that matter, and what each decides.
3. **Edge:** the nearest case that belongs to another component, with that component named.

The component already holds its prop list, defaults and classes, so the description carries only what an agent cannot read from it: when to reach for it.

| Component | Description |
| --- | --- |
| `Atom / Heading` | Every heading, title and headline. Heading tag sets the document level and Style sets the size, so choose each on its own. Body copy uses Rich Text. |
| `Atom / Button` | Every button and call-to-action link. Style picks primary, secondary or text. A link inside a sentence uses Text Link. |
| `Utility / Spacer` | Vertical space between blocks inside a section. Size picks the step from the spacing scale. Space above and below a whole section comes from the section component. |

Give each property a tooltip of one line saying which value to choose and when. For `Heading tag`: "Document outline level, one H1 per page. Style sets the size."

## Audit a library

1. List every component with its group, description, props and tooltips.
2. Run the **search test** on each: query the plain word a builder would use and confirm the component comes back. Test the synonyms too.
3. Mark library components from an installed Shared Library. Their changes happen on the source site.
4. Propose the names, groups, descriptions and tooltips as one table, and stop until the user approves. These are shared definitions.
5. Write the approved values, read them back, and rerun the search test.

Done when every component has a group and a description, and every search test returns its component.

When the site has agent instructions that index the library, update them in the same job per [site-instructions.md](site-instructions.md).
