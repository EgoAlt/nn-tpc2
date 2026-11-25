# nn-tpc2

Code for Homework 2 (TPC 2) of Nanotechnologies and Nanoelectronics at Instituto Superior Técnico (IST), 2026/27: "Cook it in the cleanroom". The group's report makes a chameleon-inspired photonic crystal in the cleanroom: a triangular lattice of amorphous silicon (a-Si) pillars in polydimethylsiloxane (PDMS), written by electron-beam lithography (EBL) in hydrogen silsesquioxane (HSQ) resist. This script estimates the bottleneck and draws the report's plot.

## Layout

- `bottleneck_plot.py`: computes the total fabrication time against the patterned area for EBL at 100 pA, EBL at 1 nA (the report's choice) and a parallel wafer process (nanoimprint or deep-UV (DUV) lithography). It marks the 1 cm² totals and writes the report's figure, `bottleneck.png`, plus a vector copy, `bottleneck-plot.pdf`.

## Running it

```
python3 bottleneck_plot.py
```

Needs Python 3 with NumPy and Matplotlib. It runs in a few seconds and writes both files to the current folder.

## The model

EBL writes one spot at a time, so the write time is the charge the resist needs divided by the beam current:

$$t_{\text{EBL}} = \frac{D\,f\,A}{I}$$

The other steps (deposition, spin, etch, PDMS and release) run on a whole wafer at once. They add $t_{\text{other}}$ for each 100 mm wafer, and the area $A$ needs $\lceil A / 45\ \text{cm}^2 \rceil$ wafers. The parallel line counts only these batch steps, so it treats the patterning time of nanoimprint or DUV as negligible.

| Input | Value | Source |
|---|---|---|
| HSQ resist dose, $D$ | 1000 µC/cm² | Grigorescu and Hagen (2009) |
| Exposed fraction, $f$ | 0.24 | the lattice: $a$ = 393 nm, $d$ = 202 nm |
| Beam current, $I$ | 100 pA (fine), 1 nA (coarse) | the week-2 lecture |
| Batch steps per wafer, $t_{\text{other}}$ | 3.5 h | the report's recipe card |
| Devices per 100 mm wafer | 45 one-centimeter devices | the week-2 lecture |

At 1 cm² the totals are 2.9 days at 1 nA and 27.9 days at 100 pA. EBL is 95% of the time at 1 nA and 99.5% at 100 pA.
