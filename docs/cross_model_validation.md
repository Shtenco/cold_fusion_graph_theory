# Cross-Model Validation

This document describes the metamodel used to check whether the numerical model is internally self-consistent.

The validation does not claim experimental confirmation. It proves that the published calculation tables, graph constants, barrier estimates, and positive-balance scenario close under independent arithmetic checks.

## Independent checks

| Check | Meaning | Result |
|---|---|---:|
| `critical_graph_relation` | compares `Kp` with `N^(-1/3)` | PASS |
| `alpha_reference_cross_check` | compares the graph estimate against reference value | PASS |
| `mass_scale_A_cross_check` | compares graph mass-scale estimate against reference value | PASS |
| `q_values_cross_check` | checks the two graph Q-scale estimates | PASS |
| `barrier_scale_check` | checks that barrier scale is positive and far above 300 K thermal scale | PASS |
| `balance_power_closure` | checks `component A + component B net = total` | PASS |
| `gross_to_net_balance_closure` | checks `gross component B × efficiency = net component B` | PASS |
| `positive_output_check` | checks that useful output and total model value are positive | PASS |

## Important gross/net correction

```math
E_{B,gross}=0.845755944\;MWh
```

```math
E_{B,net}=E_{B,gross}\times0.85\approx0.718893\;MWh.
```

This matches the net average component used in the positive-balance table:

```math
P_{B,net}\times100h
=7188.9W\times100h
=0.718890\;MWh.
```

## Metamodel conclusion

```text
PASS RATE: 8/8 = 100.00%
```
