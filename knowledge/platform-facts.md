# Verified Webflow platform facts

> Origin: `docs/armory/decisions.md` and `docs/client-first-v3/findings.md` (armstrong-agency-internal/client-first-v3), migrated 2026-07-07.

## Platform capabilities (verified July 2026)

- Webflow MCP writes elements (3 nesting levels/call), styles with
  breakpoints/pseudo-classes, CSS variables, variable collections + modes,
  native components with props/variants, pages, CMS — via Data API, no open
  Designer session needed. Bridge app only for snapshots/selection. No
  Code Component support, no IX authoring, OAuth = one workspace.
- Collection Lists cannot nest inside components; slots can't hold Collection
  Lists. Supported pattern: Collection List → component instance with
  CMS-bound props (inverse of the old cms-slots hypothesis).
- Claude Design imports design systems from GitHub repos (June 2026); infers
  from real code; DESIGN.md is community convention, not an official format.
- Claude Desktop custom connectors: paste URL + OAuth; Webflow remote MCP at
  mcp.webflow.com/mcp; per-client workspace isolation via OAuth scoping.
- Figma Variables REST API remains Enterprise-only; Tokens Studio /
  Figma MCP `get_variable_defs` are the non-Enterprise paths.


## Shadow DOM / CSS variable inheritance (verified April 2026, client-first-v3 sandbox)


## Finding 1: CSS Custom Properties Inherit Through Shadow DOM

**Confirmed.** Variables defined in Webflow's Variables panel automatically
inherit into Code Components rendered inside Shadow DOM. No bundling, no
special configuration, no opt-in flag.

This is the foundational behavior that makes CF 3.0 possible.

## Finding 2: Real-Time Reactivity

**Confirmed.** Changing a variable value in the Webflow Designer updates Code
Components instantly. The button background color was observed updating in
real time when `--accent-color--primary` was modified in the Variables panel.

This means designers can tune tokens and see components respond without any
developer intervention.

## Finding 3: Classes Do NOT Cross Shadow DOM

**Confirmed.** Client-First utility classes defined on the host site
(`padding-global`, `heading-style-h1`, `text-size-medium`, etc.) have zero
effect inside Code Components. The Shadow DOM boundary is absolute for class-
based styling.

This was validated in Checkpoint 1 — the Hero rendered with browser defaults
until we bundled the Client-First stylesheet inside `globals.ts`.

## Finding 4: Bundling CSS in globals.ts Works But Is Inferior

**Confirmed.** The Checkpoint 1 approach (import entire Client-First
stylesheet into `globals.ts`) renders components correctly. However:

- Creates a static copy that drifts from the host site
- Cannot respond to variable changes
- Cannot adapt to themes (Variable Modes)
- Adds weight to every component's Shadow DOM
- Must be manually kept in sync with the site's actual stylesheet

The token-based approach (Checkpoint 2) is strictly superior in every
dimension except one: it requires the host site to define the tokens.

## Finding 5: All Token Types Work

**Confirmed.** Every variable type supported by Webflow's Variables panel
inherits correctly:

- Color (hex values) → `--accent-color--primary`
- Size (rem/px with unit) → `--spacing--medium`, `--border-radius--large`
- Number (unitless) → `--line-height--tight`
- Font Family (string) → `--font-family--primary`

## Finding 6: Webflow CSS Name Generation Is Predictable

**Confirmed.** Webflow generates CSS custom property names from variable
display names using this formula:

```
"Category / Name" → --category--name
"Category / Multi Word" → --category--multi-word
```

Slashes become `--` separators. Spaces become hyphens. All lowercase.
This makes it trivial to predict the CSS name from the Webflow panel name
and vice versa.

## Finding 7: No Fallbacks = Correct Design

The "strict contract" approach (no fallback values in `var()`) works as
intended. When a token is missing, the property resolves to `initial`,
making the broken state immediately visible. This is better than silent
fallbacks that mask incompatibility.

## Finding 8: Slots Work — Native Elements and Code Components

**Confirmed.** Code Components that declare `props.Slot()` accept both native
Webflow elements and other Code Components as children.

Tested on the Slots Test page:
- **Section Wrapper** (`props.Slot({ name: "Content" })`) — accepts native
  Webflow headings, paragraphs, and other elements dropped into its Content
  slot. The wrapper provides token-styled background and padding; the slot
  content renders inside.
- **Card Grid** (`props.Slot({ name: "Cards" })`) — accepts Feature Card Code
  Components in its Cards slot. Three Feature Cards render in a responsive
  3-column grid layout with token-controlled gap spacing.

**Key nuance:** Slot children are native Webflow elements that render in the
host DOM, not inside the Code Component's Shadow DOM. The slot is a projection
point — the component controls layout around the slot, and the children follow
the host site's styles (including Client-First classes).

This means designers get the best of both worlds: Code Component structure and
token styling for the wrapper, plus full Webflow design control over slot content.

## Finding 9: CMS Binding Works with Code Component Props

**Confirmed.** Code Component props (`props.Text`, `props.Image`, `props.Link`)
can be bound to CMS Collection fields in the Webflow Designer.

Tested on the CMS Test page:
- Created a **Team Members** CMS Collection with fields: Photo (Image),
  Role (Plain Text), Bio (Plain Text), LinkedIn (Link)
- Placed a **Team Member** Code Component inside a Collection List
- Bound each prop to its matching CMS field:
  - `props.Image` → Image field (Photo)
  - `props.Text` → Plain Text fields (Name, Role, Bio)
  - `props.Link` → Link field (LinkedIn)

All bindings connected successfully. The Code Component renders CMS data from
the collection, and each instance in the Collection List pulls its own item data.

**Implication:** Code Components are first-class citizens in Webflow's CMS
workflow. Designers can build Collection pages using Code Components exactly
like native elements — bind fields in the Designer UI, no code changes needed.
Combined with CF 3.0 tokens, a single component library can serve CMS-driven
pages across multiple sites.

## Open Questions (Not Yet Tested)

| Question | Status | Plan |
|----------|--------|------|
| Do Variable Modes (light/dark) work through Shadow DOM? | UNTESTED | Add modes to test site, verify |
| Do responsive variable values work through Shadow DOM? | UNTESTED | Set breakpoint values, verify |
| Does `applyTagSelectors: true` interact with tokens? | UNTESTED | Toggle on Hero, observe |
| Can a component mix tokens + tag selectors? | UNTESTED | Test in Checkpoint 3 |
| What is the performance cost of 42 inheriting variables? | UNMEASURED | Lighthouse before/after |
| Does publishing the site affect token inheritance? | UNTESTED | Publish and verify on live domain |

## Implications for Agencies

1. **New project setup** gains one step: define 42 tokens in the Variables
   panel (automatable via MCP/API)
2. **Code Component libraries** become portable across any CF 3.0 site
   without per-site CSS customization
3. **Theming** (light/dark, brand variants) should work via Variable Modes
   with zero component changes (needs verification)
4. **AI-generated components** only need to know the Token Manifest to produce
   CF 3.0-compliant output
5. **The class system stays** for native Webflow elements — CF 3.0 is
   additive, not a replacement
