# Legacyify build draft — 2026-09-09

**Preservation snapshot before user analysis and governing project direction updates.** This snapshot does not amend governance, promote sources or descendants, accept experiment stages, or establish production readiness. It preserves the implemented gallery, reusable workflow and recorded history as they stood after the three user-supplied live actions.

Published as a draft on branch `draft/legacyify-build-2026-09-09` from base commit `ee1fa550ce4882734abc99b45137aeef3a25a20d`. The user explicitly approved public GitHub and Drive preservation of these text records, including their existing absolute local paths, Drive identifiers and budget metadata. This snapshot remains a preservation record pending the user's analysis and governing direction updates.

A [dated text backup](https://drive.google.com/file/d/19O5C5vJ07L8lq4rstdOPSfOdSeC3Npq6/view) is also preserved in Drive. Its ZIP SHA256 is `c696df7d56356f7351b3ff546c5ce4c0cbdae8bc2513d6f20b15693a2194d1b1` and size is 396,457 bytes. That export was assembled before approval, so its wrapper README records the earlier pending-publication state; all 150 captured source code/text files are identical to this commit. The dated backup is not an editable replacement for governing GitHub controls.

## Preserved build

- [`legacyify/`](legacyify/README.md): overnight demo implementation, action descriptions, portable skill, Python provenance helper/tests, frozen prompts and packets, all original and corrected text records, reviews and handoff information.
- [`legacyify-live/`](legacyify-live/): the subsequent C05 Character, S04 Scene and T04 Together invocations, each with its pre-call brief, exact prompt/arguments, reviewed result record and validation.
- [`SNAPSHOT_MANIFEST.json`](SNAPSHOT_MANIFEST.json): SHA256 and byte count for all 183 captured files: 150 code/text files and 33 media files.
- [`MEDIA_LOCATION.json`](MEDIA_LOCATION.json): verified Drive media-archive location, exact local archive hash, expected restoration paths and canonical Drive references.

The source files were copied byte-for-byte. Existing mistakes, review verdicts, original-versus-corrected prompt records, retrospective imports, absolute historical paths, budget snapshots and earlier completion statements remain historical records. They have not been rewritten to fit a new interpretation. The live attempts are separate from the frozen overnight package; the old overnight gallery intentionally does not include those later actions.

## Image storage boundary

Repository [`AGENTS.md`](../../AGENTS.md) and [`STORAGE_AUTHORITY.md`](../../governance/STORAGE_AUTHORITY.md) prohibit canonical art, raw generations and duplicate visual evidence in this public repository. No image bytes, embedded image data, QA screenshots or media ZIP are committed here.

The 33 media files are preserved unchanged in [Legacyify-Build-Draft-2026-09-09-Media.zip](https://drive.google.com/file/d/1uCT02lbUyh-OZP0lbCzu0GSSD8LSBnCa/view) in the governed Drive **06 Releases & Handoffs** folder. The user explicitly approved Drive as the destination for appropriate artifacts before this upload. Drive readback confirmed the file ID, name, ZIP MIME type, destination and 51,288,519-byte size. The archive was checked locally against every original media entry. Canonical masters retain their existing Drive IDs and authority; the archive is a dated draft transfer copy.

This GitHub snapshot preserves code/text and asset fingerprints; the linked Drive archive preserves the visual bytes. Local originals and the dated text backup remain available. No Drive sharing permissions were changed.

## Restore and view

1. Obtain this draft snapshot and the exact media archive identified in `MEDIA_LOCATION.json`; verify the archive SHA256.
2. Extract its `legacyify/` and `legacyify-live/` folders into this directory. The archive also contains `MEDIA_MANIFEST.json`. Verify restored file hashes against `SNAPSHOT_MANIFEST.json`.
3. Open `legacyify/index.html` locally. Open each live action's README for its original image and record. The gallery needs no web service or API key.

Gallery copy commands contain the original machine's skill path. On another machine, point Codex to the restored `legacyify/workflow/legacyify-skill/SKILL.md`. Historical packets and ledger hash chains deliberately retain their original absolute paths; do not edit them to make validation pass. Use a separate path mapping/workspace for replay. The helper's `--structure-only` option checks ledger structure, not the restored image bytes. The helper requires Python and Pillow; runtime dependencies are not bundled.

## Preservation checks

All 150 source code/text files match their local originals by SHA256. All 33 archived media entries match their original bytes, and the ZIP integrity check passed. Existing browser, workflow and ledger verification records are retained with their original dates and scopes. No image generation, new visual evaluation, or governing direction change was performed for this preservation step.
