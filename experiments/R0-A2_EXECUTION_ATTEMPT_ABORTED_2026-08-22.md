# R0-A2 Geometry-Lock Isolation — Execution Attempt

**Status:** ABORTED — GENERATION-ROUTE FAILURE; R0-A2 NOT EVALUATED  
**Date:** 2026-08-22  
**Frozen packet:** `experiments/R0-A2_GEOMETRY_LOCK_ISOLATION_FROZEN_2026-08-22.md`

## Authority verification

The exact frozen source was retrieved from Google Drive before the authorized run:

- Filename: `G1-A_HOLDOUT_OSLO_OPERA_HOUSE_BASE_SOURCE_INTERNAL_VALIDATION_2026-08-20.jpg`
- Drive ID: `1hcaY5KRnVWCbmBHb1O_jwj-oNHp9a8ZR`
- Verified SHA-256: `f2445f76358774a363ad9a4783b4b3c196f561e8f2a040b94dbcf5b19c174b75`
- Verified raster: `5520 × 3680` JPEG

The local retrieved bytes matched the frozen packet hash exactly.

## Execution outcome

The authorized protocol required exactly three independent scene outputs from the untouched source, with identical generation instructions and no evaluation content in the Laboratory generation context.

The image-generation route did **not** execute that protocol reliably in the current conversation context.

- One legitimate standalone scene output was produced and preserved as raw evidence.
- Eight additional generation attempts returned protocol/infographic images containing experiment text, source thumbnails, controls, scorecard-like material, or other document graphics rather than the requested scene.
- Those eight graphics are **invalid outputs** and are excluded from R0-A2 evidence.
- They must not be interpreted as evaluations, scorecards, comparisons, or scene generations.

Because Runs 2 and 3 were never validly produced, the frozen three-run protocol is incomplete. No cross-output analysis is possible and no R0-A2 PASS/FAIL classification is authorized.

## Preserved valid raw output

`R0-A2_RUN1_RAW_2026-08-22.png`

- Drive folder: `03 Laboratory Evidence`
- Drive ID: `1YN5MRYwAtVVObmlO6js7Br21g3c4bE2F`
- SHA-256 of local raw PNG before upload: `b375e7975fa58d67b438cb154cb86442c93a73e507ac40de5cf5ab5d401b5937`

Run 1 is preserved as raw evidence only. Under the frozen protocol, formal Evaluation was to begin after all three raw scene outputs existed. Therefore no frozen-gate verdict is assigned to Run 1 in this execution record.

## Classification of the execution failure

This is **not evidence that the R0-A2 geometry-lock hypothesis passed or failed**.

It is evidence of a separate orchestration failure:

> In a conversation containing extensive experiment-design and evaluation language, the generation route repeatedly interpreted the task as a request to visualize the protocol itself rather than execute the frozen scene-only generation instruction.

The repeated behavior persisted despite explicit scene-only directives and explicit prohibitions on text, boards, labels, protocol graphics, and evaluation content.

## Generalized process finding

Generation/evaluation separation must include **conversation-context isolation**, not only prompt-level separation.

For controlled image-generation experiments, a Laboratory run should occur in a fresh execution context containing only:

1. the exact frozen generation packet or its executable instruction;
2. the exact authorized visual source(s);
3. the minimum retrieval metadata needed to verify those sources;
4. no prior evaluation boards, scorecards, generated protocol graphics, or discussion of verdicts.

The current thread is suitable for design, governance, and analysis but is now demonstrated to be a contaminated Laboratory execution context for R0-A2.

## Resumption rule

Do not modify the frozen R0-A2 hypothesis, held/released boundary, or gates because of this aborted attempt.

Resume R0-A2 in a fresh Laboratory execution context. Retrieve the frozen packet from GitHub and the exact source object from Drive, generate exactly three scene-only outputs, preserve them, and then hard-stop for independent Evaluation.

Do not use `R0-A2_RUN1_RAW_2026-08-22.png` as an authority or input to the resumed runs. It remains descendant evidence only.
