#!/usr/bin/env python3
"""Local provenance and action packets. Never generates or modifies images."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import uuid

from PIL import Image, UnidentifiedImageError

VERSION = 1
STATUSES = {"started", "succeeded", "failed", "interrupted", "reviewed"}
ACTIONS = {
    "source_setup": {
        "label": "Synthetic development source setup",
        "use_case": "stylized-concept",
        "scope": "A newly generated synthetic development source, never a real-world or held-out test input.",
        "instruction": "Create a new synthetic development image from this brief. No source images or canonical identity references are supplied. Do not claim this output is a historical master or real-world validation input.",
        "review": ["Requested source scene", "Legibility of scene structure", "Required objects and relationships", "Synthetic source label in campaign records"],
    },
    "character": {
        "label": "Legacyify Character",
        "use_case": "identity-preserve",
        "scope": "One principal character; bounded, explicitly requested changes.",
        "instruction": "Treat the target as the content source. Preserve the character's identity and all explicitly listed invariants. Use an identity reference only for identity, and a style reference only for visual treatment.",
        "review": ["Identity and signature features", "Requested change", "Explicit invariants", "Legacy visual treatment", "Anatomy and artifact inspection"],
    },
    "scene": {
        "label": "Legacyify Scene",
        "use_case": "style-transfer",
        "scope": "A clearly structured scene; fine text, crowds, and intricate geometry need separate review.",
        "instruction": "Treat the target as the content and composition source. Transfer only the requested visual treatment from the style reference. Do not import its objects, layout, characters, or scene state.",
        "review": ["Camera and major geometry", "Object presence and placement", "Weather and scene state", "Luminance and lighting", "Legacy visual treatment", "Secondary details"],
    },
    "together": {
        "label": "Legacyify Together",
        "use_case": "compositing",
        "scope": "One canonical character in a relatively simple target scene; this action is experimental until tested on fresh inputs.",
        "instruction": "Treat the target as the scene and composition source, the identity reference as the character source, and the style reference only as visual treatment. Integrate the requested character with coherent scale, perspective, contact, and lighting. Do not import the identity reference's background.",
        "review": ["Character identity", "Scene geometry and contents", "Requested placement and action", "Scale, contact, and perspective", "Lighting integration", "Legacy visual treatment"],
    },
}


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest_bytes(value):
    return hashlib.sha256(value).hexdigest()


def digest_file(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def write_new(path, value, text=False):
    """Refuse overwrite: packets and reports should be versioned explicitly."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(value if text else json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    return str(path.resolve())


def inspect_image(path, role=None):
    """Read complete decoded image and fingerprint bytes; no image writes."""
    path = Path(path).expanduser().resolve(strict=True)
    before = path.stat()
    sha = digest_file(path)
    try:
        with Image.open(path) as im:
            fmt, width, height, mode = im.format, im.width, im.height, im.mode
            frames = getattr(im, "n_frames", 1)
            im.verify()
        with Image.open(path) as im:
            for frame in range(frames):
                im.seek(frame)
                im.load()
    except (OSError, UnidentifiedImageError, ValueError) as exc:
        raise ValueError(f"Invalid or incompletely decodable image: {path}: {exc}") from exc
    after = path.stat()
    if before.st_size != after.st_size or before.st_mtime_ns != after.st_mtime_ns or digest_file(path) != sha:
        raise ValueError(f"Image changed during inspection: {path}")
    result = {"path": str(path), "sha256": sha, "bytes": before.st_size,
              "width": width, "height": height, "format": fmt, "mode": mode,
              "frames": frames}
    if role is not None:
        result["role"] = role
    return result


def check_asset(asset, check_files=True):
    required = {"path", "sha256", "bytes", "width", "height", "format", "mode", "frames"}
    if not required <= set(asset):
        raise ValueError("Asset snapshot lacks required fields")
    if not re.fullmatch(r"[0-9a-f]{64}", asset["sha256"]):
        raise ValueError("Invalid SHA256 in asset snapshot")
    if any(type(asset[k]) is not int or asset[k] <= 0 for k in ("bytes", "width", "height", "frames")):
        raise ValueError("Invalid byte count or image dimensions")
    if check_files:
        fresh = inspect_image(asset["path"])
        if any(fresh[k] != asset[k] for k in required):
            raise ValueError(f"Asset differs from recorded original: {asset['path']}")


def inventory(args):
    assets = [inspect_image(path, args.role) for path in args.paths]
    value = {"schema_version": VERSION, "kind": "legacyify_inventory", "created_at": utc_now(), "assets": assets}
    print(write_new(args.output, value))


def read_text(path):
    return Path(path).read_text(encoding="utf-8-sig").strip()


def prepare(args):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,79}", args.id):
        raise ValueError("Attempt id must be 1-80 letters/digits/dots/underscores/hyphens and start with a letter or digit")
    refs, counts = [], Counter()
    for spec in args.input:
        role, sep, path = spec.partition("=")
        if not sep or role not in {"target", "identity", "style", "support"}:
            raise ValueError("Each input must be target=PATH, identity=PATH, style=PATH, or support=PATH")
        refs.append(inspect_image(path, role))
        counts[role] += 1
    if args.action == "source_setup" and refs:
        raise ValueError("Source setup is brand-new generation and must have zero image references")
    if args.action != "source_setup" and counts["target"] != 1:
        raise ValueError("Exactly one target input is required")
    if args.action != "source_setup" and not args.preserve:
        raise ValueError("At least one explicit --preserve invariant is required")
    if args.action == "together" and not counts["identity"]:
        raise ValueError("Together requires an identity reference")
    if args.action != "source_setup" and not counts["style"] and not args.style_text_file and not args.prompt_file:
        raise ValueError("Supply a style reference or --style-text-file describing the approved Legacy style")
    if len({item["sha256"] for item in refs}) != len(refs):
        raise ValueError("The same image bytes were assigned multiple input roles; combine role instructions instead")
    request = read_text(args.request_file or args.prompt_file)
    if not request:
        raise ValueError("Request file must not be empty")
    style_text = read_text(args.style_text_file) if args.style_text_file else ("Follow the medium described in the primary request." if args.action == "source_setup" else "Use the supplied style reference only for visual treatment.")
    action = ACTIONS[args.action]
    prompt = "\n".join([
        f"Use case: {action['use_case']}",
        f"Asset type: {action['label']} development result",
        f"Primary request: {request}",
        "Input images:",
        *[f"Image {n}: {item['role']} ({Path(item['path']).name})" for n, item in enumerate(refs, 1)],
        f"Reference authority: {action['instruction']}",
        f"Style/medium: {style_text}",
        "Preserve these explicit invariants:",
        *[f"- {item}" for item in args.preserve],
        ("Constraints: Create only the image described in the primary request. No added labels, borders, or watermark. Return one finished image." if args.action == "source_setup" else "Constraints: Change only what the primary request requires; preserve all unrequested content. No added labels, borders, or watermark. Return one finished image."),
        *[f"Additional constraint: {item}" for item in args.constraint],
    ])
    if args.prompt_file:
        # Preserve the actual call text exactly, including intentional outer whitespace.
        prompt = Path(args.prompt_file).read_text(encoding="utf-8-sig")
    tool_arguments = {"prompt": prompt}
    if args.action != "source_setup":
        tool_arguments["referenced_image_paths"] = [item["path"] for item in refs]
    packet = {
        "schema_version": VERSION, "kind": "legacyify_action_packet", "attempt_id": args.id,
        "action": args.action, "created_at": utc_now(), "inputs": refs,
        "parent_attempts": args.parent_attempt, "request": request, "preserve": args.preserve,
        "prompt_mode": "exact_import" if args.prompt_file else "structured_template",
        "scope_boundary": action["scope"], "review_checklist": action["review"],
        "prompt": prompt, "prompt_sha256": digest_bytes(prompt.encode("utf-8")),
        "tool": "image_gen.imagegen", "tool_arguments": tool_arguments,
        "execution": "This packet does not generate. In Codex, inspect each local input with view_image first if references exist, review the prompt, log started, then call the built-in image tool. For source_setup omit both image-reference arguments. Save untouched output bytes under a new filename and log the result. No API key is needed.",
        "qualification": "Unvalidated action packet. A prompt constraint is a target, not a preservation guarantee.",
    }
    folder = Path(args.out_dir)
    folder.mkdir(parents=True, exist_ok=False)
    write_new(folder / "packet.json", packet)
    write_new(folder / "prompt.txt", prompt, text=True)
    print(str((folder / "packet.json").resolve()))


def load_packet(path, check_files=True):
    packet = read_json(path)
    if packet.get("schema_version") != VERSION or packet.get("kind") != "legacyify_action_packet":
        raise ValueError("Unsupported packet schema")
    if packet.get("action") not in ACTIONS:
        raise ValueError("Invalid packet action")
    if packet.get("prompt_sha256") != digest_bytes(packet["prompt"].encode("utf-8")):
        raise ValueError("Packet prompt digest does not match")
    expected_arguments = {"prompt": packet["prompt"]}
    if packet["action"] == "source_setup":
        if packet["inputs"]:
            raise ValueError("Source setup packet must have zero image references")
    else:
        expected_arguments["referenced_image_paths"] = [x["path"] for x in packet["inputs"]]
    if packet["tool_arguments"] != expected_arguments:
        raise ValueError("Tool arguments disagree with packet references or prompt")
    for asset in packet["inputs"]:
        check_asset(asset, check_files)
    return packet


def read_ledger(path, check_files=False):
    path = Path(path)
    if not path.exists():
        return []
    events, states, packets = [], {}, {}
    previous = None
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            raise ValueError(f"Blank ledger line {number}")
        try:
            event = json.loads(line)
            unsigned = {k: v for k, v in event.items() if k != "event_sha256"}
            if event.get("schema_version") != VERSION or event.get("sequence") != number:
                raise ValueError("Schema or sequence mismatch")
            if event.get("previous_event_sha256") != previous or event.get("event_sha256") != digest_bytes(canonical(unsigned)):
                raise ValueError("Hash chain mismatch")
            attempt, status = event["attempt_id"], event["status"]
            if event["action"] not in ACTIONS or status not in STATUSES:
                raise ValueError("Invalid action or status")
            prior = states.get(attempt)
            valid = (prior is None and status == "started") or (prior == "started" and status in {"succeeded", "failed", "interrupted"}) or (prior in {"succeeded", "reviewed"} and status == "reviewed")
            if not valid:
                raise ValueError(f"Invalid transition {prior!r} -> {status!r}")
            if status == "started":
                for parent in event["parent_attempts"]:
                    if states.get(parent) not in {"succeeded", "reviewed"}:
                        raise ValueError(f"Parent attempt has no successful output: {parent}")
            if event["prompt_sha256"] != digest_bytes(event["prompt"].encode("utf-8")):
                raise ValueError("Prompt digest mismatch")
            pin = (event["packet_sha256"], event["action"], event["prompt_sha256"], canonical(event["inputs"]), canonical(event["parent_attempts"]))
            if attempt in packets and pin != packets[attempt]:
                raise ValueError("Attempt packet or inputs changed between events")
            if status == "succeeded" and not event["outputs"]:
                raise ValueError("Successful event must contain an output")
            if status == "reviewed" and not isinstance(event.get("review"), dict):
                raise ValueError("Reviewed event needs a review object")
            for asset in event["inputs"] + event["outputs"]:
                check_asset(asset, check_files)
            expected_ancestors = [x["sha256"] for x in event["inputs"]]
            for output in event["outputs"]:
                if output.get("input_sha256") != expected_ancestors:
                    raise ValueError("Output lineage does not match input snapshots")
            if check_files:
                if digest_file(event["packet_path"]) != event["packet_sha256"]:
                    raise ValueError("Packet file changed")
                packet = load_packet(event["packet_path"], check_files=False)
                if (packet["attempt_id"], packet["action"], packet["prompt_sha256"], packet["inputs"], packet["parent_attempts"]) != (attempt, event["action"], event["prompt_sha256"], event["inputs"], event["parent_attempts"]):
                    raise ValueError("Packet file disagrees with event snapshot")
            states[attempt], packets[attempt] = status, pin
            previous = event["event_sha256"]
            events.append(event)
        except (KeyError, TypeError, ValueError, OSError) as exc:
            raise ValueError(f"Ledger line {number}: {exc}") from exc
    return events


def record(args):
    packet_path = Path(args.packet).resolve(strict=True)
    packet = load_packet(packet_path)
    outputs = [inspect_image(path, "generated") for path in args.output]
    ancestors = [x["sha256"] for x in packet["inputs"]]
    for output in outputs:
        if output["path"] in [x["path"] for x in packet["inputs"]]:
            raise ValueError("An output must not overwrite an input path")
        output["input_sha256"] = ancestors
    if args.status == "succeeded" and not outputs:
        raise ValueError("Supply at least one --output for a successful attempt")
    if args.status == "started" and outputs:
        raise ValueError("Started events cannot have outputs")
    review = read_json(args.review_file) if args.review_file else None
    if args.status == "reviewed" and not isinstance(review, dict):
        raise ValueError("Reviewed events require --review-file containing a JSON object")
    ledger = Path(args.ledger)
    ledger.parent.mkdir(parents=True, exist_ok=True)
    lock = ledger.with_suffix(ledger.suffix + ".lock")
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise ValueError(f"Ledger is locked by another writer: {lock}. If a process crashed, verify no writer remains before removing this lock.") from exc
    try:
        os.close(descriptor)
        events = read_ledger(ledger)
        event = {
            "schema_version": VERSION, "sequence": len(events) + 1, "event_id": str(uuid.uuid4()),
            "recorded_at": utc_now(), "previous_event_sha256": events[-1]["event_sha256"] if events else None,
            "attempt_id": packet["attempt_id"], "action": packet["action"], "status": args.status,
            "packet_path": str(packet_path), "packet_sha256": digest_file(packet_path),
            "prompt": packet["prompt"], "prompt_sha256": packet["prompt_sha256"],
            "inputs": packet["inputs"], "outputs": outputs, "parent_attempts": packet["parent_attempts"],
            "tool": "image_gen.imagegen", "notes": read_text(args.note_file) if args.note_file else args.note,
            "review": review,
        }
        event["event_sha256"] = digest_bytes(canonical(event))
        # Validate the full proposed transaction before append; never repair history silently.
        pending = ledger.with_name(ledger.name + ".pending-" + uuid.uuid4().hex)
        try:
            old = ledger.read_bytes() if ledger.exists() else b""
            if old and not old.endswith(b"\n"):
                raise ValueError("Ledger is missing its final newline; inspect and recover it before appending")
            pending.write_bytes(old + canonical(event) + b"\n")
            read_ledger(pending)
            with ledger.open("ab") as stream:
                stream.write(canonical(event) + b"\n")
                stream.flush()
                os.fsync(stream.fileno())
        finally:
            pending.unlink(missing_ok=True)
        print(json.dumps({"attempt_id": event["attempt_id"], "status": event["status"], "sequence": event["sequence"], "event_sha256": event["event_sha256"]}))
    finally:
        lock.unlink(missing_ok=True)


def validate(args):
    if not Path(args.ledger).is_file():
        raise ValueError(f"Ledger does not exist: {args.ledger}")
    events = read_ledger(args.ledger, check_files=not args.structure_only)
    print(json.dumps({"valid": True, "events": len(events), "attempts": len({e['attempt_id'] for e in events}), "files_checked": not args.structure_only,
                      "limitation": "Verifies provenance and image decoding, not visual quality or identity consistency."}))


def resume(args):
    if not Path(args.ledger).is_file():
        raise ValueError(f"Ledger does not exist: {args.ledger}")
    events = read_ledger(args.ledger)
    latest, outputs = {}, {}
    for event in events:
        latest[event["attempt_id"]] = event
        if event["outputs"]:
            outputs[event["attempt_id"]] = event["outputs"]
    plan = read_json(args.plan_file) if args.plan_file else {}
    if not isinstance(plan, dict):
        raise ValueError("Resume plan must be a JSON object")
    summary = {"schema_version": VERSION, "created_at": utc_now(), "ledger": str(Path(args.ledger).resolve()),
               "event_count": len(events), "last_event_sha256": events[-1]["event_sha256"] if events else None,
               "status_counts": dict(Counter(e["status"] for e in latest.values())),
               "attempts": [{"attempt_id": aid, "action": event["action"], "status": event["status"],
                             "packet_path": event["packet_path"], "outputs": outputs.get(aid, []), "review": event["review"], "notes": event["notes"]} for aid, event in latest.items()],
               "incomplete_attempts": [aid for aid, event in latest.items() if event["status"] == "started"],
               "resume_plan": plan,
               "next_step": plan.get("next_step", "Inspect outputs and ledger. Resolve any started attempts before creating a new attempt ID; validate provenance before continuing."),
               "budget_note": "Budget readings and reset redemption are managed by Codex account tools; this helper does not read, spend, reset, or enforce account usage."}
    if args.output:
        print(write_new(args.output, summary))
    else:
        print(json.dumps(summary, ensure_ascii=False, indent=2))


def parser():
    root = argparse.ArgumentParser(description=__doc__)
    sub = root.add_subparsers(dest="command", required=True)
    cmd = sub.add_parser("inventory", help="Hash and fully decode images without altering them")
    cmd.add_argument("paths", nargs="+")
    cmd.add_argument("--role", choices=["source", "generated", "derivative"], default="source")
    cmd.add_argument("--output", required=True)
    cmd.set_defaults(run=inventory)
    cmd = sub.add_parser("prepare", help="Create an unexecuted built-in image-tool packet")
    cmd.add_argument("--action", choices=list(ACTIONS), required=True)
    cmd.add_argument("--id", required=True)
    cmd.add_argument("--input", action="append", default=[], help="ROLE=PATH, repeated in image-reference order; omit for source_setup")
    prompt_source = cmd.add_mutually_exclusive_group(required=True)
    prompt_source.add_argument("--request-file", help="Short request to wrap in the structured action template")
    prompt_source.add_argument("--prompt-file", help="Import an already-authored prompt verbatim; no template text is added")
    cmd.add_argument("--style-text-file")
    cmd.add_argument("--preserve", action="append", default=[], help="One explicit invariant; repeat for more; required except source_setup")
    cmd.add_argument("--constraint", action="append", default=[])
    cmd.add_argument("--parent-attempt", action="append", default=[])
    cmd.add_argument("--out-dir", required=True, help="New directory; existing directories are refused")
    cmd.set_defaults(run=prepare)
    cmd = sub.add_parser("record", help="Append one lifecycle event after validating provenance")
    cmd.add_argument("--ledger", required=True)
    cmd.add_argument("--packet", required=True)
    cmd.add_argument("--status", choices=sorted(STATUSES), required=True)
    cmd.add_argument("--output", action="append", default=[])
    notes = cmd.add_mutually_exclusive_group()
    notes.add_argument("--note", default="")
    notes.add_argument("--note-file")
    cmd.add_argument("--review-file")
    cmd.set_defaults(run=record)
    cmd = sub.add_parser("validate", help="Validate ledger chain, transitions, lineage, and image bytes")
    cmd.add_argument("--ledger", required=True)
    cmd.add_argument("--structure-only", action="store_true", help="Skip filesystem checks, e.g. when reviewing a relocated archive")
    cmd.set_defaults(run=validate)
    cmd = sub.add_parser("resume", help="Summarize saved state, optionally including a human resume plan")
    cmd.add_argument("--ledger", required=True)
    cmd.add_argument("--plan-file")
    cmd.add_argument("--output", help="New JSON report; omit to print")
    cmd.set_defaults(run=resume)
    return root


def main():
    args = parser().parse_args()
    try:
        args.run(args)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
