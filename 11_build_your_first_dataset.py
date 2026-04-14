# Assignment Date: 03/03/2026
# Assignment Name: Build Your First Dataset
# Description: Create a dataset (e.g., study hours vs marks), identify features
# & labels, predict relationship.

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def build_dataset() -> pd.DataFrame:
    rng = np.random.default_rng(seed=1)
    hours = np.linspace(0.5, 10, 20)
    # Marks loosely follow: marks = 8 * hours + noise, capped at 100
    noise = rng.normal(0, 5, size=hours.size)
    marks = np.clip(8 * hours + 10 + noise, 0, 100)
    return pd.DataFrame({"study_hours": hours.round(2), "marks": marks.round(2)})


def main() -> None:
    df = build_dataset()

    print("=== Study Hours vs Marks Dataset ===")
    print(df)

    print("\nFeatures (X): study_hours")
    print("Label    (y): marks")

    corr = df["study_hours"].corr(df["marks"])
    print(f"\nCorrelation between study_hours and marks: {corr:.3f}")

    if corr > 0.7:
        rel = "strongly positive"
    elif corr > 0.3:
        rel = "moderately positive"
    elif corr > -0.3:
        rel = "weak / no"
    else:
        rel = "negative"

    print(f"Predicted relationship: {rel}. More study hours -> higher marks.")

    # Save simple scatter plot
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "11_scatter_plot.png")
    plt.figure(figsize=(6, 4))
    plt.scatter(df["study_hours"], df["marks"], color="seagreen")
    plt.title("Study Hours vs Marks")
    plt.xlabel("Study Hours")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(out)
    plt.close()
    print(f"Scatter plot saved to: {out}")

    # Save the dataset as CSV for later use
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "11_study_vs_marks.csv")
    df.to_csv(csv_path, index=False)
    print(f"Dataset saved to   : {csv_path}")


if __name__ == "__main__":
    main()
