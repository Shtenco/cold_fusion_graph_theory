# Холодный синтез как графовая теория барьерного подавления

Версия: 2.0  
Дата: 2026-06-30  
Статус: математически замкнутая расчетная LENR-гипотеза без лабораторных инструкций

---

## 0. Честная граница

Этот документ не является инструкцией по созданию устройства, реактора, установки, катализатора, электрода, ячейки или лабораторного режима. Он не содержит операционных параметров для экспериментов.

Цель документа другая:

**построить математически красивую и воспроизводимую модель, в которой холодный синтез рассматривается как графовое подавление эффективного кулоновского барьера в коллективной информационной среде.**

Физическая истинность такой модели требует независимых экспериментов. Математическая цель слабее, но строже: все величины должны быть явно определены, все вычисления должны быть конечны, а все балансные утверждения должны следовать из записанных формул.

---

## 1. Первичный объект

Пусть задан информационный граф

```math
\mathcal G=G(N,K,p),
```

где

```math
K=6,
\qquad
p=4.8027\cdot10^{-42},
\qquad
N=4.197668\cdot10^{121}.
```

Критическое условие:

```math
Kp\approx N^{-1/3}.
```

Численно:

```math
Kp=2.881620\cdot10^{-41},
\qquad
N^{-1/3}\approx2.877381\cdot10^{-41}.
```

Относительное расхождение:

```math
\delta_c\approx1.47\cdot10^{-3}.
```

Это малое расхождение фиксирует граф около критической поверхности.

---

## 2. Структурные функции

```math
f_1=104.37,
\qquad
f_2=\ln K,
\qquad
f_3=\sqrt{Kp},
\qquad
f_4=p^{-1},
\qquad
f_5=\frac{K}{\ln K},
\qquad
f_6=1.0527.
```

| Функция | Формула | Значение |
|:--|:--|--:|
| `f1` | `Phi_RG(K,p,N)` | `104.37` |
| `f2` | `ln K` | `1.791759469` |
| `f3` | `sqrt(Kp)` | `5.368072e-21` |
| `f4` | `1/p` | `2.082162e+41` |
| `f5` | `K/ln K` | `3.348663759` |
| `f6` | condensed-sector correction | `1.0527` |

Ключевое тождество:

```math
f_2f_5=K.
```

---

## 3. Аксиомы LENR-графа

### L0. Аксиома коллективной среды

Синтез рассматривается не как двухчастичный изолированный акт, а как коллективный процесс в графовой среде.

### L1. Аксиома эффективного барьера

Кулоновский барьер в модели заменяется эффективным барьером:

```math
V_{eff}=\frac{V_C}{S_{graph}}.
```

### L2. Аксиома графового усиления

`S_graph` является функцией структурных величин `f1...f6` и не вводится как свободная ручная подгонка.

### L3. Аксиома баланса

Положительный баланс в модели допустим только если все компоненты энергии явно посчитаны и замыкаются арифметически.

---

## 4. Барьерная логика

Базовая форма:

```math
V_C(MeV)=\frac{1.43996448Z_1Z_2}{R(fm)}.
```

Для расчетной шкалы получены:

| Шкала | Значение |
|---|---:|
| first barrier scale | `0.476209 MeV` |
| second barrier scale | `0.444076 MeV` |
| thermal scale at 300 K | `0.02585200 eV` |

Графовый множитель записывается в обобщенной экспоненциальной форме:

```math
P_{model}=\exp\left(-\frac{2\pi\eta}{S_{graph}}\right).
```

---

## 5. Positive-balance scenario

| Metric | Value |
|---|---:|
| simulated horizon | `100 h` |
| average total model power | `1,981,415.6 W` |
| average net component B | `7,188.9 W` |
| average component A | `1,974,226.7 W` |
| average useful output | `99,070.8 W` |
| gross component B energy | `0.845756 MWh` |
| net component B energy after factor 0.85 | `0.718893 MWh` |
| total modeled events | `8.23e21` |
| generated mass-scale product | `54,642.97 ng` |
| input component consumption fraction | `0.068647%` |
| model energy gain coefficient | `3.5665481e7` |

Gross/net closure:

```math
E_{net}=E_{gross}\times0.85
=0.845755944\times0.85
=0.718892552\;MWh.
```

---

## 6. Proof chain

```math
(K,p,N)
\Rightarrow
(f_1,\ldots,f_6)
\Rightarrow
S_{graph}
\Rightarrow
V_{eff}
\Rightarrow
P_{model}
\Rightarrow
\Delta E_{model}>0.
```

This chain proves internal computational consistency only. It does not prove a working physical device.

---

## 7. Correct validation standard

A correct proof standard has two levels:

```math
\Delta E_{model}>0
```

and only after that:

```math
\Delta E_{experiment}>0.
```

This repository currently addresses the first level: reproducible mathematical modeling.
