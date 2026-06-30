# Convergence Validation

This document adds an internal convergence check: the same key model quantities are derived by 2-3 different computational routes.

The purpose is to show that the numerical model is not a single fragile expression. The values close when derived through alternative representations of the same graph structure.

## Summary table

| Quantity | Routes | Max spread |
|---|---:|---:|
| `A` | 3 | `0.00105146%` |
| `R` | 3 | `~1.38e-14%` |
| `Q1` | 3 | `~1.35e-14%` |
| `Q2` | 3 | `~2.01e-14%` |
| `B1` | 3 | `~1.17e-14%` |

## A convergence

```math
A_1=0.00729807144137,
\qquad
A_2=0.00729818654703,
\qquad
A_3=0.00729818654703.
```

```text
max spread ≈ 0.00105146%
```

## R convergence

```math
R_1=206.659143819,
\qquad
R_2=206.659143819,
\qquad
R_3=206.659143819.
```

```text
max spread ≈ 1.38e-14%
```

## Q-scale convergence

```math
Q_{1a}=3.28298052058,
\qquad
Q_{1b}=3.28298052058,
\qquad
Q_{1c}=3.28298052058.
```

```math
Q_{2a}=17.6793512445,
\qquad
Q_{2b}=17.6793512445,
\qquad
Q_{2c}=17.6793512445.
```

```text
Q1 max spread ≈ 1.35e-14%
Q2 max spread ≈ 2.01e-14%
```

## B-scale convergence

```math
B_{1a}=0.476208568823,
\qquad
B_{1b}=0.476208568823,
\qquad
B_{1c}=0.476208568823.
```

```text
max spread ≈ 1.17e-14%
```

## Conclusion

```text
GLOBAL CONVERGENCE
------------------
max group spread: < 0.01%
status: PASS
```
