#!/usr/bin/env python3
"""Check draft attribution and evidence eligibility; never claim semantic verification."""
import argparse
import json
from pathlib import Path
from validate_packet import validate

FORBIDDEN = ("保证盈利", "一定回本", "稳赚不赔", "战胜了99%", "你从未动摇", "亏损是成长的勋章", "千万别卖")

def validate_bundle(packet, bundle):
    errors = validate(packet)
    if bundle.get("customer_id") != packet.get("customer_id"):
        errors.append("bundle customer mismatch")
    if bundle.get("as_of") != packet.get("as_of"):
        errors.append("bundle as_of mismatch")
    if bundle.get("status") != "draft":
        errors.append("this generator only emits draft")
    if bundle.get("synthetic") != (packet.get("data_origin") == "synthetic"):
        errors.append("synthetic marker mismatch")
    facts = {f["id"]: f for f in packet.get("facts", [])}
    for field, child in (("letter", "paragraphs"), ("dossier", "sections")):
        if not isinstance(bundle.get(field, {}).get(child), list):
            errors.append("missing " + field + "." + child)
    if not isinstance(bundle.get("memories"), list):
        errors.append("memories must be a list")
    nodes = bundle.get("letter", {}).get("paragraphs", []) + bundle.get("dossier", {}).get("sections", []) + bundle.get("memories", [])
    for i, node in enumerate(nodes):
        if not node.get("text"):
            errors.append("empty text at node " + str(i))
        if not isinstance(node.get("evidence_ids"), list):
            errors.append("missing evidence_ids at node " + str(i))
        for fid in node.get("evidence_ids", []):
            f = facts.get(fid)
            if f is None:
                errors.append("unknown evidence " + str(fid))
            elif not (f.get("confirmed") is True and f.get("allowed_for_customer") is True):
                errors.append("ineligible evidence " + str(fid))
        for phrase in FORBIDDEN:
            if phrase in node.get("text", ""):
                errors.append("disallowed phrase at node " + str(i) + ": " + phrase)
    return errors

def main():
    p = argparse.ArgumentParser()
    p.add_argument("packet", type=Path)
    p.add_argument("bundle", type=Path)
    a = p.parse_args()
    packet = json.loads(a.packet.read_text(encoding="utf-8"))
    bundle = json.loads(a.bundle.read_text(encoding="utf-8"))
    errors = validate_bundle(packet, bundle)
    print(json.dumps({"valid": not errors, "errors": errors, "note": "Evidence IDs and simple phrases only; numbers, entailment, privacy and tone need review."}, ensure_ascii=False))
    raise SystemExit(bool(errors))

if __name__ == "__main__":
    main()
