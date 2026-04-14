# Assignment Date: 26/02/2026
# Assignment Name: Data Doctor
# Description: Clean a dataset by handling missing values, removing duplicates,
# standardizing text, and explain why cleaning matters.

import os
import pandas as pd


HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "titanic.csv")


def load_messy() -> pd.DataFrame:
    """Titanic already has lots of NaNs; we add a couple of duplicates and
    messy text so the cleaning steps have something to do."""
    df = pd.read_csv(CSV_PATH)
    # Duplicate two random rows to demonstrate de-duplication.
    df = pd.concat([df, df.iloc[[0, 5]]], ignore_index=True)
    # Mess with text casing/whitespace on Sex and Embarked columns.
    df.loc[df.index[:10], "Sex"] = "  MALE "
    df.loc[df.index[10:20], "Sex"] = "female "
    df.loc[df.index[:5], "Embarked"] = " s"
    return df


def clean(df: pd.DataFrame) -> pd.DataFrame:
    # 1. Standardise text (strip + title-case)
    for col in ["Sex", "Embarked"]:
        df[col] = df[col].astype("string").str.strip().str.upper()

    # 2. Handle missing values
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    # 'Cabin' has ~77% missing; the right call is usually to drop the column.
    df = df.drop(columns=["Cabin"])

    # 3. Remove duplicates
    df = df.drop_duplicates(subset=["PassengerId"])

    # 4. Fix types
    df["Age"] = df["Age"].astype(int)

    return df.reset_index(drop=True)


def main() -> None:
    df = load_messy()

    print(f"Loaded Titanic dataset from: {CSV_PATH}")
    print(f"Shape: {df.shape}")

    print("\n--- Raw head ---")
    print(df.head())

    print("\n--- Missing values ---")
    print(df.isna().sum())

    print("\n--- Duplicate rows ---")
    print(df.duplicated(subset=['PassengerId']).sum())

    cleaned = clean(df.copy())

    print("\n--- Cleaned head ---")
    print(cleaned.head())
    print(f"Cleaned shape: {cleaned.shape}")
    print("Missing after cleaning:", cleaned.isna().sum().sum())

    print("\n--- Why cleaning matters ---")
    print(
        "1. Garbage-in-garbage-out: models trained on dirty data give\n"
        "   unreliable predictions.\n"
        "2. Duplicates bias averages and class balance.\n"
        "3. Inconsistent text ('male' vs ' MALE ') is treated as different\n"
        "   categories by most algorithms.\n"
        "4. Missing values can crash training or skew statistics if not\n"
        "   handled (imputed or dropped) properly.\n"
        "5. Columns with too many missing values (Cabin was ~77% NaN) are\n"
        "   better removed than imputed."
    )


if __name__ == "__main__":
    main()
