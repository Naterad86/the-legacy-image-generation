# Legacyify workflow helper

This is a local assistant for the three Legacyify actions. It prepares a prompt and its image references, records every attempt, checks the saved bytes, and leaves a resumable state report. **It does not generate images.** Codex runs the built-in image tool after inspecting your references. No API key, network connection, or paid API runner is used by this helper.

The helper never changes image pixels or writes back to a source image. It reads images with Pillow, verifies the file, decodes every frame, and records SHA256 hashes and dimensions. Those checks establish file provenance and readability; they do not prove that a generated character or scene stayed consistent.

## The three actions

| Action | Reference roles | What to inspect afterward |
|---|---|---|
| `character` | One `target`; optional `identity` and `style` references. The pose prototype uses a pose target plus canonical identity. | Identity, distinctive features, requested pose/change, blunt master fingertips/nails, listed invariants, visual treatment, anatomy |
| `scene` | One `target`; a `style` reference or written style description | Camera, major geometry, object placement, weather, luminance, secondary details, visual treatment |
| `together` | One scene `target`; at least one `identity` reference; optional `style` | Character identity, scene contents and source medium, placement, scale, contact, perspective, lighting, visual treatment |

Start with one principal character and clearly structured scenes. Tiny text, dense crowds, intricate geometry, severe pose changes, and substantial occlusion need additional development and explicit review. These are input boundaries for development, not guaranteed capabilities. A packet always begins as unvalidated.

For a fresh Together scene, the default campaign profile is `ILLUSTRATED_CHARACTER_OVER_SOURCE`: retain the source environment's medium and add the illustrated character. `HYBRID_CGI_ILLUSTRATED_CHARACTER` remains available for an existing CGI environment or an explicitly requested conversion; new CGI conversion is experimental. T01 demonstrated structural integration in the existing rendered office. T02 demonstrated character insertion and broad alpine-scene preservation, but its originally requested CGI conversion remains unproven and must not be relabeled as passing.

The source-to-pose Character prototype uses a fresh pose image as `target` plus the canonical master as `identity`. Use an authored `--prompt-file` that gives the target only pose/frame/staging authority and gives the master all character identity, anatomy, outfit, illustrated construction, and blunt fingertip/nail authority. C03 demonstrated this role isolation on a synthetic human input but invented dark pointed claws. C04 received practical PASS for source-role isolation, controlled pose transfer, recognizable character continuity, and corrected blunt natural fingertips on both hands. C04 is a separate revised request; it does not erase C03's failure or prove exact facial geometry, arbitrary-photo transfer, or correction reliability. S01/T01 failed exact emblem-shape fidelity, and stylization can shift salient geometry even when the broad scene is recognizable. The ledger and actual reviews remain the record of what each frozen request achieved.

The packet uses image-reference order exactly as supplied. A reference can be `target`, `identity`, `style`, or `support`. Do not reuse the same image twice under different roles; give its combined authority in the authored prompt instead. This makes the actual list of tool inputs unambiguous.

## Exact replay of the completed campaign

Use `attempts/<ID>-execution/packet/packet.json` for the exact original tool arguments, and `attempts/<ID>-execution/prompt-exact.txt` for the exact prompt text. For example, the final pose prototype is [C04's execution packet](../attempts/C04-execution/packet/packet.json). The corrected audit is [validated-attempts.jsonl](../records/validated-attempts.jsonl); [PROVENANCE_VALIDATION.md](../records/PROVENANCE_VALIDATION.md) explains how it was materialized retrospectively and corrects the original prompt files' one extra terminal LF byte.

Keep the original packet directories and `records/attempts.jsonl` as history. Any replay is a new call with a fresh attempt ID, packet, and ledger entry; it must not overwrite or append synthetic execution history to the old campaign records. Pass `tool_arguments` unchanged, without trimming or adding whitespace. Exact replay means the same recorded arguments and input bytes, not a guarantee of identical new pixels. The examples below use fresh IDs and a separate new-run ledger.

## Run it

Requires Python 3.10+ and Pillow. The existing desktop runtime includes both. In PowerShell, from the `legacyify` folder:

```powershell
$legacyPython = 'C:\Users\galip\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $legacyPython .\workflow\legacyify.py --help
```

On another computer, substitute a Python executable with Pillow installed. All image paths in packets and ledgers become absolute paths so the recorded source is explicit.

### 1. Inventory original sources

```powershell
& $legacyPython .\workflow\legacyify.py inventory .\sources\character.png .\sources\style.png --role source --output .\records\source-manifest-01.json
```

Inventory accepts any Pillow-readable image. It records full file SHA256, byte count, width, height, format, color mode, and frame count. It does not claim that every Pillow-supported image is a valid input to the built-in tool; use a normal PNG/JPEG/WebP when preparing actual image calls.

### 2. Prepare a fresh packet

Write a short request to a UTF-8 text file, then use the structured template:

```powershell
& $legacyPython .\workflow\legacyify.py prepare --action character --id N01 --input 'target=.\sources\character.png' --input 'style=.\sources\style.png' --request-file .\records\N01-request.txt --preserve 'Face, proportions, silhouette, signature colors and identifying details' --preserve 'All scene contents outside the requested change' --out-dir .\attempts\N01-packet
```

For `scene`, choose `--action scene`. For `together`, choose `--action together` and add `--input 'identity=PATH'`. Use repeated `--preserve` and `--constraint` arguments for concrete requirements. Instead of a style image, `--style-text-file PATH` can contain an approved written style description.

If Codex already authored a full prompt, use `--prompt-file` **instead of** `--request-file`. This imports the text verbatim without adding template instructions. The role labels and invariants still go into the packet metadata; the imported prompt itself must explain them to the image tool. An exact imported prompt can contain its own style specification, so a separate style reference is optional.

For a follow-up to an earlier successful attempt in the same ledger, add `--parent-attempt N01`. This is workflow ancestry; the exact image ancestry remains the list of input hashes. Every actual call gets a new attempt ID and a new packet directory, including failed calls and retries.

The new directory contains:

- `packet.json`: exact prompt, ordered reference paths and roles, source fingerprints, action scope, review checklist, and built-in tool arguments.
- `prompt.txt`: the same prompt as readable text.

Existing packet directories and report files are refused. Create a new version rather than replacing provenance.

For a genuinely new synthetic source with no image references, use the separate setup action:

```powershell
& $legacyPython .\workflow\legacyify.py prepare --action source_setup --id E03 --prompt-file .\records\E03-prompt.txt --out-dir .\attempts\E03-packet
```

`source_setup` rejects image references. Its tool arguments contain only the prompt: both `referenced_image_paths` and `num_last_images_to_include` are omitted. Record it through the same ledger lifecycle, labeling the result as synthetic development material. It is a setup operation, not a fourth Legacyify product action. The existing three actions still require exactly one target and explicit invariants; Together still requires identity authority.

### 3. Execute inside Codex

1. Read `packet.json`, check its boundaries, and inspect each local input with `view_image` before editing.
2. Record `started` immediately before the actual tool call.
3. Call `image_gen.imagegen` with the exact `tool_arguments` from the packet. The packet supplies `prompt` and `referenced_image_paths`. Do not add `num_last_images_to_include` when using explicit reference paths.
4. Copy each returned original image byte-for-byte into the campaign's attempts folder under a new filename. Keep the original output even if it fails visual review. Keep later crops, annotations, and presentation derivatives separate.
5. Record `succeeded` for a tool call that returned saved images; this describes execution, not a passing visual result. Record `failed` for a tool error or `interrupted` if it ended without a result. If a call is still pending, leave it `started`; the resume report will flag it.
6. Inspect the result and append a `reviewed` event with the actual observed verdict.

```powershell
& $legacyPython .\workflow\legacyify.py record --ledger .\records\new-run-attempts.jsonl --packet .\attempts\N01-packet\packet.json --status started
& $legacyPython .\workflow\legacyify.py record --ledger .\records\new-run-attempts.jsonl --packet .\attempts\N01-packet\packet.json --status succeeded --output .\attempts\N01-original.png
& $legacyPython .\workflow\legacyify.py record --ledger .\records\new-run-attempts.jsonl --packet .\attempts\N01-packet\packet.json --status reviewed --review-file .\records\N01-review.json
```

For multiline notes, use `--note-file PATH`; for a short note, use `--note 'Tool error description'`. Repeat `--output` if one tool call returned several images.

Suggested review JSON:

```json
{
  "verdict": "conditional",
  "assessor": "Codex visual inspection",
  "checks": [
    {"criterion": "Signature features", "result": "pass", "evidence": "Describe what the actual image shows."},
    {"criterion": "Small background details", "result": "fail", "evidence": "Name the specific drift and region."}
  ],
  "boundary": "What this attempt supports, and where it should not be generalized.",
  "next_change": "One targeted change if another attempt is justified."
}
```

`review` is intentionally a human-authored JSON object. The helper does not invent scores or infer visual success. A reviewed event can be followed by another reviewed event to correct or extend the assessment without rewriting history.

### 4. Verify and checkpoint

```powershell
& $legacyPython .\workflow\legacyify.py validate --ledger .\records\new-run-attempts.jsonl
& $legacyPython .\workflow\legacyify.py resume --ledger .\records\new-run-attempts.jsonl --plan-file .\records\new-run-resume-plan.json --output .\records\new-run-resume-state-01.json
```

Validation checks the hash chain, event sequence, lifecycle, pinned packet, exact prompt, source and output hashes, dimensions, full image decoding, and output/input lineage. `--structure-only` skips current filesystem checks; it is useful for inspecting an archive after paths change and must not be presented as a fresh byte verification.

The resume plan can use these fields, with any extra human notes needed:

```json
{
  "completed": ["Which action is usable and where the best output is saved"],
  "remaining_issues": ["Specific failures or uncertainty"],
  "next_step": "Exact next useful action, with packet or source paths",
  "budget": {
    "refreshed_allowance_used_percent": null,
    "refreshes_redeemed": 0,
    "refreshed_allowance_hard_stop_remaining_percent": 85
  }
}
```

The report preserves this plan, summarizes latest attempt states, keeps links to saved outputs and packets, identifies calls still marked `started`, and records the last ledger event hash. Codex account tools manage usage checks and refreshes. This helper does not access or enforce account limits. The campaign's agreed maximum is the existing allowance, at most one refresh, then at most 15% consumed of the refreshed allowance, stopping with at least 85% remaining.

## Integration contract

All commands return exit code `0` on success and `2` on expected input/provenance errors. Diagnostics go to stderr; paths or JSON results go to stdout. The helper only writes a file/directory explicitly requested by the caller. It makes temporary adjacent lock and transaction files while appending a ledger and removes them after the operation.

| Artifact | Schema/version | Key fields |
|---|---|---|
| Inventory JSON | `schema_version: 1`, `kind: legacyify_inventory` | `created_at`, `assets[]` |
| Packet JSON | `schema_version: 1`, `kind: legacyify_action_packet` | `attempt_id`, `action`, `inputs[]`, `parent_attempts[]`, `prompt`, `prompt_sha256`, `prompt_mode`, `preserve[]`, `tool_arguments`, `review_checklist[]` |
| Event JSONL | `schema_version: 1`; one complete object per line | `sequence`, `event_id`, `recorded_at`, `attempt_id`, `action`, `status`, `packet_path`, `packet_sha256`, `prompt`, `prompt_sha256`, `inputs[]`, `outputs[]`, `parent_attempts[]`, `notes`, `review`, `previous_event_sha256`, `event_sha256` |
| Resume JSON | `schema_version: 1` | `event_count`, `last_event_sha256`, `status_counts`, `attempts[]`, `incomplete_attempts[]`, `resume_plan`, `next_step` |

Each asset is `{path, sha256, bytes, width, height, format, mode, frames, role}`. Output assets additionally contain `input_sha256`, the ordered hashes of the image inputs to that call. Hashes are lowercase SHA256 hex; timestamps are UTC ISO 8601. The exact prompt is hashed as UTF-8. Event hashes are computed over all event fields except `event_sha256`, using UTF-8 JSON with sorted keys, no extra spaces, and unescaped Unicode. The first event's `previous_event_sha256` is null.

Allowed lifecycle: `started` → `succeeded`, `failed`, or `interrupted`; `succeeded` → `reviewed`; `reviewed` → `reviewed`. A parent attempt must already have succeeded or been reviewed. Success requires at least one output. Reviews require an object. Inputs, prompt, action, parents, and packet bytes stay pinned for an attempt. `started` and the result use the **same packet file**; a changed prompt needs a new packet and attempt ID.

The ledger is append-only through this CLI and detects accidental edits. It is not a signed or externally notarized audit log: someone with filesystem access can rewrite the entire chain. Preserve the final resume report/hash with the handoff to help detect later truncation. A crash can leave a lock or incomplete trailing line; the helper refuses to silently repair these. Inspect the saved state and establish that no writer is active before recovering a ledger copy. Keep the original damaged file as evidence.

## Verification

```powershell
& $legacyPython .\workflow\test_legacyify.py
```

Twelve checks cover original-byte preservation, exact prompt import, output lineage, full lifecycle and resume state, corrupted image rejection, changed sources and outputs, ledger tampering, a changed packet between events, invalid transition refusal, concurrent-writer protection, and zero-reference source setup without relaxing the three existing actions. Test fixtures stay in temporary directories within this workflow folder and are removed afterward. No image model is invoked.

The portable [Legacyify skill](legacyify-skill/SKILL.md) adds the September 7 one-request/one-raw-output product contract, source-role compilation, conditional boundaries, and demo-first delivery. Ask Codex to read/use that file. It has not been installed into your skill library.
