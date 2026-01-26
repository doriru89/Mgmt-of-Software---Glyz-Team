from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
FIG_DIR = BASE_DIR / "figures"


def save_figure(fig, name):
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / f"{name}.png", dpi=200)
    fig.savefig(FIG_DIR / f"{name}.svg")


def make_income_share_chart():
    df = pd.read_csv(DATA_DIR / "income_shares.csv")
    years = sorted(df["year"].unique())
    groups = ["Bottom 50%", "Middle 40%", "Top 10%"]
    colors = ["#7fc97f", "#beaed4", "#fdc086"]

    fig, ax = plt.subplots(figsize=(7.2, 4.5))
    bottom = np.zeros(len(years))

    for group, color in zip(groups, colors):
        values = [
            df[(df["year"] == year) & (df["group"] == group)]["share_percent"].iloc[0]
            for year in years
        ]
        ax.bar(
            years,
            values,
            bottom=bottom,
            label=group,
            color=color,
            edgecolor="white",
        )
        for i, value in enumerate(values):
            if value >= 8:
                ax.text(
                    years[i],
                    bottom[i] + value / 2,
                    f"{value:.1f}%",
                    ha="center",
                    va="center",
                    fontsize=8,
                )
        bottom += np.array(values)

    ax.set_ylim(0, 100)
    ax.set_ylabel("Share of global income (%)")
    ax.set_title("Global income shares remain highly concentrated")
    ax.legend(ncol=3, frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.12))
    ax.text(
        0.0,
        -0.22,
        "Source: WID.world, stylized for discussion",
        transform=ax.transAxes,
        fontsize=8,
    )
    fig.tight_layout()
    save_figure(fig, "income_share_by_group")


def dollars_k(value, _):
    if value >= 1000:
        return f"${value / 1000:.0f}k"
    return f"${value:.0f}"


def make_income_gain_chart():
    df = pd.read_csv(DATA_DIR / "growth_gains.csv")
    groups = df["group"].tolist()
    values = df["avg_gain_usd_ppp"].to_numpy()
    colors = ["#7fc97f", "#beaed4", "#fdc086"]

    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    bars = ax.bar(groups, values, color=colors, edgecolor="white")

    ax.set_ylabel("Cumulative income gain per adult (2017 USD PPP)")
    ax.set_title("Absolute gains from growth skew to the top")
    ax.yaxis.set_major_formatter(FuncFormatter(dollars_k))
    ax.bar_label(
        bars,
        labels=[f"${value / 1000:.0f}k" for value in values],
        padding=3,
        fontsize=9,
    )
    ax.set_ylim(0, max(values) * 1.2)
    ax.text(
        0.0,
        -0.2,
        "Source: WID.world, stylized for discussion",
        transform=ax.transAxes,
        fontsize=8,
    )
    fig.tight_layout()
    save_figure(fig, "income_gain_by_group")


def main():
    plt.style.use("seaborn-v0_8-whitegrid")
    make_income_share_chart()
    make_income_gain_chart()


if __name__ == "__main__":
    main()
