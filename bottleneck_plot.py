import numpy as np
import matplotlib.pyplot as plt

# Parameters matching Sections 3 and 4 (2D a-Si pillar lattice in PDMS: a = 393 nm, d = 202 nm, gap = 191 nm)
f = 0.24              # exposed area filling fraction (negative resist HSQ)
D = 1000e-6           # C/cm^2 (1000 uC/cm^2 for HSQ)
I_fine = 100e-12      # A (100 pA, fine)
I_coarse = 1e-9       # A (1 nA, coarse: enough, because the color depends on the period, not the pillar size)
t_other_h = 3.5       # h (parallel wafer steps per 100-mm wafer)
devices_per_wafer = 45  # one-centimeter devices per 100-mm wafer (Section 4)

A = np.logspace(-2, 2, 300)  # 1 mm^2 to 100 cm^2

n_wafers = np.ceil(A / devices_per_wafer)  # wafers needed to hold area A
t_fine_h = (D * f * A / I_fine) / 3600.0 + n_wafers * t_other_h
t_coarse_h = (D * f * A / I_coarse) / 3600.0 + n_wafers * t_other_h
t_parallel_h = n_wafers * t_other_h

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans", "Arial", "Helvetica"],
    "font.size": 9,
    "axes.linewidth": 0.9,
})

fig, ax = plt.subplots(figsize=(4.4, 3.0), dpi=300)

ax.loglog(A, t_fine_h, color="#c0392b", lw=2.2, label=r"EBL fine ($100\ \mathrm{pA}$)")
ax.loglog(A, t_coarse_h, color="#e67e22", lw=1.8, label=r"EBL coarse ($1\ \mathrm{nA}$, our choice)")
ax.loglog(A, t_parallel_h, color="#2b5c8f", lw=2.0, drawstyle="steps-post", label=r"Parallel wafer process (nanoimprint / DUV)")

for y_h, lbl in [(1.0, "1 h"), (24.0, "1 day"), (24*30.0, "1 mo"), (24*365.0, "1 yr")]:
    ax.axhline(y_h, color="#e5e5e5", lw=0.8, zorder=0)
    ax.text(88, y_h * 1.12, lbl, color="#777777", fontsize=7.5, ha="right", va="bottom")

t_1cm2_fine = (D * f * 1.0 / I_fine) / 3600.0 + t_other_h
t_1cm2_coarse = (D * f * 1.0 / I_coarse) / 3600.0 + t_other_h
ax.plot(1.0, t_1cm2_fine, "o", color="#c0392b", ms=5, zorder=4)
ax.annotate(f"{t_1cm2_fine / 24:.1f} d\n(1 cm²)", (1.0, t_1cm2_fine), xytext=(-46, 8),
            textcoords="offset points", fontsize=7.5, color="#c0392b", fontweight="bold",
            arrowprops=dict(arrowstyle="-", color="#c0392b", lw=0.7))

ax.plot(1.0, t_1cm2_coarse, "o", color="#e67e22", ms=4.5, zorder=4)
ax.annotate(f"{t_1cm2_coarse / 24:.1f} d", (1.0, t_1cm2_coarse), xytext=(8, -11),
            textcoords="offset points", fontsize=7.5, color="#b35900")

ax.set_xlim(1e-2, 1e2)
ax.set_ylim(0.6, 5e5)
ax.set_xticks([1e-2, 1e-1, 1, 10, 100])
ax.set_xticklabels(["1 mm²", "10 mm²", "1 cm²", "10 cm²", "100 cm²"])
ax.set_xlabel(r"Patterned photonic crystal area $A$", labelpad=4)
ax.set_ylabel("Total fabrication time (hours)", labelpad=4)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.legend(loc="upper left", frameon=True, facecolor="white", framealpha=0.95, fontsize=7.3)

plt.tight_layout()
plt.savefig("bottleneck.png", dpi=300)  # the report includes bottleneck.png
plt.savefig("bottleneck-plot.pdf")
