import matplotlib
matplotlib.use("Agg")  # avoids interactive backend errors

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

# =====================================================
# Paths
# =====================================================
op_path = "operational_results_mean_1.csv"
sd_path = "structural_results_mean_1.csv"

out_path = "delta_heatmap.png"

# =====================================================
# Column mappings: CSV long names -> heatmap labels
# =====================================================
op_map = {
    "OP1(mean(R1, R2, R3))": "OP1",
    "OP2(mean(R1, R2, R3))": "OP2",
    "OP3(mean(R1, R2, R3))": "OP3",
    "OP4(mean(R1, R2, R3))": "OP4",
    "OP5(mean(R1, R2, R3))": "OP5",
}

sd_map = {
    "SD1(mean(R1, R2, R3))": "SD1",
    "SD2(mean(R1, R2, R3))": "SD2",
    "SD3(mean(R1, R2, R3))": "SD3",
    "SD4(mean(R1, R2, R3))": "SD4",
    "SD5(mean(R1, R2, R3))": "SD5",
}

id_order = [
    "all",
    "b1", "b2", "b3",
    "k1", "k2", "k3",
    "neg1", "neg2", "neg3",
    "p1", "p2", "p3",
    "s1", "s2", "s3",
]

# =====================================================
# Load and extract Delta rows
# =====================================================
def extract_delta(csv_path, col_map):
    df = pd.read_csv(csv_path)
    df.columns = [c.strip() for c in df.columns]

    # IDs are only written on the first row of each block:
    # Surface Reader / Baseline / Delta.
    df["ID"] = df["ID"].ffill()

    # Keep Delta rows only
    delta = df[df["Model"].astype(str).str.contains("Delta", case=False, na=False)].copy()

    # Keep and rename metric columns
    keep_cols = ["ID"] + list(col_map.keys())
    delta = delta[keep_cols].rename(columns=col_map)

    # Numeric conversion
    for col in col_map.values():
        delta[col] = pd.to_numeric(delta[col], errors="coerce")

    return delta

op_delta = extract_delta(op_path, op_map)
sd_delta = extract_delta(sd_path, sd_map)

# =====================================================
# Merge OP and SD matrices
# =====================================================
df = pd.merge(op_delta, sd_delta, on="ID", how="outer")

df["ID"] = pd.Categorical(df["ID"], categories=id_order, ordered=True)
df = df.sort_values("ID").reset_index(drop=True)
df["ID"] = df["ID"].astype(str)

metric_cols = ["OP1", "OP2", "OP3", "OP4", "OP5",
               "SD1", "SD2", "SD3", "SD4", "SD5"]

values = df[metric_cols].to_numpy(dtype=float)

# =====================================================
# Plot
# =====================================================
fig, ax = plt.subplots(figsize=(10.5, 7.2))
# fig, ax = plt.subplots(figsize=(12, 7.5))
# fig, ax = plt.subplots(figsize=(9.5, 6.5))

# Diverging scale fixed to [-2, 2], centered on 0
norm = TwoSlopeNorm(vmin=-2, vcenter=0, vmax=2)

# Positive values = red; negative values = blue
cmap = plt.get_cmap("RdBu_r").copy()
cmap.set_bad("#e6e6e6")  # colour for NaN cells, e.g. OP3 for all

masked_values = np.ma.masked_invalid(values)
im = ax.imshow(masked_values, cmap=cmap, norm=norm, aspect="auto")

# Axis ticks
ax.set_xticks(np.arange(len(metric_cols)))
ax.set_xticklabels(metric_cols, fontsize=10)

ax.set_yticks(np.arange(len(df)))
ax.set_yticklabels(df["ID"], fontsize=10)

# Put metrics on top
ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)

# Gridlines
ax.set_xticks(np.arange(-0.5, len(metric_cols), 1), minor=True)
ax.set_yticks(np.arange(-0.5, len(df), 1), minor=True)
ax.grid(which="minor", color="white", linestyle="-", linewidth=1.0)
ax.tick_params(which="minor", bottom=False, left=False)

# Separator between OP and SD blocks
ax.axvline(4.5, color="black", linewidth=1.5)

# Cell annotations
for i in range(values.shape[0]):
    for j in range(values.shape[1]):
        val = values[i, j]

        if np.isnan(val):
            text = "–"
            color = "black"
        else:
            text = f"{val:.2f}"
            color = "white" if abs(val) >= 1.0 else "black"

        ax.text(j, i, text, ha="center", va="center", color=color, fontsize=8)

# Titles and labels
ax.set_ylabel("Prompt ID", fontsize=11)

# Colorbar
cbar = fig.colorbar(im, ax=ax, fraction=0.035, pad=0.025)
cbar.set_label(r"$\Delta$ score", fontsize=10)
cbar.set_ticks([-2, -1, 0, 1, 2])

plt.tight_layout()
plt.savefig(out_path, dpi=300, bbox_inches="tight")
plt.close(fig)

print(f"Saved heatmap to: {out_path}")
print("\nMatrix used for plotting:")
print(df[["ID"] + metric_cols].to_string(index=False))