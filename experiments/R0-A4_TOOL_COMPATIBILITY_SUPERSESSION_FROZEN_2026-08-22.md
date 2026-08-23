# R0-A4 Tool-Compatibility Supersession — Frozen Packet

**Status:** FROZEN — SUPERSEDES THE 2026-08-22 R0-A4 PACKET AND HANDOFF; GENERATION NOT YET AUTHORIZED  
**Freeze date:** 2026-08-22  
**Experimental generation budget:** exactly one accepted generation request producing at most one output  
**Budget consumed:** zero outputs; zero accepted generation requests  
**Correction budget:** zero

## Supersession scope

This packet supersedes:

- `experiments/R0-A4_STYLE_AUTHORITY_DISCRIMINATION_FROZEN_2026-08-22.md`; and
- `handoffs/R0-A4_ISOLATED_ONE_OUTPUT_LAB_HANDOFF_2026-08-22.md`.

The earlier packet and handoff remain immutable historical records and are non-executable. All R0-A4 scientific controls remain unchanged except the tool-ingestion representation of the Oslo source and the clarified budget rule below.

## Tool-ingestion incident

The first handoff execution verified both exact inputs, then submitted one request. The image endpoint rejected the request before generation because the Oslo source was internally classified as unsupported `mpo` format.

- Incident classification: `TOOL_INGESTION_FAILURE — NO EXPERIMENTAL OUTPUT`
- Standalone output produced: no
- Raw output reference: none
- Preservation record: none required because no output existed
- Evaluation: not started
- Retry or correction: none

The rejected request is infrastructure evidence, not an R0-A4 image result. It does not consume the restored experimental output budget under this supersession.

## Purpose and unchanged hypothesis

Test whether a narrowly governed visual rendering-language authority can move the direct-edit route out of the repeatable photo-enhancement basin established by R0-A3 without weakening the demonstrated Oslo geometry lock.

The experiment succeeds only if one output simultaneously preserves the original Oslo scene and clearly reads as deliberately authored premium architectural CGI rather than a lightly retouched photograph.

## Upstream scene authority — unchanged original

- Role: `R0_A4_BASE_SCENE_AUTHORITY`
- Filename: `G1-A_HOLDOUT_OSLO_OPERA_HOUSE_BASE_SOURCE_INTERNAL_VALIDATION_2026-08-20.jpg`
- Drive ID: `1hcaY5KRnVWCbmBHb1O_jwj-oNHp9a8ZR`
- SHA-256: `f2445f76358774a363ad9a4783b4b3c196f561e8f2a040b94dbcf5b19c174b75`
- Drive MIME type: `image/jpeg`
- Byte size: `5,730,585`
- Primary raster: `5520 × 3680`
- Internal container: MPO with two frames (`5520 × 3680` primary; `1632 × 1080` secondary)

The original exact bytes remain the sole upstream authority for frame, camera, lens behavior, crop, viewpoint, perspective, horizon, architecture, ramps, plaza, paving organization, skyline, cranes, people, weather, clouds, illumination direction, major luminance organization, and all spatial relationships. The original MPO must be retrieved for identity verification but must not be attached to the image-generation endpoint.

## Authorized tool-ingestion surrogate

- Role: `R0_A4_BASE_SCENE_TOOL_INGESTION_SURROGATE`
- Filename: `R0-A4_OSLO_PRIMARY_FRAME_STANDARD_JPEG_TOOL_COMPATIBILITY_DERIVATIVE_2026-08-22.jpg`
- Drive ID: `1fQ6S66VVsHMIVyZH2LoOvYnbeqh8s7p9`
- SHA-256: `0588f3111c38e256520e16bff7059fbd956fe0a47c4f77ddd2821dd961493fd3`
- MIME type: `image/jpeg`
- Byte size: `5,289,110`
- Raster: `5520 × 3680`
- Container: standard single-frame baseline JPEG

Nate explicitly authorized this derivative only as the R0-A4 tool-ingestion representation of the original primary frame. It is not a new scene authority, canonical master, production asset, independent source, or general-purpose replacement.

### Extraction and equivalence verification

The derivative was created without decoding, pixel editing, or JPEG recompression:

- removed one `4,096`-byte MPF `APP2` index at original offset `67,586`;
- copied the original primary JPEG header segments other than the MPF index;
- copied the original primary entropy-coded scan through its EOI marker unchanged;
- discarded the `437,379`-byte MPO secondary-frame trailer after the primary EOI;
- original and derivative primary-scan SHA-256: `f5ae39ffb17d98677b8522deb81bcfab4e8a2cc9a39af30102793dd9787c1491`;
- original primary-frame and derivative decoded-RGB SHA-256: `ffdf8f70240804d3e8a9c2b1b24f3d9760d2a66b4ddcdb47cc0e015364d33985`;
- decoded pixel comparison: zero differing pixels; maximum channel delta `0`;
- original parser result: `MpoImageFile`, `MPO`, two frames;
- derivative parser result: `JpegImageFile`, `JPEG`, one frame.

This is a container-normalization derivative with identical primary-frame pixels and unchanged compressed primary image data.

## Rendering-language authority — unchanged

- Role: `R0_A4_CGI_RENDER_LANGUAGE_REFERENCE`
- Filename: `R0-A4_CGI_RENDER_LANGUAGE_REFERENCE_CANDIDATE_02_2026-08-22.png`
- Drive ID: `1Idru5AaH9fZZXHqseoYJ715apXzJrlnG`
- SHA-256: `2d244885b74d90953cea7a9fe3f62c3c6c8148610ccce3aae06577d47c6c8d9e`
- MIME type: `image/png`
- Raster: `1448 × 1086`
- File size: `1,731,851` bytes
- Jurisdiction: rendering language only

Candidate 02 may control only premium architectural-CGI legibility, PBR material vocabulary for pale stone/glass/metal/concrete, ray-traced reflection/refraction character, controlled roughness, coherent GI, crisp anti-aliased edges, synthetic surface microdetail, and polished architectural-visualization finish.

Candidate 02 controls no scene content, design, geometry, camera, composition, crop, aspect ratio, viewpoint, palette, weather, clouds, light placement, illumination direction, objects, people, cranes, landscaping, typography, logos, motifs, brands, or narrative content.

Candidate 01 and the five canonical Legacy source masters remain outside this experiment and must not be retrieved, attached, or used.

## Single superseding mechanism change

Image generation receives the verified standard-JPEG surrogate instead of the unsupported original MPO container. The visible primary scene, pixels, compressed primary scan, style reference, prompt, held constants, evaluation gates, and correction boundary remain unchanged.

## Exact Laboratory instruction

Attach exactly two images to the generation call in this order:

1. the verified standard-JPEG surrogate as Image 1;
2. Candidate 02 as Image 2.

Submit this instruction once, unchanged:

> Use Image 1 as the edit target and exclusive authority for the visible scene. Image 1 is the verified, pixel-identical tool-ingestion surrogate of the controlling Oslo primary frame. Use Image 2 only as the rendering-language reference.
>
> Edit Image 1 in place. Preserve the complete frame and 3:2 relationship; camera and lens behavior; perspective, horizon, crop, and viewpoint; every major architectural edge and object boundary; Opera House position, scale, silhouette, roof diagonals, glass volumes, facade divisions, and ramps; plaza extent, slopes, stone-plane boundaries, and paving organization; skyline and background buildings; crane and people count, presence, position, approximate pose, and scale; overcast weather and existing cloud masses; illumination direction and major luminance organization; and every major spatial relationship. Do not add, remove, move, enlarge, reduce, redesign, reconstruct, or reinterpret any scene element.
>
> Transfer from Image 2 only its deliberately authored premium-CGI render language: procedural PBR construction for pale stone, glass, metal, and concrete; controlled roughness; clean ray-traced reflections and refractions; coherent global illumination; crisp anti-aliased edges; synthetic surface microdetail; and polished architectural-visualization finish. Do not transfer Image 2's building design, geometry, camera, composition, crop, aspect ratio, viewpoint, palette, light placement, sky, clouds, objects, landscaping, empty-scene population, or any other content. Image 2 does not authorize removing Image 1's people or cranes or simplifying Image 1 detail.
>
> The result must remain Image 1's exact Oslo scene, now rendered in Image 2's CGI construction vocabulary. Keep Image 1's overcast weather, cloud masses, illumination direction, and major luminance organization. The result must clearly read as deliberately authored premium architectural CGI, not a photograph or lightly retouched photo. Add no logos, text, motifs, characters, labels, borders, or multiple panels. Return one image only.

## Held constants and exclusions

- Original MPO remains upstream scene authority; the surrogate supplies identical primary-frame pixels to the tool.
- Direct image-edit route remains fixed.
- Complete perceptual frame and 3:2 relationship remain fixed.
- All Oslo scene, geometry, object, weather, cloud, illumination, luminance, and spatial locks remain fixed.
- Rendering-language jurisdiction of Candidate 02 remains fixed.
- No Legacy or Allstate sources, logos, characters, branding, text, or motifs.
- No R0 descendant as input.
- No prompt correction, intermediate steering, selection loop, descendant editing, or alternate output.

Released property: rendering modality and render/surface finish only.

## Cycle and budget rule

1. Use a fresh non-project ChatGPT Work conversation.
2. Retrieve and verify the original authority, authorized surrogate, and Candidate 02 by exact IDs and hashes.
3. Confirm locally before submission that the surrogate is a single-frame standard JPEG at `5520 × 3680`.
4. Attach only the surrogate and Candidate 02 to the generation endpoint.
5. Submit the frozen instruction once with no modification or steering.
6. If accepted, preserve the one raw output without editing or re-encoding and hard-stop before Evaluation.
7. If rejected before generation, record `TOOL_INGESTION_FAILURE — NO EXPERIMENTAL OUTPUT` and hard-stop. No retry is authorized inside this packet.

The restored budget is one accepted request producing at most one output. The earlier rejected MPO request remains recorded but consumed no experimental output. This supersession authorizes no generation by itself.

## Preregistered evaluation rubric

The independent evaluator must retrieve the original authority, surrogate, Candidate 02, one raw output, and this packet. Evaluation remains excellence-only:

1. exact input and authority-chain integrity;
2. frame and 3:2 perceptual retention;
3. camera and major-geometry retention;
4. secondary scene-state retention, including people and cranes;
5. weather, clouds, illumination direction, and luminance retention;
6. unmistakable premium architectural-CGI legibility;
7. coherent PBR materials, roughness, reflections/refractions, GI, edge treatment, and microdetail;
8. no Candidate 02 scene/content leakage;
9. no added logos, text, motifs, characters, labels, borders, or panels;
10. release-level coherence without local artifacts or secondary reconstruction.

Classification is `EXCELLENT` or `FINAL FAIL`. Primary failure labels remain:

- `STYLE_AUTHORITY_LEAKAGE`
- `REFERENCE_INSUFFICIENT_TO_ESCAPE_PHOTO_BASIN`
- `GEOMETRY_LOCK_DEGRADATION`
- `SECONDARY_SCENE_RECONSTRUCTION`
- `WEATHER_LUMINANCE_DRIFT`
- `OUTPUT_INTEGRITY_FAILURE`

No correction is authorized.

## Decision rules and blinded Evaluation handoff

- Advance only if the output is independently classified `EXCELLENT` and Nate accepts it.
- Any failed gate is `FINAL FAIL` under this excellence-only preflight.
- Do not repair, rerun, reinterpret, or expand R0-A4.
- A successful preflight validates only this bounded mechanism instance.

After Laboratory preservation and hard stop, a separate fresh Evaluation context receives only this supersession packet, exact original authority, exact surrogate, exact Candidate 02, and the raw output/preservation record. Do not provide Laboratory commentary, preferred outcome, or quality claims.

## Hard stop and authorization boundary

This frozen supersession restores the experimental budget to one output but does not authorize generation. A separate instruction from Nate is required. When authorized, exactly one submitted generation request is permitted. No second request, variation, correction, crop, repair, or Evaluation may occur in the Laboratory context.
