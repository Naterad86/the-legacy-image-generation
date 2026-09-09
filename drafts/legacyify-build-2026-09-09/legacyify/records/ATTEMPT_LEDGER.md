# Complete development attempt record

Campaign: September 9, 2026. Tool: built-in `image_gen.imagegen`. **12 calls, 12 returned original PNGs, 0 image-tool failures, 0 post-generation image repairs.** Ten calls were action trials; two created synthetic development sources. Every original image is preserved in `../attempts/`.

Execution order below comes from the actual tool sequence. The first four calls were imported into the local helper's original ledger after it became ready. That ledger's event timestamps are recording times, not original invocation start times. See [exact actual arguments](ACTUAL_TOOL_CALLS.json) and [provenance validation](PROVENANCE_VALIDATION.md). The original prompt packets include a terminal newline added by text-file formatting; exact transport strings are preserved in the actual-arguments record and corrected execution packets.

| Order | ID | Action / source | Practical result | Meaningful finding | Raw | Review |
|---:|---|---|---|---|---|---|
| 1 | C01 | Male welcoming pose | Conditional | Strong recognizability and coherent anatomy; eyes/face/mane rebuilt modestly; palm height differs. | [PNG](../attempts/C01-raw.png) | [Review](review-C01.md) |
| 2 | S01 | Office to pixel art | Conditional | Strong medium/layout; main emblem topology differs from master. Secondary mark removal was permitted. | [PNG](../attempts/S01-raw.png) | [Review](review-S01.md) |
| 3 | T01 | Female in CGI office | Conditional | Coherent mixed-medium integration and seating; exact emblem fails, fine identity/scene changes remain. | [PNG](../attempts/T01-raw.png) | [Review](review-T01.md) |
| 4 | E01 | Synthetic alpine source | Setup only | New generated development scene; not real photography or held-out evidence. | [PNG](../attempts/E01-raw.png) | [Prompt](../attempts/E01-prompt.txt) |
| 5 | S02 | Alpine to pixel art | Conditional | Lamp became rectangular, path/frame/skyline shifted. | [PNG](../attempts/S02-raw.png) | [Review](review-S02.md) |
| 6 | C02 | Female arms folded | Pass | Recognizable continuity, coherent pose, polished illustration; mild facial/hair variation remains. | [PNG](../attempts/C02-raw.png) | [Review](review-C02.md) |
| 7 | T02 | Male in alpine scene | Conditional | Strong insertion/source preservation; separate CGI conversion unproven and figure too large for brief. | [PNG](../attempts/T02-raw.png) | [Review](review-T02.md) |
| 8 | E02 | Synthetic human pose | Setup only | Fictional adult presenter for pose-role test; not a real person's photograph. | [PNG](../attempts/E02-raw.png) | [Prompt](../attempts/E02-prompt.txt) |
| 9 | C03 | Human pose to male lion | Conditional | Pose-only role isolation works; conspicuous dark pointed claws were invented. | [PNG](../attempts/C03-raw.png) | [Review](review-C03.md) |
| 10 | S03 | Revised alpine pixel action | Pass | Round lamp and gentle path retained; remaining fine geometry/light differences. | [PNG](../attempts/S03-raw.png) | [Review](review-S03.md) |
| 11 | T03 | Two characters in alpine scene | Pass, exploratory | Distinct identities, coherent contact and shared light; figures exceed requested height. Source medium preserved as requested. | [PNG](../attempts/T03-raw.png) | [Review](review-T03.md) |
| 12 | C04 | Revised pose-transfer action | Pass | Blunt fingertips corrected; recognizable male, pose isolation and coherent anatomy retained. | [PNG](../attempts/C04-raw.png) | [Review](review-C04.md) |

**Pass is a practical visual judgment, not an assertion that every literal prompt constraint passed.** Exact deviations remain in the separate-agent review. The evaluator is another Codex agent, not an independent human or blinded external panel. Four practical passes and six conditional outcomes are descriptive counts from a changing development sample; they do not establish a reliability rate.

## Transparent revisions

- S03 revises S02's brief around lamp shape and path preservation, using the original alpine source again. S02 does not become a pass.
- C04 revises C03's brief around blunt fingertips, using the original human pose and original male master again. C03 does not become a pass.
- T03 is a separately declared two-character exploratory extension. It explicitly preserves the existing environmental medium; it does not repair or relabel T02's missed CGI request.

## Selected outputs

The files in `../selected/` are byte-for-byte copies of C04, S03, T01 and T03. They are not cropped, retouched, recolored or upscaled. The demo presents primary actions and additional proof examples while keeping all development results available.

## Scope

No historical failed output was used as a new visual authority. No held-out task bank was populated or consumed. No canonical source was modified or promoted. No asset was publicly published. This package is a local development demonstration and reusable Codex workflow.
