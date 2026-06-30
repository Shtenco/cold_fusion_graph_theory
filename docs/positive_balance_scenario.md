# Positive Balance Scenario

This document records the positive-balance numerical scenario from the model set. It is a simulation report, not an experimental claim and not an operational guide.

## Simulation horizon

| Parameter | Value |
|---|---:|
| simulated time | `100 h` |
| model step | `1 s` |
| initial external start input | `10 kW` |
| average angular speed | `200 rad/s` |
| average temperature | `1205.7 C` |
| maximum temperature | `1226.8 C` |

## Positive balance output

| Metric | Value |
|---|---:|
| average total model power | `1,981,415.6 W` |
| average component B net power | `7,188.9 W` |
| average component A power | `1,974,226.7 W` |
| average useful output power | `99,070.8 W` |
| gross component B energy | `0.845756 MWh` |
| net component B energy after factor 0.85 | `0.718893 MWh` |
| total modeled events | `8.23e21` |
| generated mass-scale product | `54,642.97 ng` |
| input component fraction | `0.068647%` |
| energy gain coefficient in this model | `3.5665481e7` |

## Interpretation

The positive result is a model-level result: it proves that the selected assumptions produce a positive computed balance inside the simulation. It does not by itself prove a physical device.

The proof chain used in the README is:

```math
(K,p,N)
\Rightarrow
(f_1,\ldots,f_6)
\Rightarrow
S_{graph}
\Rightarrow
\text{lower effective exponential barrier}
\Rightarrow
\text{positive balance in the numerical scenario}.
```
