# The Legacy — Rendering Modality Profiles

**Status:** ACTIVE upon merge into `main`  
**Version:** 0.1  
**Decision date:** 2026-08-21

## Purpose

Translate the durable Legacy visual grammar into the native construction rules of a selected medium. The profile is an adapter, not an additional identity source.

Every generation must name the profile for each major component. No profile is inferred from the input file extension or visual appearance.

## `CGI_ENVIRONMENT`

Use for production-facing environments unless another profile is explicitly selected.

- Deliberately authored high-end 3D CGI rather than an untouched or lightly retouched photograph.
- Physically credible materials appropriate to the scene: controlled stone, wood, leather, metal, glass, fabric, vegetation, water, or atmosphere.
- Cinematic light with clear direction, controlled practical illumination, warm highlights, and cool or deep shadows where scene logic supports them.
- High surface detail without random texture noise or procedural clutter.
- Preserve the scene properties identified as held; redesign only the released materials, lighting, atmosphere, and secondary details.
- Avoid the uncanny middle state of a literal photograph carrying pasted synthetic details.

## `ILLUSTRATED_CHARACTER`

Use for Legacy lion or lioness characters when their canonical character masters are invoked.

- Canonical character master alone controls likeness, anatomy, mane or hair, proportions, tail, and established mascot identity.
- Clean, confident curves and immediately readable silhouettes.
- Bold controlled outlines where appropriate; soft cel shading or limited gradients that clearly describe muscle and fur form.
- Adult, powerful, heroic, commercial-mascot presence without unrelated cartoon exaggeration.
- Fitted black clothing and gold accents are permitted variable treatments only when authorized; incidental marks never control identity.
- No sketch lines, muddy texture noise, anatomy inflation, or generic lion substitution.

## `PIXEL_ART`

Use when the intended successor is pixel art.

- Preserve or explicitly choose a native pixel scale, cluster size, edge stair-stepping, palette discipline, and detail frequency before generation.
- Build forms from deliberate pixel clusters; do not trace the emblem with a finer, smoother, anti-aliased vocabulary than the scene.
- Translate lighting, material, and luxury through value grouping, palette relationships, controlled dithering, and silhouette—not through PBR language.
- Canonical topology must survive the medium's resolution; reduce detail deliberately rather than producing accidental simplification.
- No photographic texture, subpixel linework, smooth vector edges, or particle-dense overlays.

## `PAINTERLY`

Use for authored painted or atmospheric scenes.

- Match an explicitly selected brush scale, edge softness, paint texture, value grouping, and detail frequency.
- Express form through brushwork, mass, light, and atmosphere rather than graphic overlay.
- Scene-native atmospheric embodiments may soften modestly while preserving the emblem's defining topology and negative spaces.
- Do not render the motif at a sharper or more graphic resolution than the surrounding painting.

## `PHOTOGRAPHIC_PRESERVATION`

Use only when Nate explicitly authorizes a validation task whose purpose requires the output to remain photographic.

- Preserve full perceptual frame, camera, scene identity, major geometry, lighting relationships, palette relationships, and photographic rendering vocabulary to the degree frozen by the experiment.
- Introduced elements must match the photograph's material scale, optics, light, depth, and resolution.
- This profile is evidence-producing and does not establish the default production aesthetic.

## `HYBRID_CGI_ILLUSTRATED_CHARACTER`

Use when illustrated canonical characters occupy a rendered CGI environment.

- Apply `CGI_ENVIRONMENT` to the environment and `ILLUSTRATED_CHARACTER` to each character.
- Unify them through camera perspective, contact, occlusion, light direction, cast shadows, local color interaction, edge hierarchy, and comparable finish.
- Do not convert the character master into 3D anatomy merely to match the environment, and do not flatten the environment into character-style cel art merely to match the character.
- Judge integration separately from the fidelity of either component.

## Conflict and fallback rules

- Canonical source authority outranks every profile.
- A base scene controls only the properties explicitly held from it.
- The durable visual grammar outranks optional profile flourishes.
- If one profile rule would erase the intended medium, preserve the medium and express the invariant by native means.
- When profile interaction cannot be resolved without changing an authority boundary, stop for Nate's decision.

