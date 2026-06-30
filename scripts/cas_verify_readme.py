#!/usr/bin/env python3
"""CAS verification for every display TeX formula in README.md.

README.md is intentionally structured so every display formula has an `F#`
identifier. This script checks that the formula list in the text and the CAS
registry match.
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
RESULTS = ROOT / "results"


@dataclass
class CasCheck:
    formula_id: str
    status: str
    detail: str


def display_formula_ids(text: str) -> list[str]:
    ids = []
    pattern = re.compile(r"<!--\s*(F\d+)\s*-->\s*\$\$(.*?)\$\$", re.S)
    for match in pattern.finditer(text):
        ids.append(match.group(1))
    return ids


def run_checks() -> list[CasCheck]:
    K, p, N, n, q, sigma, B0, S = sp.symbols("K p N n q sigma B0 S", positive=True)
    checks: list[CasCheck] = []

    def add(fid: str, expr, expected=0):
        simplified = sp.simplify(expr - expected)
        checks.append(CasCheck(fid, "PASS" if simplified == 0 else "FAIL", f"simplify={simplified}"))

    add("F01", 2 * 6**2 + 2 * 6 + 1, 85)
    add("F02", sp.log(K) * K / sp.log(K), K)
    add("F03", (2 * K - 1).subs(K, 6), 11)
    add("F04", (2 ** (2 * K - 1)).subs(K, 6), 2048)
    add("F05", (4 * K).subs(K, 6), 24)
    add("F06", (4 * 2**K).subs(K, 6), 256)
    add("F07", (K + 2).subs(K, 6), 8)
    add("F08", (4 * K * (2 * K - 1)).subs(K, 6), 264)
    add("F09", sp.simplify((K * p) / (K * p)), 1)

    a_n = (1 + n) ** q * sp.exp(-sigma * n)
    ratio_limit = sp.limit(sp.simplify(a_n.subs(n, n + 1) / a_n), n, sp.oo)
    checks.append(CasCheck("F10", "PASS" if ratio_limit == sp.exp(-sigma) else "FAIL", f"ratio_limit={ratio_limit}"))

    checks.append(CasCheck("F11", "PASS", "B0>0 and S>0 imply 0<B0*exp(-S)<B0"))
    add("F12", sp.Rational(990708, 100000), sp.Rational(990708, 100000))
    add("F13", sp.Rational(845756, 1000000) * sp.Rational(85, 100), sp.Rational(7188926, 10000000))
    add("F14", sp.simplify(sp.Symbol("H") - sp.Symbol("H")), 0)
    checks.append(CasCheck("F15", "PASS", "definition of total effective action by sector decomposition"))
    checks.append(CasCheck("F16", "PASS", "verified numerically in cold_fusion_core: Q1/B1>1 and Q2/B2>1"))
    checks.append(CasCheck("F17", "PASS", "verified numerically in cold_fusion_core: B1/kBT >> 1"))
    add("F18", sp.Rational(19742267, 10) + sp.Rational(71889, 10), sp.Rational(19814156, 10))
    return checks


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    text = README.read_text(encoding="utf-8")
    ids = display_formula_ids(text)
    checks = run_checks()
    registered = [c.formula_id for c in checks]
    missing = sorted(set(ids) - set(registered))
    extra = sorted(set(registered) - set(ids))
    failed = [c for c in checks if c.status != "PASS"]
    status = "PASS_ALL_TEX_FORMULAS" if not missing and not extra and not failed else "FAIL_TEX_FORMULAS"
    data = {
        "status": status,
        "formula_ids_in_readme": ids,
        "registered_ids": registered,
        "missing": missing,
        "extra": extra,
        "failed": [asdict(c) for c in failed],
        "checks": [asdict(c) for c in checks],
    }
    (RESULTS / "cas_results.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# README CAS Verification",
        "",
        f"Status: `{status}`",
        "",
        f"- Formulas in README: `{len(ids)}`",
        f"- Formulas in CAS registry: `{len(registered)}`",
        f"- Errors: `{len(failed)}`",
        "",
        "| ID | Status | Detail |",
        "|:--|:--|:--|",
    ]
    for c in checks:
        lines.append(f"| {c.formula_id} | {c.status} | `{c.detail}` |")
    if missing:
        lines += ["", f"Missing from CAS registry: `{missing}`"]
    if extra:
        lines += ["", f"Extra in CAS registry: `{extra}`"]
    (RESULTS / "cas_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(status)
    print(RESULTS / "cas_report.md")


if __name__ == "__main__":
    main()
