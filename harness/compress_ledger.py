#!/usr/bin/env python3
"""Compress one ledger row. Run on every append. No model call."""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone

MAX_EVIDENCE = 140
MAX_BRANCH = 40
DECISIONS = frozenset({"prune", "advance", "escalate", "converge", "reopen", "suspect"})


def squash(text: str) -> str:
    text = text.replace("\r", " ").replace("\n", " ").replace("\t", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def clip(text: str, n: int) -> str:
    text = squash(text)
    if len(text) <= n:
        return text
    return text[: n - 1].rstrip() + "…"


def compress(branch: str, decision: str, evidence: str, ts: str | None = None) -> str:
    decision = squash(decision).lower()
    if decision not in DECISIONS:
        decision = "suspect"
    branch = clip(branch, MAX_BRANCH).replace("|", "/")
    evidence = clip(evidence, MAX_EVIDENCE).replace("|", "/")
    if not ts:
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return f"| {ts} | {branch} | {decision} | {evidence} |"


def main() -> int:
    p = argparse.ArgumentParser(description="Compress a ledger row")
    p.add_argument("--branch", required=True)
    p.add_argument("--decision", required=True)
    p.add_argument("--evidence", required=True)
    p.add_argument("--ts")
    p.add_argument("--file", help="Append to this ledger if set")
    args = p.parse_args()
    row = compress(args.branch, args.decision, args.evidence, args.ts)
    if args.file:
        header = "| ts | branch | decision | evidence |\n|---|---|---|---|\n"
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                existing = f.read()
        except FileNotFoundError:
            existing = ""
        with open(args.file, "a", encoding="utf-8") as f:
            if "| ts | branch | decision | evidence |" not in existing:
                f.write(header)
            f.write(row + "\n")
    print(row)
    return 0


if __name__ == "__main__":
    sys.exit(main())
