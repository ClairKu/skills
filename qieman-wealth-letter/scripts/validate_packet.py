#!/usr/bin/env python3
"""Validate one customer packet. No network, persistence or investment advice."""
import argparse
import datetime as dt
import json
from decimal import Decimal
from pathlib import Path

def validate(packet):
    errors = []
    cid = packet.get("customer_id")
    if not isinstance(cid, str) or not cid.strip():
        errors.append("customer_id is required")
    if packet.get("data_origin") not in ("synthetic", "approved_customer_export"):
        errors.append("data_origin must identify synthetic or approved_customer_export")
    auth = packet.get("authorization", {})
    if not auth.get("purpose") or auth.get("customer_content_allowed") is not True:
        errors.append("customer content authorization is missing")
    try:
        asof = dt.date.fromisoformat(packet["as_of"])
        start = dt.date.fromisoformat(packet["period"]["start"])
        end = dt.date.fromisoformat(packet["period"]["end"])
        if not start <= end <= asof:
            errors.append("period must satisfy start <= end <= as_of")
        if packet["period"].get("complete_calendar_year"):
            if not (start.month == 1 and start.day == 1 and end.month == 12 and end.day == 31 and start.year == end.year):
                errors.append("complete_calendar_year does not cover one calendar year")
    except (KeyError, TypeError, ValueError):
        errors.append("valid ISO dates and period are required")
    if not packet.get("scope"):
        errors.append("scope is required")
    seen = set()
    for fact in packet.get("facts", []):
        fid = fact.get("id")
        if not fid or fid in seen:
            errors.append("fact IDs must be present and unique")
        seen.add(fid)
        if fact.get("customer_id") != cid:
            errors.append("cross-customer fact: " + str(fid))
        if fact.get("kind") not in ("system", "customer_confirmed", "derived"):
            errors.append("unknown fact kind: " + str(fid))
        for field in ("text", "source", "observed_at"):
            if not fact.get(field):
                errors.append("fact missing " + field + ": " + str(fid))
        if fact.get("kind") == "derived" and (not fact.get("input_ids") or not fact.get("formula")):
            errors.append("derived fact requires formula and input_ids: " + str(fid))
    for fact in packet.get("facts", []):
        for fid in fact.get("input_ids", []):
            if fid not in seen:
                errors.append("unknown derived input: " + str(fid))
    account = packet.get("account")
    if account:
        if account.get("bridge_type") != "simplified_reconciled":
            errors.append("only a declared simplified_reconciled asset bridge can be checked")
        if account.get("currency") != "CNY":
            errors.append("asset bridge example only supports CNY")
        try:
            values = [Decimal(str(account[k])) for k in ("opening", "inflow", "outflow", "investment_pnl", "closing")]
            opening, inflow, outflow, pnl, closing = values
            if not all(v.is_finite() for v in values):
                errors.append("asset bridge numbers must be finite")
            elif abs(opening + inflow - outflow + pnl - closing) > Decimal("0.01"):
                errors.append("asset bridge does not reconcile")
            if inflow < 0 or outflow < 0:
                errors.append("inflow and outflow must be nonnegative")
        except (KeyError, ValueError, ArithmeticError):
            errors.append("asset bridge fields must be numeric and complete")
        for fid in account.get("evidence_ids", []):
            if fid not in seen:
                errors.append("asset bridge references unknown fact: " + str(fid))
    return errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("packet", type=Path)
    args = parser.parse_args()
    packet = json.loads(args.packet.read_text(encoding="utf-8"))
    errors = validate(packet)
    print(json.dumps({"valid": not errors, "errors": errors, "note": "Format and simple reconciliation only; semantic review remains required."}, ensure_ascii=False))
    raise SystemExit(bool(errors))

if __name__ == "__main__":
    main()
