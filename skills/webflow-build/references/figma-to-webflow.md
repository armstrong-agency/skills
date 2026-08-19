# Figma-to-Webflow implementation

Use this workflow when Figma, a Figma node, or a supplied design screenshot is
the approved source for Webflow work. It governs cross-tool implementation
judgment; use the current Figma and Webflow platform guidance for tool
mechanics.

## Preflight the exact targets

Before expensive reads or destination writes:

1. Verify that the intended Figma capability is callable in the current task.
   Configured or authenticated does not prove that a tool loaded successfully.
2. Resolve the approved Figma file, exact node or frame, intended viewport, and
   current source revision when available.
3. Resolve the authorized Webflow connection, site, page, component definition
   or instance, and environment.
4. Record whether the task is read-only, saved-draft implementation, staging
   work, or an explicitly authorized publication.
5. Treat a request not to reload a large file as a retrieval budget, not a
   casual preference.

Fail closed on an unavailable scoped Webflow destination. Do not substitute a
global connection or another project's server.

Keep one active writer for a Webflow destination. Parallelize source research
or read-only inventory when useful, but serialize mutations and read back each
coherent batch before the next writer action.

## Establish source authority

State which evidence is authoritative for each claim:

- Targeted Figma node data can establish structure, text, component identity,
  variants, variables, and measured dimensions.
- A targeted Figma screenshot can establish the visible appearance at its
  captured viewport and state.
- A user-supplied screenshot or export may become the declared visual authority
  when node access is unavailable.
- A screenshot does not prove hidden states, interactions, component
  provenance, variable bindings, or responsive behavior outside its capture.
- A written brief can resolve intent that the visible design does not express.

Do not silently downgrade from node-level evidence to visual approximation.
Report the fallback and the claims it cannot support.

## Read the smallest useful target

Prefer the exact node, relevant component children, and targeted screenshots
over the root of a large file. After resolving a component, retain a compact
evidence record so it does not need to be loaded again without cause.

Use a ledger like:

| Requirement | Design evidence | Webflow candidate | Decision | Verification |
| --- | --- | --- | --- | --- |
| Section or atom | Node and viewport | Component, class, token, asset | Reuse, configure, duplicate, change, or create | Persisted, canvas, runtime |

Record copy, dimensions, typography, spacing, color, border, radius, assets,
responsive expectations, and states only to the degree the source proves them.

## Calibrate raster screenshots

Do not translate raster pixels directly into CSS values until the capture scale
is established.

1. Record the raster dimensions and, when available, the Figma frame
   dimensions or device scale.
2. Test a possible scale against at least two independent anchors, such as
   frame width, a known typography token, a known icon size, or an established
   corner radius.
3. Use `CSS pixels = raster pixels / capture scale` only after those anchors
   agree.
4. Mark any remaining value as estimated rather than exact.

Do not assume every high-density screenshot is exactly 2x.

## Map the design into the approved system

Inventory existing component definitions and instances, properties, variants,
slots, classes, variables and modes, responsive rules, interactions, assets,
and nearby approved implementations before creating anything.

A familiar name is only a candidate. Inspect the actual responsibility,
declarations, breakpoints, consumers, and behavioral contract. Reuse when those
match the target; leave a legacy near-match untouched when changing it could
affect unrelated consumers.

For common design-system parts such as Button, Label, card, icon, typography,
spacing, radius, and color:

- reuse the actual component, supported variant, token, or asset;
- do not recreate the visual appearance from raw elements;
- verify the active variable mode and computed value;
- preserve supplied copy exactly unless editing was requested;
- avoid uploading an asset that already exists in the destination library.

## Use named source components as real starting points

When the brief says to start from an existing component:

1. Record the exact design target and the proposed source component.
2. Confirm their structural responsibilities match, not merely their visible
   appearance.
3. Follow the derivative-component workflow in the main Designer skill on an
   approved isolated review page.
4. Compare the source and derivative against the target design and document the
   intentional differences.

## Work component by component

For each coherent component:

1. Compare structure, semantics, and reading order.
2. Compare copy and content hierarchy.
3. Verify actual component usage and supported properties or variants.
4. Compare typography and wrapping.
5. Compare spacing, sizing, alignment, and layout.
6. Compare borders, radii, fills, and assets.
7. Check relevant default, hover, focus, active, selected, open, and disabled
   states.
8. Check the established breakpoints and mobile collapse order.
9. Persist the change and read back the definition and representative instance.
10. Inspect Designer canvas and Preview/runtime as required before continuing.

This prevents a full page from accumulating small fidelity errors that become
expensive to isolate later.

## Fallback and handoff

If Figma tooling is unavailable:

- do not repeatedly reopen a massive file through a slower browser fallback;
- use an already-loaded targeted node, an approved crop, or a user-supplied
  screenshot when available;
- ask for a more precise export only when the missing evidence would materially
  change the implementation;
- keep hidden states and unsupported breakpoints explicitly unverified.

Report the Figma file or source, exact node when known, capture scale, reused
Webflow pieces, new decisions, exact versus estimated values, QA surfaces, and
anything the available evidence could not prove.
