# `L0-E` Freeze Candidate — Perspective-Aware Environmental Embodiment

**Status:** FREEZE CANDIDATE — ASSEMBLED FOR NATE REVIEW / NON-EXECUTABLE  
**Design state:** D1–D5 approved  
**Freeze state:** NOT FROZEN  
**Release state:** NOT RELEASED  
**Run state:** NOT AUTHORIZED / NOT STARTED  
**Decision authority:** Nate  
**Approval boundary:** AWAITING NATE D6a FREEZE APPROVAL AND LATER EXPLICIT D6b RUN AUTHORIZATION

This file contains the proposed Laboratory packet and the separate Evaluation handoff in one versioned text artifact. Its sections must be used in separate workstreams. Nothing in this candidate authorizes source attachment, Drive release, Laboratory generation, or Evaluation.

## Experiment definition

**Identifier:** `L0-E` — Perspective-Aware Environmental Embodiment  
**Purpose:** Test whether one complete canonical Legacy emblem shape can repeatably become a scene-native architectural bas-relief while the supplied unbranded environment remains itself.  
**Hypothesis:** The frozen single-surface instruction will produce three outputs that all clear the critical gates, with at least two judged genuinely usable by Nate.  
**Intended variable:** Independent generation stochasticity only.  
**Cycle count:** Three outputs; no replacements.

## Part A — Laboratory Packet

### A1. Execution boundary

This section is inert until Nate explicitly freezes the packet, the frozen release is written to Drive `02 Experiment Packets`, and Nate separately authorizes the Laboratory run.

The Laboratory generates only. It does not receive or record evaluation classifications, advancement conclusions, or repair decisions.

### A2. Exact source resolution

| Laboratory role | Exact file | Drive ID | SHA-256 | Authority in this experiment |
|---|---|---|---|---|
| Reference 1 — `BASE_SCENE_INPUT` | `RC1_LEGACYIFY_BEACH_BASE_SCENE_INPUT_2026-08-19.jpg` | `18kXU-RIZFaDkcSJAy9ifKhf5Y-CZkn9s` | `55514219c109b5768744f9cfa16a14f07f9d7462e39956c0fca9997a1c75b737` | Scene subject, composition, camera, framing, and major objects |
| Reference 2 — `LEGACY_LOGO_MASTER` | `LEGACY_LOGO_MASTER.jpg` | `1bsTHkVg8_pN0E23i_B9NCWsb0WlgDha_` | `68bc3c93ef900e5b3f25e2f7fb1e987661d60f0b6baec93f0ded0bbb841eb76b` | Sole mirrored-lion emblem geometry authority |

Candidates 1–3 and every other visual source are excluded. The logo master does not control the beach environment. The base scene does not control emblem identity.

### A3. Preflight

Before each cycle:

1. Resolve both source files by Drive ID and SHA-256.
2. Confirm that both exact files can be opened and are available as generation source bytes.
3. Open a clean Laboratory context containing only the frozen packet and the two exact sources, mapped in the fixed order above.
4. Confirm that no RC1 candidate, thumbnail, descendant, office master, character master, Allstate master, or incidental logo is present.
5. Confirm the frozen usable-façade envelope `x=82–94%`, `y=15–36%` of the exact original 4:3 canvas, with `(0,0)` at the top-left. Use this same envelope for every façade-inset calculation, and confirm that the canonical emblem aspect ratio can fit by uniform proportional shrinkage.
6. Use the exact prompt below without addition, deletion, paraphrase, verdict language, or cycle-specific correction.
7. If any preflight item fails, stop before generation.

### A4. Exact generation prompt — candidate text

```text
Reference 1 is BASE_SCENE_INPUT and controls the complete scene. Reference 2 is LEGACY_LOGO_MASTER and controls only the mirrored-lion emblem's geometry. Use no wordmark, background, color, or layout from Reference 2.

Make exactly one localized edit to Reference 1. On the broad flat front façade of the rightmost and tallest upper-right high-rise, within the frozen usable-façade envelope x=82–94% and y=15–36% of the exact original canvas measured from the top-left origin, add one façade-native stone/concrete bas-relief of the complete mirrored-lion emblem.

Treat the emblem as one rigid planar unit at its canonical aspect ratio. Apply one whole-unit projective transform matching the façade plane, then give it uniform moderate relief depth. Preserve the master's exact outer contour, bilateral relationship, and principal internal negative spaces. Do not redraw, locally warp, mirror, rearrange, or crop any part.

Center it within the target envelope. Aim for approximately 70% of usable façade height, but shrink proportionally until it remains at least 10% inside every usable façade edge and 5% inside every canvas edge. Margins override scale. Keep the complete emblem visible.

Match the existing façade material and scene illumination. Add only the local highlights, contact shadows, and narrow cast shadows physically caused by the relief. Preserve the original window and balcony grid; existing apertures may interrupt the relief but may not be moved, removed, resized, added, covered by a backing plane, or redesigned.

Make no other edit. Preserve the original full-frame 4:3 composition, camera, scene content, sky and weather, global lighting, and palette. Add no text, secondary motif, backing panel, gold/black treatment, glow, decal, new object, crop, border, or broad redesign. Return one edited image.
```

No PASS, FAIL, drift classification, usability judgment, or advancement instruction appears in the Laboratory prompt.

### A5. Held constants

- exact source bytes and exact prompt;
- original 4:3 framing and perceptual camera position;
- coastline, road, skyline, buildings, terrain, vehicles, people, foreground surfboards, golf bag, and scene identity;
- sole target: broad front-facing façade of the tallest upper-right high-rise, operationalized as the usable-façade envelope `x=82–94%`, `y=15–36%` of the exact original 4:3 canvas with top-left origin; this envelope controls all façade-inset calculations;
- at least 5% canvas clearance and 10% usable-façade inset;
- target scale of approximately 70% usable façade height with shrink-only margin protection;
- canonical mirrored-lion artwork only, no typography, held at canonical aspect ratio;
- one rigid planar emblem, canonical upright and bilateral construction, one whole-unit projective transform, and one uniform moderate-depth extrusion;
- moderate façade-native stone/concrete bas-relief with natural light and shadow;
- the original window and balcony grid remains fixed and readable; existing apertures may interrupt the relief but may not be moved, removed, resized, added, covered by a backing plane, or redesigned;
- original coastal palette outside the target;
- no intentional change outside the target façade.

### A6. Exclusions

- no descendant source or prior candidate in context;
- no typography, secondary logo, stamp, lion fragment, generic arch, sign, or extra branding;
- no black backing field, gold tracing, glow, decal, black-and-gold wash, or palette substitution for shape;
- no sky, cloud, weather, or atmospheric change;
- no independent transformation of either emblem half;
- no new object, crop, camera shift, composition change, or broad redesign;
- no in-cycle correction, prompt stacking, manual logo replacement, or best-of promotion.

### A7. Cycle procedure and hard stop

1. Generate `L0-E-C1` in a one-image call using the exact two local source paths through `referenced_image_paths` in fixed Reference 1/Reference 2 order. Never use recent-image inclusion.
2. Preserve the raw output immediately in Drive `03 Laboratory Evidence` with source IDs, prompt commit, timestamp, and output hash.
3. Clear the candidate from the next generation context; do not use it as a reference.
4. Repeat the same one-image process independently for `L0-E-C2` and `L0-E-C3`, always from the same two authoritative source paths and exact prompt bytes.
5. Stop after `L0-E-C3`.

Any returned image occupies its run slot even if visibly defective. Only a true no-image or tool-execution failure may be retried identically. Do not generate a visual replacement, Candidate 4, repair, crop, or best-of descendant. A wrong source, source blend, descendant contamination, missing source, or changed prompt stops the cycle immediately and does not authorize a replacement.

## Part B — Evaluation Handoff

### B1. Workstream separation

Evaluation receives only:

- this Part B;
- the exact base-scene and logo-master references;
- the three raw outputs, relabeled in randomized order as `A`, `B`, and `C`;
- a blank observation table.

Evaluation does not generate or edit. Part A's hypothesis, run order, and Laboratory notes remain withheld until observations and classifications are locked.

### B2. Evaluation sequence

For each output, compare directly against the exact base scene and exact logo master—not against RC1 Candidates 1–3 or either sibling output.

Observe in this order:

1. source integrity and jurisdiction;
2. perceptual base-scene preservation outside the target façade: minor reconstruction texture noise is observed, while changed framing, object identity/count/position, building massing, sky/weather, or global lighting is a critical defect;
3. motif count, complete containment, canvas clearance, and façade inset;
4. mirrored-lion topology, bilateral relation, profiles, central rise, and major negative spaces;
5. whole-unit perspective coherence and absence of independent half deformation;
6. façade-native material, moderate depth, natural light/shadow, and readable windows/balconies;
7. unauthorized text, logos, palette wash, atmospheric change, new objects, crop, or broad redesign;
8. Nate's independent usability judgment.

Record observation before classification and classification before interpretation.

The original window and balcony apertures are authorized scene-driven interruptions in visible relief material. They are not emblem negative spaces and may not substitute for, reshape, or make the canonical projected topology untraceable.

### B3. Critical gates

An output is `CRITICAL-CLEAR` only when every item below is satisfied:

- exact authorities used with no source contamination;
- exactly one authorized mirrored-lion emblem and no typography;
- complete, untruncated emblem with the required canvas and façade margins;
- recognizable exact outer contour, bilateral relationship, and principal internal negative-space topology carried by shape rather than color;
- canonical aspect ratio and whole-unit perspective placement with no local warp or independently transformed half;
- base scene preserved and no unauthorized addition or redesign;
- approved façade-native bas-relief treatment without a forbidden signboard, backing field, gold trace, glow, or decal treatment.

Failure of any item is `CRITICAL-DEFECT`. A less-than-ideal but compliant material integration is recorded separately as integration drift; it cannot conceal a critical defect.

### B4. Usability judgment

After the critical classification, Nate answers: **“Would I release this candidate as-is within the intended architectural Legacyify scope, without requesting correction to the tested embodiment mechanism?”** Record `USABLE` for yes or `NOT USABLE` for no. Aesthetic appeal cannot override `CRITICAL-DEFECT`.

### B5. Observation table

| Blinded output | Source/base observations | Containment/topology observations | Perspective/material observations | Unauthorized-change observations | Critical class | Nate usability |
|---|---|---|---|---|---|---|
| `A` |  |  |  |  |  |  |
| `B` |  |  |  |  |  |  |
| `C` |  |  |  |  |  |  |

### B6. Distribution interpretation

- `CRITICAL-CLEAR ×3` and `USABLE ≥2/3`: qualifies the distribution for Nate's holdout-transfer decision; advancement is not automatic.
- `CRITICAL-CLEAR ×2`: partial support; no default advancement.
- `CRITICAL-CLEAR ×3` and `USABLE ≤1/3`: controlled but not valuable enough; no holdout advancement.
- `CRITICAL-CLEAR ≤1`: stop this prompt version.
- The same critical-defect category appearing in at least two outputs: repeated critical defect; stop this prompt version.
- Any wrong-master, jurisdiction, source-blending, or descendant-contamination finding stops the cycle irrespective of count.

Nate may advance, revise, repeat, narrow the intended rollout scope, or stop after reviewing the complete distribution. Any revised core prompt creates a new version and requires a complete new three-output calibration from the original base scene.

## Part C — Freeze and Release Record

| Control | Required record | Current state |
|---|---|---|
| D1–D5 design approval | Nate decision log | Complete |
| D6a freeze approval | Nate explicit decision and date | PENDING |
| Frozen GitHub packet | Path, version, commit SHA, prompt hash | PENDING |
| Drive `02 Experiment Packets` release | Filename, Drive ID, SHA-256, Git commit | PENDING |
| Source-byte preflight | IDs, hashes, accessibility | PENDING |
| D6b Laboratory run authorization | Nate explicit decision and date | PENDING |
| Laboratory workspace | Clean-context confirmation | PENDING |

If Nate approves D6a, promote this candidate into a separately named frozen v1 packet tied to its GitHub commit and Drive release. Do not treat this candidate filename as retroactively executable. D6b remains a separate explicit decision after the frozen release is verified.
