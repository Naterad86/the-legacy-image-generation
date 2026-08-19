# Closed Source Authority System

The Legacy uses a closed visual-source manifest. Controlled assets may derive identity only from their designated master source.

## Core rule

A source controls only its assigned component. Any other element visible inside that source is incidental and has zero authority over that element elsewhere.

## Canonical jurisdictions

### `LEGACY_LOGO_MASTER` — Level 0

The approved black-and-gold mirrored-lion emblem reading THE LEGACY is the sole authority for every Legacy logo. Preserve its lion artwork, geometry, typography, proportions, and composition. Never derive it from character sheets, office images, descendants, or embedded graphics.

### `MALE_CHARACTER_MASTER` — Level 1

The approved Male Legacy Lion identity sheet is the sole authority for male character likeness: head and facial proportions, muzzle, eyes and brows, ears, mane silhouette, fur presentation, body proportions, athletic build, tail, and established mascot rendering style. Logos, typography, clothing graphics, and brand marks appearing on the sheet are non-authoritative.

### `FEMALE_CHARACTER_MASTER` — Level 1

The exact approved `LEGACY_FEMALE_CHARACTER_MASTER.jpg` in Drive is the sole authority for female character likeness: head and facial proportions, muzzle, eyes and brows, ears, hair/mane silhouette, fur presentation, body proportions, athletic build, tail, and established mascot rendering style. Logos, typography, clothing graphics, and brand marks appearing on the sheet are non-authoritative.

Do not substitute `file_00000000d05481fbae9ead05659bc8f6` or another visually similar file. Resolve the controlling bytes by the Drive ID and SHA-256 recorded in `manifests/SOURCE_MANIFEST.md`.

### `LEGACY_OFFICE_MASTER` — Level 2

The approved office image controls the Legacy workspace archetype, equipment, furniture, general prop inventory, environment, and black/gold design language. Legacy logos, Allstate marks, lion artwork, or other branding appearing inside it do not control brand or mascot identity.

### `ALLSTATE_LOGO_MASTER` — Brand-Locked

When the dedicated approved Allstate source is supplied, it alone controls Allstate logo identity. Allstate graphics appearing incidentally in other Legacy sources have zero logo authority. Do not reconstruct the mark from an incidental reference.

## Conflict resolution

Source jurisdiction outranks similarity, recency, previous generations, and model interpretation. When sources disagree, return completely to the designated master and do not blend competing versions.

A generated image is a descendant, never an identity source, unless Nate explicitly promotes it. Previous posters, edits, and generated images may control composition, pose, placement, scene structure, and requested preserved content, but never override a designated identity master.

## Pre-generation source resolution

Before every generation resolve:

1. **Brand lock** — designated logo master or masters.
2. **Character lock** — male and/or female identity master.
3. **Environment lock** — office master or explicitly requested alternate setting.
4. **Variable layer** — pose, clothing, activity, props, theme, lighting, composition, effects, and other permitted variation.
5. **Exclusions** — incidental, obsolete, unavailable, or unauthorized material that must not influence controlled assets.

If a requested controlled asset lacks an available approved master, stop rather than invent or substitute it.
