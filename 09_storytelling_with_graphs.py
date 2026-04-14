# Assignment Date: 28/02/2026
# Assignment Name: Storytelling with Graphs
# Description: Create bar chart, pie chart, histogram and write a short data
# story explaining trends.

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # save to file without needing a display
import matplotlib.pyplot as plt


def build_sales_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "product": ["Phones", "Laptops", "Tablets", "Headphones", "Watches"],
            "units_sold": [1200, 800, 400, 1500, 600],
        }
    )


def build_marks_data(seed: int = 7) -> np.ndarray:
    rng = np.random.default_rng(seed)
    # simulate 200 students' marks with mean 70, std 12
    marks = rng.normal(loc=70, scale=12, size=200).clip(0, 100)
    return marks


def main() -> None:
    out_dir = os.path.dirname(os.path.abspath(__file__))
    sales = build_sales_data()
    marks = build_marks_data()

    # Bar chart - units sold per product
    plt.figure(figsize=(7, 4))
    plt.bar(sales["product"], sales["units_sold"], color="steelblue")
    plt.title("Units Sold per Product")
    plt.ylabel("Units Sold")
    plt.xlabel("Product")
    bar_path = os.path.join(out_dir, "09_bar_chart.png")
    plt.tight_layout()
    plt.savefig(bar_path)
    plt.close()

    # Pie chart - market share
    plt.figure(figsize=(5, 5))
    plt.pie(
        sales["units_sold"],
        labels=sales["product"],
        autopct="%1.1f%%",
        startangle=90,
    )
    plt.title("Market Share by Product")
    pie_path = os.path.join(out_dir, "09_pie_chart.png")
    plt.tight_layout()
    plt.savefig(pie_path)
    plt.close()

    # Histogram - marks distribution
    plt.figure(figsize=(7, 4))
    plt.hist(marks, bins=15, color="orange", edgecolor="black")
    plt.title("Distribution of Student Marks")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    hist_path = os.path.join(out_dir, "09_histogram.png")
    plt.tight_layout()
    plt.savefig(hist_path)
    plt.close()

    print("Saved plots:")
    print(" -", bar_path)
    print(" -", pie_path)
    print(" -", hist_path)

    print("\n--- Data Story ---")
    print(
        "Headphones are the best-selling category (1,500 units), followed\n"
        "closely by phones. Tablets lag behind with only 400 units. The pie\n"
        "chart shows headphones and phones together make up over half of our\n"
        "sales, suggesting we should keep stock of these in focus. The\n"
        "histogram of student marks is roughly bell-shaped around 70, with a\n"
        "handful of outliers at both ends - typical of a class where most\n"
        "students perform around the average."
    )


if __name__ == "__main__":
    main()
