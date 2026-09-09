---
name: legacyify-skill
description: Run Legacyify Character, Scene, or Together as source-bound transformations through Codex's built-in image tool, preserving source authority and documenting each one-request result. Use for these Legacy actions and their explicit development revisions.
---

# Legacyify

Deliver the visual demo first and the walkthrough afterward. This is a portable local skill, not an installed integration. It can be invoked by asking Codex to read and use this `SKILL.md`. Keep the surrounding workflow folder when moving it so the optional provenance helper remains available.

## Product contract

The September 7 Legacy direction is one operator action, internal source analysis/routing, **one accepted generation request and one untouched returned image**. Inspect and compile internally, then make one built-in image call. No hidden retries, candidate selection, descendant edits, or external post-production fixes belong inside that invocation. A transparent development campaign may compare separately numbered invocations; do not present its selected best image as measured first-pass reliability.

Use `image_gen.imagegen` only. This skill does not require an API key, install anything, buy services, or silently switch to an API fallback. If the built-in tool fails, record the failure. Another call is a separately identified revision within the user's authorized development scope, or a new requested invocation. Account for every call and returned image. If the tool unexpectedly returns multiple images, preserve and disclose them; do not silently choose one and claim the one-output contract passed.

## Resolve authority before generation

Inspect every local reference with `view_image`. Preserve its original bytes and record its absolute path, SHA256, and dimensions. Resolve canonical sources against the available source manifest; a similar historical output is not a substitute for a master.

| Source | Authority |
|---|---|
| `LEGACY_MALE_CHARACTER_MASTER.jpg` | Male likeness, face/muzzle/eyes/brows/ears/mane/fur, proportions, athletic build, tail, illustrated construction. Embedded marks have no logo authority. |
| `LEGACY_FEMALE_CHARACTER_MASTER.jpg` | Female identity and illustrated construction. Do not import male face, mane, or anatomy. |
| `LEGACY_OFFICE_MASTER.jpg` | Depicted environment and, where requested, abstract dark-luxury art direction. Its furniture, room layout, props, equipment, embedded marks, and photographic appearance do not automatically transfer to another scene. |
| `LEGACY_LOGO_MASTER.jpg` | Sole authority for the mirrored-lion emblem and THE LEGACY typography, geometry, spacing, and negative spaces. |
| `ALLSTATE_LOGO_MASTER.jpg` | Allstate mark only, and only when the requested scene contract calls for it. |

A fresh user image is a new source for its depicted subject or scene. Assign its role explicitly; it is not automatically a canonical master or style authority. When a canonical Legacy character is requested, the canonical master controls identity while a fresh reference may control an explicitly assigned pose, scene, or composition. An attachment without a local path may use the smallest sufficient recent-image count supported by the tool. Never combine that mechanism with `referenced_image_paths`; obtain local bytes for exact hashing if accessible, otherwise disclose that its byte provenance is unverified rather than inventing a hash.

Before the call, save a compact brief covering:

- Input order, exact hashes, each source's role, and which source prevails for each property.
- Source state: focal subject, view/frame, major geometry, salient objects/people, light/weather, text/branding, and relationships.
- Consequential properties that must be correct; perceptually important properties to preserve; incidental properties allowed to vary. Make these decisions before viewing the output.
- Named rendering profile for each component, requested change, and redesign envelope.
- Any requested logo's embodiment form, surface, and count. Prefer one complete contained mark with room to remain legible; do not infer permission to introduce a logo from embedded branding elsewhere.

Freeze the brief and exact prompt for the invocation. Compile in this priority: identity/brand/consequential properties → spatial story and frame → requested change → native medium → finish → exclusions. Keep evaluation reports and protocol language out of the image prompt; request a standalone finished image.

## Route the action

**Character — `ILLUSTRATED_CHARACTER`.** One clear character, familiar view, bounded pose/expression/wardrobe change, visible face. Preserve facial proportions, muzzle, eyes/brows, mane or hair shape, ears, tail, body proportions, species, and character count. Explicitly preserve the master’s restrained blunt fingertips/nails; do not invent dark pointed claws. Use the master’s adult commercial mascot illustration, confident curves, readable silhouette, and controlled shading. Avoid piling extreme pose, new wardrobe, emotion, angle, props, and occlusion into the same initial action. A generic attractive lion fails identity. Exact facial geometry is conditional even where recognizability is strong; extreme view invention, hidden faces, tiny subjects, and multiple interacting characters remain experimental.

For the **supported source-to-pose prototype**, assign the new pose image as `target` and the exact canonical character master as `identity`. Borrow only the target’s declared gesture, joint arrangement, frame, and staging; the master controls the complete character, face, anatomy/proportions, outfit, hands/nails, and illustrated construction. Do not transfer human identity, skin, clothing, or footwear. Use a frozen authored `--prompt-file` that states this jurisdiction explicitly rather than assuming the generic character template resolves it. C03 demonstrated pose transfer and role isolation on a synthetic human reference, while adding unauthorized dark claws and mild facial/mane variation. C04 received practical PASS for source-role isolation, controlled pose transfer, recognizable character continuity, and corrected blunt natural fingertips on both hands. It remains a separately logged revised request: C03's failure is retained, exact facial/mane geometry is unproven, and success does not establish arbitrary photographic-person transfer or correction reliability.

**Scene — one selected profile such as `PIXEL_ART` or `PAINTERLY`.** Lock the source’s scene meaning, camera/frame, major geometry, salient objects, and story-bearing relationships unless explicitly released. Choose pixel cluster/detail scale or brush scale/edge softness before generation. Legacy direction is premium crafted finish, clear hierarchy, warm/cool value contrast, and restrained gold or golden-orange accents where suitable; a black-and-gold wash does not establish medium conversion. Keep native medium behavior coherent. Dense crowds, exact tiny text, intricate architecture, and physically exact reconstruction remain experimental.

**Together — default fresh-scene campaign profile `ILLUSTRATED_CHARACTER_OVER_SOURCE`.** Use a canonical identity reference and a distinct environment authority. Preserve the supplied environment's medium and add the illustrated character. Integrate camera/perspective, scale, feet/contact, occlusion, light direction, shadows, local color, edge hierarchy, and finish without converting either component into the other's medium. Start with one visible character, simple floor contact, a familiar view, and room for placement. Heavy occlusion, mirrors, complicated sitting/hand contact, touching characters, and exact room reconstruction remain experimental. Judge identity, environment fidelity, and integration separately.

Use `HYBRID_CGI_ILLUSTRATED_CHARACTER` when the source environment is already CGI, or when the user explicitly requests a CGI conversion. Preserve the illustrated character in either case. New environment conversion remains experimental and needs its own visible acceptance evidence. T01 supports illustrated-character integration in the existing rendered office. T02 supports insertion and broad scene preservation in the synthetic alpine source, but did not establish its requested CGI conversion and missed the requested approximate character frame fraction. The fresh-scene default is a prospective action refinement: **never retrospectively relabel T02 as passing its original frozen CGI-conversion request.**

The campaign's practical boundaries also include exact emblem shape and salient geometry. S01 and T01 produced recognizable branding but failed the exact canonical emblem-shape gate. Stylization can alter meaningful object geometry despite preserving broad composition. Carry these limits into future briefs and reviews; do not infer a geometry or logo lock from presentation polish.

## Execute, record, show

Use the companion [helper instructions](../README.md) when preparing packets, hashing sources, or recording events. `../legacyify.py prepare --prompt-file PATH` imports the frozen prompt exactly. Image inputs become ordered `referenced_image_paths`. For genuinely new synthetic development setup, use `source_setup` with zero references and omit both image-reference tool arguments. Label that setup as synthetic development material; it is not held-out or real-world transfer evidence.

For exact historical campaign replay, read `../../attempts/<ID>-execution/packet/packet.json` and its `tool_arguments`; `../../attempts/<ID>-execution/prompt-exact.txt` contains the exact transport prompt. The audit chain is `../../records/validated-attempts.jsonl`; [the provenance report](../../records/PROVENANCE_VALIDATION.md) explains its transparent retrospective materialization and the single extra terminal LF in the original authored files. Preserve those originals. Prepare a new attempt ID and ledger entry for any replay call, using the recorded arguments unchanged rather than stripping or appending whitespace. Exact argument replay does not guarantee identical new pixels.

Record `started` immediately before the call, preserve the tool's returned original bytes under a fresh filename, then record execution success/failure/interruption and actual visual review. Use a new attempt ID for every new call. Revisions begin from the original authorities, not a failed generated character used as replacement identity authority. Byte-preserving copies and separate demo layouts are allowed; do not repair the showcased raw image to conceal a failed property.

Before a demo, state the applicable input boundary in one brief sentence. Show the raw result and action name next. Then report both laboratory fidelity (meaningful departures) and practical acceptance (coherent, finished, legible, every consequential property correct). An incidental deviation may pass practical acceptance while remaining visible in fidelity notes. Label behavior demonstrated, conditional, or experimental according to the actual evidence. Exact branding can be a one-request limit; disclose any shape, typography, or containment failure.

Place the walkthrough, source roles, prompts, attempt history, and repeatable instructions after the visuals. Do not claim a universal reliability rate from a changing small sample. For a longer campaign, checkpoint the ledger and a concrete resume plan before any agreed deadline or usage ceiling; carry forward the user's active budget authorization without adding refresh permission.
