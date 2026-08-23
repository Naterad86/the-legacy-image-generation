# Source Intake Register

## Canonical promotion checkpoint — 2026-08-19

Nate supplied five files together and explicitly designated them as the five canonical sources. All five loaded successfully, were visually available for jurisdiction mapping, and passed byte inspection. Because the delivered `.png`-named files contained JPEG bytes, filenames were normalized to `.jpg` without editing pixel content.

| Transport file | Conversation source identifier | Promoted canonical filename | Result |
|---|---|---|---|
| `1380.png` | `file_000000005c90820c8626a969810cdc29` | `LEGACY_MALE_CHARACTER_MASTER.jpg` | Promoted to `01 Canonical Masters` |
| `1381.png` | `file_00000000f36c822fb07fab6494a8d360` | `LEGACY_FEMALE_CHARACTER_MASTER.jpg` | Promoted to `01 Canonical Masters` |
| `1383.jpg` | `file_00000000845c820db77db76f224ad50a` | `ALLSTATE_LOGO_MASTER.jpg` | Promoted to `01 Canonical Masters` |
| `1182.png` | `file_00000000ccb0820c8a6962b8e1c03ab2` | `LEGACY_LOGO_MASTER.jpg` | Promoted to `01 Canonical Masters` |
| `1171.png` | `file_00000000040c822f9211a449b67c453e` | `LEGACY_OFFICE_MASTER.jpg` | Promoted to `01 Canonical Masters` |

Drive IDs, dimensions, MIME types, hashes, and jurisdictions are controlled by `SOURCE_MANIFEST.md`.

## Historical migration incident

| Candidate | Observed state | Authority decision |
|---|---|---|
| `Female Lion Character Identity Sheet.png` in the prior ChatGPT project | Source row remained visible, preview missing, deletion failed in Android and web | Historical unavailable record; no authority in the new system |
| Same-named Library item | File could not be delivered to the migration workspace | Not inspected; no authority |
| `file_00000000d05481fbae9ead05659bc8f6` | Historical visually similar candidate referenced by an older decomposition | Explicitly excluded as a substitute |

The new, functioning `1381.png` upload was independently and explicitly designated by Nate as `FEMALE_CHARACTER_MASTER`. This resolves the operational blocker without asserting that it is byte-identical to the unavailable historical item.

## Rendering-language intake and narrow promotion — 2026-08-22

| Candidate | Drive ID | SHA-256 before upload | Raster | Current decision |
|---|---|---|---:|---|
| `R0-A4_CGI_RENDER_LANGUAGE_REFERENCE_CANDIDATE_01_2026-08-22.png` | `1765ddLeg7b2ef2xR0pKaornrya-4pXCp` | `a5cf68d3a65dfb9a6a623ad09e7f3b23e114e96f1d5159558bda0536c0dd6cb3` | `1536 × 1024` PNG | Preserved in `99 Unverified Intake`; no authority; awaiting Nate's visual review and explicit narrow promotion decision |
| `R0-A4_CGI_RENDER_LANGUAGE_REFERENCE_CANDIDATE_02_2026-08-22.png` | `1Idru5AaH9fZZXHqseoYJ715apXzJrlnG` | `2d244885b74d90953cea7a9fe3f62c3c6c8148610ccce3aae06577d47c6c8d9e` | `1448 × 1086` PNG | Nate explicitly promoted these exact bytes for `R0_A4_CGI_RENDER_LANGUAGE_REFERENCE` only; same Drive ID moved to `02 Experiment Packets`; not canonical or scene authority |

Both candidates are original fictional exterior CGI calibration images and are not derived from the Oslo source or an R0 descendant. Candidate 01 remains unverified and has no authority. Candidate 02 may be used only in R0-A4 and only for the rendering-language jurisdiction fixed by the frozen packet. This promotion does not alter `SOURCE_MANIFEST.md` because Candidate 02 is not a canonical Legacy master.

## R0-A4 tool-ingestion surrogate — 2026-08-22

The exact Oslo source at Drive ID `1hcaY5KRnVWCbmBHb1O_jwj-oNHp9a8ZR` and SHA-256 `f2445f76358774a363ad9a4783b4b3c196f561e8f2a040b94dbcf5b19c174b75` is internally an MPO with two frames despite its `.jpg` filename and Drive `image/jpeg` metadata. Its first R0-A4 submission was rejected by the image endpoint before generation as unsupported `mpo`. The incident is `TOOL_INGESTION_FAILURE — NO EXPERIMENTAL OUTPUT`; it is not image evidence and did not consume the restored output budget.

| Derivative | Drive ID | SHA-256 | Raster | Current decision |
|---|---|---|---:|---|
| `R0-A4_OSLO_PRIMARY_FRAME_STANDARD_JPEG_TOOL_COMPATIBILITY_DERIVATIVE_2026-08-22.jpg` | `1fQ6S66VVsHMIVyZH2LoOvYnbeqh8s7p9` | `0588f3111c38e256520e16bff7059fbd956fe0a47c4f77ddd2821dd961493fd3` | `5520 × 3680` JPEG | Authorized only as `R0_A4_BASE_SCENE_TOOL_INGESTION_SURROGATE`; single-frame container; pixel-identical to the original primary frame; not canonical or independent scene authority |

The derivative was extracted without JPEG recompression. The MPF index and secondary-frame trailer were removed while the primary compressed scan was copied unchanged. Original-primary and derivative decoded-RGB SHA-256 both equal `ffdf8f70240804d3e8a9c2b1b24f3d9760d2a66b4ddcdb47cc0e015364d33985`; pixel comparison found zero differences. The original MPO remains upstream scene authority.

## Future intake procedure

1. Place a candidate in `99 Unverified Intake`.
2. Confirm successful byte and visual access.
3. Record its original filename, MIME type, dimensions, Drive ID, and SHA-256.
4. Confirm its jurisdiction and compare it against the current controlling master.
5. Obtain Nate's explicit promotion decision.
6. For canonical-master promotion, move the approved file into `01 Canonical Masters` and update `SOURCE_MANIFEST.md` in the same change. For a narrower experiment-scoped role, move it to the applicable experiment folder and record its exact jurisdiction without adding it to the canonical manifest.
