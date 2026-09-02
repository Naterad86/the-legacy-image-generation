# R0-A4 Independent Evaluation Report

**Evaluation date:** 2026-09-02 (UTC)  
**Scope:** R0-A4 only  
**Controlling authority:** `experiments/R0-A4_TOOL_COMPATIBILITY_SUPERSESSION_FROZEN_2026-08-22.md` from branch `main` of `Naterad86/the-legacy-image-generation`  
**Evaluation mode:** independent, excellence-only, no correction  
**Final classification:** `FINAL FAIL`

## 1. Controlling-packet verification

The controlling frozen packet was retrieved read-only from the exact repository path and branch specified above.

- GitHub blob SHA: `f65ea03253c17c0b00c55a238520715c9268f9ff`
- Packet status: `FROZEN — SUPERSEDES THE 2026-08-22 R0-A4 PACKET AND HANDOFF`
- Governing decision rule: any failed gate is `FINAL FAIL`
- Correction boundary: no repair, rerun, reinterpretation, expansion, or correction is authorized

Only the packet's preregistered ten-gate rubric and primary failure-label taxonomy were applied.

## 2. Evaluation-input and authority-chain verification

All four governed image inputs were retrieved read-only from their exact Google Drive IDs. The byte counts and SHA-256 digests below were computed from the complete Drive-returned bytes, not from previews, thumbnails, screenshots, re-uploads, or substitutes.

| Role | Exact file and Drive ID | Verified technical identity | Result |
| --- | --- | --- | --- |
| Sole upstream scene authority | `G1-A_HOLDOUT_OSLO_OPERA_HOUSE_BASE_SOURCE_INTERNAL_VALIDATION_2026-08-20.jpg`; Drive ID `1hcaY5KRnVWCbmBHb1O_jwj-oNHp9a8ZR` | `image/jpeg`; 5,730,585 bytes; SHA-256 `f2445f76358774a363ad9a4783b4b3c196f561e8f2a040b94dbcf5b19c174b75`; MPO/MPF container evidence present; controlling primary raster `5520 × 3680`; secondary raster `1632 × 1080` | Exact match |
| Authorized tool-ingestion surrogate only | `R0-A4_OSLO_PRIMARY_FRAME_STANDARD_JPEG_TOOL_COMPATIBILITY_DERIVATIVE_2026-08-22.jpg`; Drive ID `1fQ6S66VVsHMIVyZH2LoOvYnbeqh8s7p9` | `image/jpeg`; 5,289,110 bytes; SHA-256 `0588f3111c38e256520e16bff7059fbd956fe0a47c4f77ddd2821dd961493fd3`; standard JPEG with no MPF index or secondary `1632 × 1080` frame; primary raster `5520 × 3680` | Exact match |
| Rendering-language authority only | `R0-A4_CGI_RENDER_LANGUAGE_REFERENCE_CANDIDATE_02_2026-08-22.png`; Drive ID `1Idru5AaH9fZZXHqseoYJ715apXzJrlnG` | `image/png`; 1,731,851 bytes; SHA-256 `2d244885b74d90953cea7a9fe3f62c3c6c8148610ccce3aae06577d47c6c8d9e`; raster `1448 × 1086` | Exact match |
| Preserved raw R0-A4 output | `R0-A4_TOOL_COMPATIBLE_LAB_RAW_OUTPUT_2026-09-02.png`; Drive ID `1Q6kHAt4Pb7ZI--UNERo3l6Pd6AKFTgNO` | `image/png`; 2,295,807 bytes; SHA-256 `fc1dec074dab05d0274fca95d4975ab69a3899ea0c8b66e21cdf8ddc1c079250`; raster `1536 × 1024` | Exact match |

### Authority chain

1. The original Oslo MPO remains the sole authority for scene, frame, camera, geometry, objects, people, cranes, weather, clouds, illumination, luminance, and spatial relationships.
2. The standard-JPEG surrogate is authorized only as the tool-ingestion representation of the original primary frame. Matching the frozen packet's exact surrogate hash grounds the packet-recorded pixel-equivalence chain; it does not confer new scene authority.
3. Candidate 02 controls rendering language only. It has no authority over scene content, geometry, camera, composition, crop, palette, weather, clouds, light placement, objects, people, cranes, or narrative content.
4. The exact Drive-stored raw PNG is the sole R0-A4 output evaluated. It carries no authority over the inputs or rubric.

**Input-integrity conclusion:** PASS. The evaluation set and authority chain are intact.

## 3. Gate-by-gate evaluation

Observations below describe visible or technical evidence. Interpretations apply only the corresponding preregistered gate.

| Gate | Observation | Rubric interpretation | Finding |
| --- | --- | --- | --- |
| 1. Exact input and authority-chain integrity | Every governed file matched its exact Drive ID, filename, MIME type, byte count, SHA-256, and listed raster/container role. The frozen packet was retrieved from `main` at the exact path. | No substitution or authority-role collapse occurred. | **PASS** |
| 2. Frame and 3:2 perceptual retention | The output is `1536 × 1024`, exactly 3:2. It retains the Oslo scene's broad left-to-right extent, sky, principal building, sloping roof/ramp system, and foreground plaza within a single frame. | The complete perceptual frame and aspect relationship remain recognizable. | **PASS** |
| 3. Camera and major-geometry retention | The principal viewpoint, horizon logic, converging plaza lines, Opera House scale, main glass volume, roof diagonals, left slope, and right ramp remain broadly aligned with the upstream scene. | Major camera and architectural geometry remain sufficiently retained at the rubric's major-structure level. Secondary-state failures are assessed separately below. | **PASS** |
| 4. Secondary scene-state retention, including people and cranes | The original foreground-right people are partially edge-bound and larger; the output reconstructs them as a smaller, fully visible group moved materially inward and left. Other people are altered in scale, pose, or placement. Crane booms and crane distribution/count are not retained exactly; several are moved, rescaled, simplified, or omitted. | People and cranes were not held in count/presence/position/approximate pose/scale. | **FAIL** |
| 5. Weather, clouds, illumination direction, and luminance retention | The source has a dark, low-contrast gray overcast field and subdued overall luminance. The output introduces a much brighter, opened cloudscape with a strong high-key region above the building, brighter stone, stronger glass highlights, and a substantially lighter plaza. Cloud masses and major luminance organization are visibly reorganized. | Weather/cloud and luminance locks were not retained. | **FAIL** |
| 6. Unmistakable premium architectural-CGI legibility | The output is cleaner, brighter, and more polished than the source, but it retains photographic atmospheric behavior, human/crane treatment, glass response, and an HDR-like architectural-photo appearance. At ordinary viewing scale it can plausibly be read as a heavily enhanced photograph. | The result does not unmistakably escape the photo-enhancement basin into deliberately authored premium architectural CGI. | **FAIL** |
| 7. Coherent PBR materials, roughness, reflections/refractions, GI, edge treatment, and microdetail | Pale stone and paving gain pronounced synthetic-looking veining and sharpness, but the treatment is not consistently controlled: foreground texture is conspicuous and repetitive, glass response remains unevenly photographic, and the material/lighting system does not cohere to Candidate 02's restrained premium-render finish. | Some CGI cues strengthened, but the full PBR/coherence gate is not met at an excellence-only threshold. | **FAIL** |
| 8. No Candidate 02 scene/content leakage | Candidate 02 has a pale high-key palette and bright diffuse cloud field. The output shifts the source toward a similarly bright sky, opened cloud structure, and high-key neutral luminance despite Candidate 02 having no authority over palette, sky, clouds, or light placement. No clear transfer of Candidate 02's building design is observed. | The unauthorized sky/palette/luminance shift is consistent with rendering-reference leakage into excluded scene-state properties. | **FAIL** |
| 9. No added logos, text, motifs, characters, labels, borders, or panels | The output is one image with no border or panel structure. No clear new logo, label, motif, character, or unrelated text is visible. Existing architectural/signage detail is not treated as a newly added element. | No prohibited addition is established. | **PASS** |
| 10. Release-level coherence without local artifacts or secondary reconstruction | The main scene is visually coherent at a glance, but the people and cranes are visibly reconstructed, including relocation/rescaling of the foreground-right group and altered crane geometry/distribution. | The gate expressly requires absence of secondary reconstruction; that condition is not met. | **FAIL** |

## 4. Final classification

`FINAL FAIL`

The output fails gates 4, 5, 6, 7, 8, and 10. Under the frozen packet's excellence-only decision rule, any one failed gate requires `FINAL FAIL`.

## 5. Applicable preregistered failure labels

- `SECONDARY_SCENE_RECONSTRUCTION`
  - People and cranes were moved, rescaled, simplified, omitted, or reconstructed rather than held.
- `WEATHER_LUMINANCE_DRIFT`
  - The dark overcast source state shifted to a substantially brighter cloudscape and high-key material/luminance organization.
- `REFERENCE_INSUFFICIENT_TO_ESCAPE_PHOTO_BASIN`
  - The result remains plausibly readable as an enhanced architectural photograph rather than unmistakable premium CGI.
- `STYLE_AUTHORITY_LEAKAGE`
  - Candidate 02's bright sky/high-key palette and luminance character appear in properties explicitly outside its jurisdiction.

Not applied:

- `GEOMETRY_LOCK_DEGRADATION` — major camera and architectural geometry were broadly retained; the decisive structural failures are in secondary scene state.
- `OUTPUT_INTEGRITY_FAILURE` — the preserved output is the exact, valid single PNG identified by the preservation record; the failure is evaluative, not file-identity or container integrity.

## 6. Concise supporting evidence

The R0-A4 output preserves the broad Oslo composition and exact 3:2 aspect, but it does not preserve the locked secondary scene state or the locked weather/luminance state. The most concrete failures are the relocated/rescaled foreground-right people, altered crane distribution, replacement of the dark gray overcast with a bright opened cloudscape, and the continued plausibility of the image as HDR-style photographic enhancement. These failures independently prevent `EXCELLENT` classification.

## 7. Authorization boundary and hard stop

No image was edited, repaired, regenerated, cropped, re-encoded, or substituted. No retry or alternate output was requested. GitHub and Google Drive were accessed read-only and were not modified. No correction is authorized. Evaluation ends with this report.
