# All Computed Values Table

This document collects the main values computed in the Information Graph Theory model.

## Core graph parameters

| Category | Quantity | Symbol / Key | Value | Notes |
|---|---|---|---:|---|
| graph | local connectivity | `K` | `6.0` | base graph parameter |
| graph | long-range connection probability | `p` | `4.8027e-42` | base graph parameter |
| graph | graph scale | `N` | `4.197668e+121` | base graph parameter |
| graph | critical product | `Kp` | `2.881620e-41` | `K * p` |
| graph | critical relation estimate | `N^(-1/3)` | `2.877381e-41` | comparison target |

## Structural functions

| Category | Quantity | Symbol / Key | Value | Notes |
|---|---|---|---:|---|
| structural | graph RG scale | `f1` | `104.37` | `Phi_RG(K,p,N)` |
| structural | logarithmic node factor | `f2` | `1.791759469` | `ln(K)` |
| structural | critical local scale | `f3` | `5.368072e-21` | `sqrt(Kp)` |
| structural | inverse long-range scale | `f4` | `2.082162e+41` | `1/p` |
| structural | graph regularity factor | `f5` | `3.348663759` | `K / ln(K)` |
| structural | correction factor | `f6` | `1.0527` | model correction |

## Main theory outputs

| Category | Quantity | Symbol / Key | Value | Units |
|---|---|---|---:|---|
| constants | fine-structure estimate | `alpha_graph` | `0.0072980714` | dimensionless |
| reference scale | mass-scale A estimate | `mass_scale_A_mev` | `105.602605` | MeV |
| reference scale | gain-scale A estimate | `gain_scale_A` | `8.825999e+06` | dimensionless |
| energy scale | first energy scale | `energy_scale_Q1_mev` | `3.282981` | MeV |
| energy scale | second energy scale | `energy_scale_Q2_mev` | `17.679351` | MeV |
| barrier scale | first barrier scale | `barrier_scale_B1_mev` | `0.476209` | MeV |
| barrier scale | second barrier scale | `barrier_scale_B2_mev` | `0.444076` | MeV |
| thermal scale | thermal value at 300 K | `thermal_scale_300K_ev` | `0.02585200` | eV |
| graph factors | factor A | `graph_factor_A` | `5.650970` | dimensionless |
| graph factors | factor B | `graph_factor_B` | `10.437000` | dimensionless |
| graph factors | factor C | `graph_factor_C` | `57.731231` | dimensionless |

## Positive-balance scenario values

| Category | Quantity | Symbol / Key | Value | Units |
|---|---|---|---:|---|
| balance | simulated horizon | `simulated_horizon` | `100` | h |
| balance | average total model power | `avg_total_model_power` | `1,981,415.6` | W |
| balance | average net component B | `avg_net_component_B` | `7,188.9` | W |
| balance | average component A | `avg_component_A` | `1,974,226.7` | W |
| balance | average useful output | `avg_useful_output` | `99,070.8` | W |
| balance | gross component B energy | `gross_component_B_energy` | `0.845756` | MWh |
| balance | net component B energy after factor 0.85 | `net_component_B_energy` | `0.718893` | MWh |
| balance | total modeled events | `total_modeled_events` | `8.23e21` | count |
| balance | generated mass-scale product | `generated_mass_scale_product` | `54,642.97` | ng |
| balance | input component consumption fraction | `input_component_fraction` | `0.068647` | % |
| balance | model energy gain coefficient | `model_energy_gain_coefficient` | `3.5665481e7` | dimensionless |

## Validation summaries

| Category | Summary | Value |
|---|---|---:|
| metavalidation | pass rate | `8/8 = 100.00%` |
| convergence | global status | `PASS` |
| convergence | max group spread threshold | `< 0.01%` |
