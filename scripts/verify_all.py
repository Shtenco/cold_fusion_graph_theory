#!/usr/bin/env python3
"""Unified verification for the cold_fusion_graph_theory package."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def run(script: str) -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / script)], check=True, cwd=str(ROOT))


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    run("cold_fusion_core.py")
    run("cas_verify_readme.py")
    core = json.loads((RESULTS / "cold_fusion_results.json").read_text(encoding="utf-8"))
    cas = json.loads((RESULTS / "cas_results.json").read_text(encoding="utf-8"))

    checks = []
    f = core["structural_functions"]
    scales = core["lenr_scales"]
    balance = core["balance"]
    checks.append(("critical_relation", f["critical_relative_error"] < 0.002))
    checks.append(("barrier_order_Q1", scales["Q1_over_B1"] > 1.0))
    checks.append(("barrier_order_Q2", scales["Q2_over_B2"] > 1.0))
    checks.append(("thermal_suppression", scales["B1_over_kBT"] > 1.0e6))
    checks.append(("balance_closure", abs(balance["avg_component_A_W"] + balance["avg_net_component_B_W"] - balance["avg_total_model_power_W"]) < 1e-6))
    checks.append(("cas", cas["status"] == "PASS_ALL_TEX_FORMULAS"))

    status = "PASS_COLD_FUSION_PACKAGE" if all(v for _, v in checks) else "FAIL_COLD_FUSION_PACKAGE"
    lines = ["# Final cold_fusion_graph_theory Verification", "", f"Status: `{status}`", "", "| Check | Status |", "|:--|:--|"]
    for name, value in checks:
        lines.append(f"| {name} | {'PASS' if value else 'FAIL'} |")
    (RESULTS / "verification_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(status)
    print(RESULTS / "verification_report.md")
    if status.startswith("FAIL"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
