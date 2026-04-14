# Assignment Date: 24/02/2026
# Assignment Name: Dataset Detective
# Description: Load a dataset, display top rows, find highest value column,
# count missing values, share 5 insights.

import os
import numpy as np
import pandas as pd


HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "iris.csv")


def load_dataset() -> pd.DataFrame:
    df = pd.read_csv(CSV_PATH)
    # Inject ~5% missing values in two columns so the missing-value analysis
    # is meaningful (the raw Iris file has none).
    rng = np.random.default_rng(seed=42)
    for col in ["sepal_length", "petal_width"]:
        mask = rng.random(len(df)) < 0.05
        df.loc[mask, col] = np.nan
    return df


def main() -> None:
    df = load_dataset()

    print(f"Dataset loaded from: {CSV_PATH}")

    print("\n--- Shape ---")
    print(df.shape)

    print("\n--- First 5 rows ---")
    print(df.head())

    print("\n--- Summary statistics ---")
    print(df.describe(include="all"))

    print("\n--- Missing values per column ---")
    print(df.isna().sum())

    numeric = df.select_dtypes(include="number")
    mean_vals = numeric.mean()
    highest_col = mean_vals.idxmax()
    print(f"\n--- Column with the highest average value: '{highest_col}' "
          f"(mean = {mean_vals.max():.2f}) ---")

    print("\n--- 5 Insights ---")
    insights = [
        "The Iris dataset has 3 balanced classes (setosa, versicolor, "
        "virginica) with 50 samples each.",
        f"'{highest_col}' has the largest average value - petals are generally "
        "longer than sepals are wide.",
        "Around 5% of the values in two columns are missing (synthetic) and "
        "need imputation or removal before modelling.",
        "Sepal length and petal length are positively correlated "
        f"(r = {df['sepal_length'].corr(df['petal_length']):.2f}).",
        "Species can be distinguished primarily by petal dimensions rather "
        "than sepal dimensions.",
    ]
    for i, insight in enumerate(insights, start=1):
        print(f"{i}. {insight}")


if __name__ == "__main__":
    main()
