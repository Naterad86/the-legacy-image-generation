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

## Future intake procedure

1. Place a candidate in `99 Unverified Intake`.
2. Confirm successful byte and visual access.
3. Record its original filename, MIME type, dimensions, Drive ID, and SHA-256.
4. Confirm its jurisdiction and compare it against the current controlling master.
5. Obtain Nate's explicit promotion decision.
6. Move the approved file into `01 Canonical Masters` and update `SOURCE_MANIFEST.md` in the same change.
