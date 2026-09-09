# Exact-transport provenance validation

Validated 2026-09-09T11:49:46+00:00.

**PASS: 12 original calls, 12 untouched raw PNGs, 10 action reviews, and 34 validated lifecycle events.** Four Character, three Scene, and three Together outputs are development actions. E01 and E02 are synthetic setup inputs and are excluded from the ten-action count.

## What was corrected

Every original authored prompt text file contains exactly one additional terminal LF byte (`0x0A`) beyond the prompt string actually sent to the built-in image tool. The earlier packets and `records/attempts.jsonl` consistently recorded those file bytes, so they were internally consistent but were not byte-exact representations of the transport prompt.

The separate `records/ACTUAL_TOOL_CALLS.json` capture was materialized retrospectively from the orchestration session store. Its `actual_tool_arguments` supply the corrected exact strings and original reference order. New `attempts/<ID>-execution/prompt-exact.txt` files and `packet/packet.json` files reproduce those arguments exactly, without adding a newline. The original prompt files, packet directories, raw outputs, and 24-event `records/attempts.jsonl` remain unchanged history.

## Timing and evidence limits

`records/validated-attempts.jsonl` is a retrospective audit import, not a log that was written before the image calls. All `created_at`/`recorded_at` values are materialization times. The `started` events reconstruct already-completed lifecycle states and did not initiate requests. Actual execution order is preserved in each packet's `execution_order` field and every event note. No generation timestamp is inferred from those import timestamps.

The ten new `review.json` files retain each separate evaluator markdown's full text, source SHA256, practical verdict, and exact acceptance paragraph. Importing a practical PASS does not promote a strict-fidelity failure or unproven requirement to a pass. E01/E02 have execution records but no invented action review.

## Validation performed

- Matched all 12 packet tool-argument objects and UTF-8 prompt hashes to the captured transport arguments, including input order/roles and omission of both reference arguments for E01/E02.
- Validated the corrected ledger's hash chain, all transitions, packet pins, source and raw-output SHA256 hashes, image dimensions, full decoding, parent-attempt links, and ordered input lineage.
- Matched 12/12 saved raw images byte-for-byte to the built-in tool's original generated-image paths recorded in its output hints.
- Preserved all ten evaluator texts verbatim in review JSON and reviewed events. Confirmed every protected original file was unchanged after import.
- Changed no output pixels. This validates provenance and readable image files; it does not establish visual reliability, canonical identity exactness, or held-out qualification.

| Call order | Attempt | Action | Raw dimensions | Imported practical verdict |
|---|---|---|---|---|
| 1 | C01 | character | 1122 x 1402 | CONDITIONAL |
| 2 | S01 | scene | 1672 x 941 | CONDITIONAL |
| 3 | T01 | together | 1672 x 941 | CONDITIONAL |
| 4 | E01 | source_setup | 1672 x 941 | Setup only; no action verdict |
| 5 | S02 | scene | 1672 x 941 | CONDITIONAL |
| 6 | C02 | character | 1122 x 1402 | PASS |
| 7 | T02 | together | 1672 x 941 | CONDITIONAL |
| 8 | E02 | source_setup | 1122 x 1402 | Setup only; no action verdict |
| 9 | C03 | character | 1122 x 1402 | CONDITIONAL |
| 10 | S03 | scene | 1672 x 941 | PASS |
| 11 | T03 | together | 1672 x 941 | PASS |
| 12 | C04 | character | 1122 x 1402 | PASS |

Corrected ledger final event SHA256: `f553f52bf9f5ff74051fc71e4f9b695b2f0aec2352df300e9cbcb8fa492bafc1`.
Corrected ledger file SHA256: `18a8107da1ffd2a90ced65f837858f43f189fd8e047a596ba3541b69ca9b1840`.
Actual transport capture SHA256: `8db8d6a65d9790a36228036a5f9fd060d9b77d73ed9baf6c776239bfcb190556`.

Use the new execution packets for exact prompt replay and the corrected ledger for byte-level audit. Retain the original ledger alongside them to preserve the materialization history.
