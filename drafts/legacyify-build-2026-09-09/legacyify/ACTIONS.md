# Your three Legacyify actions

Use these in Codex with the included [portable skill](workflow/legacyify-skill/SKILL.md). You can simply ask Codex to read that file, attach an image, and name an action. The original canonical masters are in `sources/`; no need to attach them again when this folder is accessible.

## 1. Legacyify Character

**Give it:** one clear full-body human pose or one canonical character image, plus which canonical character to use.

**Say:** “Legacyify Character. Use this image for pose and framing only; use the male [or female] master for identity, body proportions, black outfit and illustrated rendering. Preserve the master’s blunt fingertips. One request, one raw image. Show the result before explaining.”

**Demonstrated:** C04 transfers the human gesture without inheriting the human face, blue shirt, brown shoes or narrower build. C02 shows the female character in a new folded-arm pose. Fine face and hair geometry still varies. Familiar angles and visible faces are the best fit; extreme views, heavy face occlusion and intricate hand interactions need development.

C04 is a disclosed development revision of C03, which invented dark pointed claws. Each was a separate one-call invocation from original references. The first result remains in the record.

## 2. Legacyify Scene

**Give it:** one readable scene with a few important structures or objects.

**Say:** “Legacyify Scene in pixel art. Preserve the camera, spatial story, salient object shapes/counts and lighting direction. Inspect and name fragile features before generating. Use deliberate pixel clusters with restrained Legacy warm/cool contrast. Style-only; no added branding. One request, one raw image.”

**Demonstrated:** S03 retains the alpine pavilion, round lamp, bench, lake, red canoe and gentle central descent. S01 shows a separate office transformation. This is perceptual composition retention, not exact geometric registration. Micro-contours, texture and lighting detail can vary; exact tiny text, logos and a verified native pixel grid are outside the supported claim.

S03 is a disclosed revision of S02, whose lamp became rectangular and whose path/geometry drifted. The medium is part of the action: an exact logo redrawn in pixels cannot be assumed to retain literal master geometry.

## 3. Legacyify Together

**Give it:** a scene with enough visible space to place one character, and choose the male or female master.

**Say:** “Legacyify Together. Add the canonical female [or male] character here, preserving the supplied environment medium. Keep the character illustrated and match scale, perspective, lighting, contact, occlusion and shadows. No added branding. One request, one raw image. Show the result first.”

**Demonstrated:** T01 seats the illustrated lioness convincingly in the rendered office; T02 inserts the male into the outdoor source. T03 explores two distinct characters together, with coherent grounding. T01's main emblem differs from the required logo master. T02 did not establish its additionally requested CGI conversion. T03's characters are larger than specified. These misses remain recorded; the final fresh-scene default explicitly preserves the existing environmental medium instead of promising a new CGI conversion.

Start with simple placement and a familiar view. Two separated characters worked in one exploratory example. Touching characters, mirrors, complex seated interactions, exact frame-relative sizing and unseen-angle invention are not stabilized.

## What the action does internally

Codex inspects the references, verifies source roles, writes a short set of consequential/perceptual/incidental constraints, chooses a medium, and makes one image call. It saves the original bytes and records the outcome. Any development revision is a new numbered invocation; it is never a hidden repair or retry inside an action. The local helper prepares packets and records provenance; it does not generate independently.

For exact replay, use `records/ACTUAL_TOOL_CALLS.json` or the corrected `attempts/*-execution/packet/packet.json` records. Supply the original sources in their recorded order. Outputs are stochastic: the same request is not guaranteed to produce the same pixels or quality.

## Recommended three-image set

For a live demonstration, choose a clear pose photo, a scene you want stylized, and an environment you want a character to inhabit. The included development set is `DEVELOPMENT_HUMAN_POSE.png`, `DEVELOPMENT_ALPINE_TERRACE.png`, and `LEGACY_OFFICE_MASTER.jpg`. The first two are explicitly synthetic setup images. Fresh user photographs would be the next useful test of transfer.
