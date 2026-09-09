"""Provenance, lifecycle, and preservation checks; no network or generated artwork."""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import struct
import tempfile
import unittest
import zlib

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("legacyify", HERE / "legacyify.py")
L = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(L)


def fixture_png(path, width=2, height=3, color=b"\x14\x35\x55"):
    """Minimal RGB test fixture assembled as PNG bytes, not campaign image work."""
    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))
    data = b"\x89PNG\r\n\x1a\n"
    data += chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
    data += chunk(b"IDAT", zlib.compress((b"\x00" + color * width) * height))
    data += chunk(b"IEND", b"")
    path.write_bytes(data)
    return path


class WorkflowChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="test-", dir=HERE)
        self.root = Path(self.temp.name)
        self.source = fixture_png(self.root / "source.png")
        self.style = fixture_png(self.root / "style.png", color=b"\xaa\x77\x11")
        self.output = fixture_png(self.root / "output.png", width=4, height=6)
        self.source_bytes = self.source.read_bytes()
        self.prompt = self.root / "authored.txt"
        self.prompt.write_text("  Exact authored prompt.\nPreserve identity.\n", encoding="utf-8")
        self.ledger = self.root / "ledger.jsonl"
        self.packet_dir = self.root / "packet-a1"
        self.call("prepare", "--action", "character", "--id", "a1", "--input", f"target={self.source}", "--input", f"style={self.style}", "--prompt-file", self.prompt, "--preserve", "Identity", "--out-dir", self.packet_dir)
        self.packet = self.packet_dir / "packet.json"

    def tearDown(self):
        self.temp.cleanup()

    def call(self, *args):
        parsed = L.parser().parse_args([str(x) for x in args])
        with contextlib.redirect_stdout(io.StringIO()) as out:
            parsed.run(parsed)
        return out.getvalue()

    def record(self, status, *args):
        return self.call("record", "--ledger", self.ledger, "--packet", self.packet, "--status", status, *args)

    def success(self):
        self.record("started")
        self.record("succeeded", "--output", self.output)

    def test_full_cycle_preserves_sources_exact_prompt_and_lineage(self):
        manifest = self.root / "inventory.json"
        self.call("inventory", self.source, "--output", manifest)
        self.assertEqual(L.read_json(manifest)["assets"][0]["height"], 3)
        packet = L.load_packet(self.packet)
        self.assertEqual(packet["prompt"], self.prompt.read_text(encoding="utf-8"))
        self.success()
        review = self.root / "review.json"
        review.write_text(json.dumps({"verdict": "conditional", "notes": "Test fixture only"}), encoding="utf-8")
        self.record("reviewed", "--review-file", review)
        report = json.loads(self.call("validate", "--ledger", self.ledger))
        self.assertTrue(report["valid"])
        events = L.read_ledger(self.ledger, check_files=True)
        self.assertEqual(events[1]["outputs"][0]["input_sha256"][0], hashlib.sha256(self.source_bytes).hexdigest())
        self.assertEqual(self.source.read_bytes(), self.source_bytes)
        state = json.loads(self.call("resume", "--ledger", self.ledger))
        self.assertEqual(state["status_counts"], {"reviewed": 1})
        self.assertEqual(len(state["attempts"][0]["outputs"]), 1)
        self.assertEqual(state["last_event_sha256"], events[-1]["event_sha256"])

    def test_source_modification_blocks_next_event(self):
        self.record("started")
        previous = self.ledger.read_bytes()
        fixture_png(self.source, color=b"\xff\x00\x00")
        with self.assertRaisesRegex(ValueError, "differs from recorded original"):
            self.record("succeeded", "--output", self.output)
        self.assertEqual(self.ledger.read_bytes(), previous)

    def test_output_modification_is_detected(self):
        self.success()
        fixture_png(self.output, width=5)
        with self.assertRaisesRegex(ValueError, "differs from recorded original"):
            self.call("validate", "--ledger", self.ledger)

    def test_ledger_tampering_is_detected(self):
        self.success()
        value = self.ledger.read_text(encoding="utf-8").replace('"notes":""', '"notes":"altered"', 1)
        self.ledger.write_text(value, encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Hash chain mismatch"):
            self.call("validate", "--ledger", self.ledger)

    def test_valid_but_changed_packet_cannot_rewrite_attempt(self):
        self.record("started")
        previous = self.ledger.read_bytes()
        packet = L.read_json(self.packet)
        packet["prompt"] += " Changed instruction."
        packet["prompt_sha256"] = L.digest_bytes(packet["prompt"].encode("utf-8"))
        packet["tool_arguments"]["prompt"] = packet["prompt"]
        self.packet.write_text(json.dumps(packet), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "changed between events"):
            self.record("failed")
        self.assertEqual(self.ledger.read_bytes(), previous)

    def test_invalid_transition_does_not_append(self):
        self.success()
        previous = self.ledger.read_bytes()
        with self.assertRaisesRegex(ValueError, "Invalid transition"):
            self.record("started")
        self.assertEqual(self.ledger.read_bytes(), previous)

    def test_corrupt_image_cannot_enter_inventory(self):
        bad = self.root / "broken.png"
        bad.write_bytes(self.source_bytes[:45])
        with self.assertRaises(ValueError):
            self.call("inventory", bad, "--output", self.root / "bad.json")
        self.assertFalse((self.root / "bad.json").exists())

    def test_concurrent_writer_is_refused(self):
        lock = self.ledger.with_suffix(".jsonl.lock")
        lock.write_text("", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "locked by another writer"):
            self.record("started")
        self.assertTrue(lock.exists())
        self.assertFalse(self.ledger.exists())

    def test_together_requires_identity_and_has_no_partial_packet(self):
        folder = self.root / "invalid-together"
        with self.assertRaisesRegex(ValueError, "identity reference"):
            self.call("prepare", "--action", "together", "--id", "a2", "--input", f"target={self.source}", "--prompt-file", self.prompt, "--preserve", "Geometry", "--out-dir", folder)
        self.assertFalse(folder.exists())

    def test_incomplete_attempt_has_resume_marker(self):
        self.record("started")
        state = json.loads(self.call("resume", "--ledger", self.ledger))
        self.assertEqual(state["incomplete_attempts"], ["a1"])
        self.record("interrupted", "--note", "Tool stopped before result")
        state = json.loads(self.call("resume", "--ledger", self.ledger))
        self.assertEqual(state["incomplete_attempts"], [])
        self.assertEqual(state["status_counts"], {"interrupted": 1})

    def test_source_setup_generates_packet_without_reference_arguments(self):
        folder = self.root / "setup-e1"
        self.call("prepare", "--action", "source_setup", "--id", "E01", "--prompt-file", self.prompt, "--out-dir", folder)
        packet_path = folder / "packet.json"
        packet = L.load_packet(packet_path)
        self.assertEqual(packet["inputs"], [])
        self.assertEqual(packet["tool_arguments"], {"prompt": self.prompt.read_text(encoding="utf-8")})
        for status in ["started", "succeeded"]:
            extras = ("--output", self.output) if status == "succeeded" else ()
            self.call("record", "--ledger", self.ledger, "--packet", packet_path, "--status", status, *extras)
        events = L.read_ledger(self.ledger, check_files=True)
        self.assertEqual(events[-1]["outputs"][0]["input_sha256"], [])

    def test_only_source_setup_accepts_zero_references(self):
        for action in ("character", "scene", "together"):
            with self.assertRaisesRegex(ValueError, "Exactly one target"):
                self.call("prepare", "--action", action, "--id", "Z01", "--prompt-file", self.prompt, "--preserve", "Identity", "--out-dir", self.root / action)
        with self.assertRaisesRegex(ValueError, "zero image references"):
            self.call("prepare", "--action", "source_setup", "--id", "E02", "--input", f"target={self.source}", "--prompt-file", self.prompt, "--out-dir", self.root / "wrong-setup")


if __name__ == "__main__":
    unittest.main(verbosity=2)
