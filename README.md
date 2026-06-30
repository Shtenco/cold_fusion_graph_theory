# SHTENCO Cold Fusion Graph Theory

This repository now contains only the **synthesis/LENR-specific interpretation** of the information graph model.

The base mathematical theory, convergence framework, general constants, audit kit, and graph-theory materials have been moved to:

```text
https://github.com/Shtenco/info_graph_theory
```

---

## Boundary

This repository is a theoretical and numerical hypothesis repository. It is **not** a laboratory manual and does not contain instructions for building a reactor, electrode, cell, installation, catalyst, or operating regime.

The goal is narrower:

> to describe a mathematical model where low-energy synthesis is interpreted as graph-mediated suppression of an effective barrier in a collective information medium.

Physical truth requires independent experiments, controlled measurements, and specialist review.

---

## Core synthesis document

The synthesis-specific document is here:

[`docs/cold_fusion_graph_theory.md`](./docs/cold_fusion_graph_theory.md)

---

## Shared base theory

The synthesis model uses the same base graph object:

```math
\mathcal G=G(N,K,p),
```

with

```math
K=6,
\qquad
p=4.8027\cdot10^{-42},
\qquad
N=4.197668\cdot10^{121}.
```

Critical relation:

```math
Kp\approx N^{-1/3}.
```

The general theory behind this object belongs to `Shtenco/info_graph_theory`.

---

## Synthesis-specific structural functions

| Function | Formula / role | Value |
|---:|---|---:|
| `f1` | graph RG scale | `104.37` |
| `f2` | `ln(K)` | `1.791759469` |
| `f3` | `sqrt(Kp)` | `5.368072e-21` |
| `f4` | `1/p` | `2.082162e+41` |
| `f5` | `K/ln(K)` | `3.348663759` |
| `f6` | condensed-sector correction | `1.0527` |

---

## Positive-balance numerical scenario

| Metric | Value |
|---|---:|
| simulated horizon | `100 h` |
| average total model power | `1,981,415.6 W` |
| average net component B | `7,188.9 W` |
| average component A | `1,974,226.7 W` |
| average useful output | `99,070.8 W` |
| gross component B energy | `0.845756 MWh` |
| net component B energy after factor `0.85` | `0.718893 MWh` |
| total modeled events | `8.23e21` |
| generated mass-scale product | `54,642.97 ng` |
| input component consumption fraction | `0.068647%` |
| model energy gain coefficient | `3.5665481e7` |

---

## Model proof chain

```math
(K,p,N)
\Rightarrow
(f_1,\ldots,f_6)
\Rightarrow
S_{graph}
\Rightarrow
\text{effective barrier reduction in the model}
\Rightarrow
\text{positive numerical balance}.
```

This is a computational consistency chain, not an experimental proof.

---

## Files

| File | Purpose |
|---|---|
| `docs/cold_fusion_graph_theory.md` | synthesis-specific graph-theory hypothesis |
| `docs/positive_balance_scenario.md` | positive-balance numerical scenario report |

---

## Notes

All non-synthesis information-graph-theory materials should live in:

```text
Shtenco/info_graph_theory
```

This repository keeps only the synthesis-specific layer.
