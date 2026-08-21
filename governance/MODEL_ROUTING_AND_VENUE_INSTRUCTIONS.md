# The Legacy — Model Routing and Venue Instructions

**Status:** Project-specific operating-instruction prototype  
**Version:** 0.2  
**Date:** 2026-08-21

## Purpose

Teach Nate to allocate Chat, Work, and reasoning effort efficiently while The Legacy is being developed. Standardization and answer quality take priority over consumption, but recommendations should still use the least expensive reasoning level likely to succeed.

This is a temporary teaching layer, not a permanent user-interface requirement.

## Choose the venue first

Choose by required capabilities, then preserve the workstream role inside that venue.

- **Chat:** Use for clarification, scope decisions, interpretation, critique, or human judgment when the exact needed evidence is already present and the task requires no connected-source retrieval, file inspection, tool execution, or durable artifact.
- **Work:** Use whenever the next step requires connected GitHub or Drive retrieval, comparison across governed files, visual inspection of remote artifacts, image generation or editing, repository changes, Drive preservation, or another multi-step/tool-bearing output. Independent Evaluation belongs in Work when it must retrieve or inspect governed evidence.
- Coordination, Prompt Design, Laboratory, Evaluation, Dashboard, and Prototype Studio remain distinct roles or threads. Workstream separation is not a fixed mapping in which Evaluation must use Chat and Laboratory must use Work.
- A receiving thread must retrieve exact linked artifacts through connected sources when the handoff supplies their paths, IDs, and hashes. Do not make Nate paste, download, or reattach governed artifacts that are already accessible.
- Do not recommend changing venue merely for ceremony. If the current surface has every required capability and can preserve the role boundary, remain there.

## Choose reasoning effort second

Recommend the least expensive level likely to complete the task correctly.

- Do not comment on reasoning level for trivial requests, routine refinements, obvious next actions, or tasks where Nate has already selected a clearly sufficient level.
- **High:** Default for substantive Legacy prompt design, bounded visual evaluation, controlled comparison, and ordinary governance decisions with clear sources and criteria.
- **Extra High:** Use when ambiguity, source interaction, geometric fidelity, consequential judgment, or a failed High attempt creates a materially harder problem.
- **Max:** Reserve for the hardest single-threaded causal diagnosis, control-system redesign, or conflict that remains unresolved after a strong lower-level pass.
- **Ultra:** Reserve for genuinely parallel, multi-workstream work whose parts benefit from simultaneous deep reasoning. Do not recommend Ultra merely because it is available or because more reasoning might marginally improve a straightforward answer.
- Proper standardization outranks credit conservation. Escalate when the identified failure condition is present, not as a reflex.

## Routing recommendations must be paired with an actionable handoff

Never append a venue/reasoning footer by itself.

A routing recommendation is allowed only when the response first provides both:

1. an explicit next prompt, command, or concrete instruction Nate can use; and
2. clear directions explaining where and how to use it.

The short routing line then closes that handoff. It must refer to the immediately preceding instructions, so it cannot read as a non sequitur.

## When to omit the routing line

Do not include one when:

- the response does not request or prepare a next user action;
- no prompt, command, or use instruction is being handed off;
- there is no meaningful reason to change venue;
- the answer is a simple clarification, confirmation, status update, or ordinary conversational response;
- the assistant is already executing the authorized task;
- the current venue and reasoning level are plainly adequate and teaching the distinction would add no value;
- Nate has already chosen an appropriate level and no escalation condition has appeared.

Silence is the correct routing guidance when routing guidance would not improve Nate's decision.

## Routing-line style

Keep it casual, short, and specific. Do not label it as a formal “routing recommendation” or explain the full model hierarchy again.

Use one of these forms only after the paired handoff:

- `Go to: Chat · use High unless [very short escalation condition].`
- `Go to: Work · use High unless [very short escalation condition].`
- `Stay here: Chat · use High unless [very short escalation condition].`
- `Stay here: Work · use High unless [very short escalation condition].`

The exception must describe an observable fail case, not a vague possibility.

Good examples:

- `Go to: Work · use High unless source retrieval reveals conflicting authority.`
- `Go to: Work · use High unless the first controlled edit changes anything outside the authorized region.`
- `Stay here: Work · use High unless the evaluator cannot separate topology drift from material mismatch.`

Bad examples:

- `Use more reasoning if needed.`
- `Extra High may provide a better answer.`
- A routing line after a response that supplied no prompt or next-use instructions.

## Escalation behavior

When the stated fail case occurs:

1. stop the current attempt if continuing would contaminate evidence or spend the only allowed revision;
2. identify the specific failure that triggered escalation;
3. recommend the next reasoning level only, not every available level;
4. preserve the same sources, authority boundaries, and held constants unless Nate explicitly approves a redesign;
5. do not treat escalation as permission to broaden scope or combine workstreams.

## Project-only boundary

These instructions apply only inside **The Legacy — Image Generation 2.0**. Do not export this routing layer into unrelated conversations or projects. For ordinary tasks elsewhere, omit model commentary when the selected mode is already sufficient.
