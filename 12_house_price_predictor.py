# Assignment Date: 09/03/2026
# Assignment Name: House Price Predictor
# Description: Train a Linear Regression model, predict prices, and test with
# new input.
#
# Dataset: California Housing (housing.csv) - 20,640 rows.

import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score


HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "housing.csv")


def main() -> None:
    df = pd.read_csv(CSV_PATH)
    print(f"Loaded housing.csv  shape={df.shape}")

    # Clean: drop rows with any NaN in the columns we care about.
    feature_cols = [
        "housing_median_age", "total_rooms", "total_bedrooms",
        "population", "households", "median_income",
    ]
    target_col = "median_house_value"
    df = df.dropna(subset=feature_cols + [target_col]).reset_index(drop=True)

    print("\n--- Sample rows ---")
    print(df[feature_cols + [target_col]].head())

    X = df[feature_cols]
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    print("\n--- Learned coefficients ---")
    for feature, coef in zip(X.columns, model.coef_):
        print(f"{feature:<22}: {coef:,.2f}")
    print(f"{'intercept':<22}: {model.intercept_:,.2f}")

    print("\n--- Test metrics ---")
    print(f"MAE : ${mean_absolute_error(y_test, preds):,.0f}")
    print(f"R^2 : {r2_score(y_test, preds):.3f}")

    print("\n--- Predicting a new house ---")
    new_house = pd.DataFrame([{
        "housing_median_age": 20,
        "total_rooms": 2000,
        "total_bedrooms": 350,
        "population": 800,
        "households": 300,
        "median_income": 5.0,   # ~$50k (income is in tens-of-thousands)
    }])
    predicted = model.predict(new_house)[0]
    print(f"Input : {new_house.to_dict(orient='records')[0]}")
    print(f"Predicted house value: ${predicted:,.0f}")


if __name__ == "__main__":
    main()
