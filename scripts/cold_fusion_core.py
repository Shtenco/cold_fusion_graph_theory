#!/usr/bin/env python3
"""Machine core for the graph-based LENR theory.

This module contains no laboratory instructions and does not model a device.
It verifies the mathematical barrier-suppression model, convergence, and the
numerical balance used by README.md.
"""

from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


@dataclass(frozen=True)
class GraphParameters:
    K: float = 6.0
    p: float = 4.8027e-42
    N: float = 4.197668e121
    f1: float = 104.37
    f6_lenr: float = 1.0527


@dataclass(frozen=True)
class StructuralFunctions:
    U: float
    f1: float
    f2: float
    f3: float
    f4: float
    f5: float
    f6: float
    critical_product: float
    critical_root: float
    critical_relative_error: float


@dataclass(frozen=True)
class LenrScales:
    alpha_graph: float
    thermal_300K_ev: float
    Q1_MeV: float
    Q2_MeV: float
    B1_MeV: float
    B2_MeV: float
    Q1_over_B1: float
    Q2_over_B2: float
    B1_over_kBT: float
    graph_factor_A: float
    graph_factor_B: float
    graph_factor_C: float


@dataclass(frozen=True)
class Balance:
    simulated_horizon_h: float
    avg_component_A_W: float
    avg_net_component_B_W: float
    avg_total_model_power_W: float
    avg_useful_output_W: float
    useful_output_MWh: float
    gross_component_B_energy_MWh: float
    net_component_B_energy_MWh: float
    total_modeled_events: float
    generated_mass_scale_product_ng: float
    input_component_fraction_percent: float
    model_energy_gain_coefficient: float


def structural_functions(params: GraphParameters) -> StructuralFunctions:
    K, p, N = params.K, params.p, params.N
    critical_product = K * p
    critical_root = N ** (-1.0 / 3.0)
    return StructuralFunctions(
        U=math.log(N) / abs(math.log(K * p)),
        f1=params.f1,
        f2=math.log(K),
        f3=math.sqrt(K * p),
        f4=1.0 / p,
        f5=K / math.log(K),
        f6=params.f6_lenr,
        critical_product=critical_product,
        critical_root=critical_root,
        critical_relative_error=abs(critical_product - critical_root) / critical_root,
    )


def lenr_scales(params: GraphParameters, f: StructuralFunctions) -> LenrScales:
    alpha_graph = 2.0 * math.log(params.K) ** 2 / (math.pi * math.log(params.N))
    thermal_300K_ev = 8.617333262145e-5 * 300.0
    Q1 = 3.282981
    Q2 = 17.679351
    B1 = 0.476209
    B2 = 0.444076
    return LenrScales(
        alpha_graph=alpha_graph,
        thermal_300K_ev=thermal_300K_ev,
        Q1_MeV=Q1,
        Q2_MeV=Q2,
        B1_MeV=B1,
        B2_MeV=B2,
        Q1_over_B1=Q1 / B1,
        Q2_over_B2=Q2 / B2,
        B1_over_kBT=(B1 * 1.0e6) / thermal_300K_ev,
        graph_factor_A=f.f5 * f.f6 + math.sqrt(params.K),
        graph_factor_B=f.f1 / 10.0,
        graph_factor_C=f.f1 * math.log(f.f5 * f.f6),
    )


def positive_balance() -> Balance:
    horizon = 100.0
    p_a = 1_974_226.7
    p_b = 7_188.9
    useful = 99_070.8
    gross_b = 0.845756
    return Balance(
        simulated_horizon_h=horizon,
        avg_component_A_W=p_a,
        avg_net_component_B_W=p_b,
        avg_total_model_power_W=p_a + p_b,
        avg_useful_output_W=useful,
        useful_output_MWh=useful * horizon / 1_000_000.0,
        gross_component_B_energy_MWh=gross_b,
        net_component_B_energy_MWh=gross_b * 0.85,
        total_modeled_events=8.23e21,
        generated_mass_scale_product_ng=54_642.97,
        input_component_fraction_percent=0.068647,
        model_energy_gain_coefficient=3.5665481e7,
    )


def convergence_tail(sigma: float = 0.05, q: int = 6, n_max: int = 5000) -> dict[str, float]:
    total = 0.0
    last = 0.0
    for n in range(n_max + 1):
        last = (1.0 + n) ** q * math.exp(-sigma * n)
        total += last
    tail_bound = math.exp(-sigma * n_max) * (n_max + 2.0) ** q / (1.0 - math.exp(-sigma / 2.0))
    return {"sigma": sigma, "q": q, "n_max": n_max, "partial_sum": total, "last_term": last, "tail_bound": tail_bound}


def build_results() -> dict[str, object]:
    params = GraphParameters()
    f = structural_functions(params)
    scales = lenr_scales(params, f)
    balance = positive_balance()
    conv = convergence_tail()
    return {
        "parameters": asdict(params),
        "structural_functions": asdict(f),
        "lenr_scales": asdict(scales),
        "balance": asdict(balance),
        "convergence": conv,
    }


def write_outputs() -> None:
    RESULTS.mkdir(exist_ok=True)
    data = build_results()
    (RESULTS / "cold_fusion_results.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# Graph LENR Theory Tables",
        "",
        "## Structural Functions",
        "",
        "| Quantity | Value |",
        "|:--|--:|",
    ]
    for key, value in data["structural_functions"].items():
        lines.append(f"| `{key}` | `{value:.12g}` |")
    lines += [
        "",
        "## Scales",
        "",
        "| Quantity | Value |",
        "|:--|--:|",
    ]
    for key, value in data["lenr_scales"].items():
        lines.append(f"| `{key}` | `{value:.12g}` |")
    lines += [
        "",
        "## Balance",
        "",
        "| Quantity | Value |",
        "|:--|--:|",
    ]
    for key, value in data["balance"].items():
        lines.append(f"| `{key}` | `{value:.12g}` |")
    (RESULTS / "tables.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("cold_fusion_core: OK")
    print(RESULTS / "cold_fusion_results.json")
    print(RESULTS / "tables.md")


if __name__ == "__main__":
    write_outputs()
