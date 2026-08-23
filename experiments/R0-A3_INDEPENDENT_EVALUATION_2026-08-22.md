# R0-A3 CGI Legibility Under Geometry Lock — Independent Evaluation

**Status:** `FINAL FAIL` — ACCEPTED BY NATE; NO CORRECTION  
**Evaluation date:** 2026-08-22  
**Controlling packet:** `experiments/R0-A3_CGI_LEGIBILITY_UNDER_GEOMETRY_LOCK_FROZEN_2026-08-22.md`

## Scope and authority

Evaluation used the exact untouched Oslo source and the three independently preserved isolated direct-edit outputs. No generated descendant was treated as authority, and no correction or generation occurred during Evaluation.

### Exact source

- Filename: `G1-A_HOLDOUT_OSLO_OPERA_HOUSE_BASE_SOURCE_INTERNAL_VALIDATION_2026-08-20.jpg`
- Drive ID: `1hcaY5KRnVWCbmBHb1O_jwj-oNHp9a8ZR`
- SHA-256: `f2445f76358774a363ad9a4783b4b3c196f561e8f2a040b94dbcf5b19c174b75`
- Raster: `5520 × 3680` JPEG

### Evaluated outputs

| Run | Drive file | Drive ID | SHA-256 | Raster |
|---|---|---|---|---:|
| 2 | `R0-A3_ISOLATED_EDIT_RUN2_RAW_2026-08-22.jpg` | `1KgKckWspjmemiPnh_3ZuoNjSX0Xk5Hbj` | `1f48aa16a956082ec545a878ba6e4413fb175e9990c4a2e79876427a5a3d3b98` | `1536 × 1024` |
| 3 | `R0-A3_ISOLATED_EDIT_RUN3_RAW_2026-08-22.jpg` | `1a-bCCvfw5aQKsiXMGQ3zyt5suVRGsvWf` | `8e49ba1add54b6e7c6771857310d4f76b8c8b354ee4e5c86fd6cc81e43465cd7` | `1536 × 1024` |
| 4 | `R0-A3_ISOLATED_EDIT_RUN4_RAW_2026-08-22.jpg` | `1HFzmi_nqjyQ65LnXq4NuuhX-4dAmfDUs` | `2805a0705579e84330a017058e038ade932318ad0055fe7fe74f715778bed964` | `1537 × 1023` |

Run 1 was not used to qualify repeatability because its recorded supplied hash does not match either the exact conversation PNG or the requested JPEG preservation encoding. It remains preserved with the discrepancy documented in Drive run record `R0-A3_LABORATORY_RUN_RECORD_2026-08-22.md`, ID `1Ozh7KmZJiyxO3x7tBrvk8OywnPAwAfau`.

## Direct visual observations

- Runs 2–4 are extremely similar to one another. The direct-edit route is producing a stable behavior distribution.
- The Opera House massing, camera, horizon, principal roof diagonals, ramps, plaza, glass volume, and broad skyline remain substantially aligned with the source.
- All three outputs still read primarily as processed, sharpened, high-dynamic-range architectural photographs rather than unmistakably authored premium CGI.
- Stone retains photo-derived irregularity instead of a deliberately constructed PBR finish. Glass reflections, refractions, and interior light remain largely photographic rather than cleanly rendered.
- The original relatively flat overcast sky is reconstructed into more dramatic and higher-contrast cloud texture. Frozen cloud structure is not held.
- Small people, distant structures, facade divisions, paving joins, and crane/background detail are simplified or shifted rather than held exactly.
- Tonal amplitude varies across the set: Run 2 is brighter, Run 4 is darker/cooler, and Run 3 lies between them.
- Run 4 has separate near-ratio raster quantization (`1537 × 1023`). This is recorded as output-format inconsistency, not automatically conflated with perceptual crop or frame drift.

## Gate results

| Gate | Run 2 | Run 3 | Run 4 |
|---|---:|---:|---:|
| Exact source retrieval and descendant isolation | PASS | PASS | PASS |
| Gross composition, camera, horizon, and architectural identity | PASS | PASS | PASS |
| Frozen object-boundary, people, and secondary-detail lock | FAIL | FAIL | FAIL |
| Frozen weather and cloud-mass preservation | FAIL | FAIL | FAIL |
| Existing major luminance organization retained without new dramatic treatment | FAIL | FAIL | FAIL |
| Unmistakable deliberately authored premium-CGI legibility | FAIL | FAIL | FAIL |
| PBR material response, clean render optics, and coherent synthetic finish | FAIL | FAIL | FAIL |
| No unauthorized reconstruction or reinterpretation | FAIL | FAIL | FAIL |
| Output-format consistency | PASS | PASS | FAIL |
| Release-level result under the frozen success condition | FAIL | FAIL | FAIL |

## Classification and correction eligibility

- Run 2: `FINAL FAIL`
- Run 3: `FINAL FAIL`
- Run 4: `FINAL FAIL`
- Distribution: `FINAL FAIL`
- Correction eligibility: **not one-edit eligible**

The distribution contains multiple independent defect families: modality underconversion; secondary-scene reconstruction involving sky, people, and fine structure; tonal instability; and one output-format inconsistency. Repair would require another global reconstruction rather than one bounded edit that preserves unrelated successes.

## Stabilization finding

R0-A3 demonstrates repeatable **photo-enhancement behavior**, not repeatable premium-CGI conversion. The route consistently prioritizes recognizable source preservation while remaining inside a photographic rendering basin, then regenerates unconstrained fine detail.

Record the recurrent failure class as:

> `MODALITY_UNDERCONVERSION + SECONDARY_SCENE_RECONSTRUCTION`

This advances failure predictability but does not establish repeatable excellence, within-Legacy transfer, or production qualification.

## Authorized next direction

Retire R0-A3 uncorrected. Design a new experiment that changes one rendering-control mechanism: add an explicitly bounded, non-descendant, brand-neutral premium-exterior-CGI rendering-language authority while keeping the untouched Oslo source as the exclusive authority for scene geometry, composition, camera, weather state, object placement, and lighting organization.

The style candidate must remain unverified intake until Nate explicitly promotes its exact bytes for this narrow experimental jurisdiction. It receives no canonical, scene, brand, or production authority.
