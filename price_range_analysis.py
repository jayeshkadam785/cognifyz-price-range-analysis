"""
Cognifyz Technologies - Data Analyst Internship
Task 2: Price Range Analysis

- Determine the most common price range among all restaurants.
- Calculate the average rating for each price range.
- Identify the color that represents the highest average rating among
  different price ranges.

Usage:
    python price_range_analysis.py data.csv
"""

import sys
import pandas as pd


def analyze(csv_path: str) -> None:
    df = pd.read_csv(csv_path, encoding="utf-8-sig")

    # 1. Most common price range
    price_counts = df["Price range"].value_counts().sort_index()
    most_common_price_range = df["Price range"].mode()[0]

    # 2. Average rating per price range
    avg_rating_by_price = df.groupby("Price range")["Aggregate rating"].mean().round(2)

    # 3. Rating color associated with the highest average rating
    highest_price_range = avg_rating_by_price.idxmax()
    highest_avg_rating = avg_rating_by_price.max()
    color_for_highest = (
        df[df["Price range"] == highest_price_range]["Rating color"]
        .value_counts()
        .idxmax()
    )

    print("=" * 50)
    print("PRICE RANGE DISTRIBUTION")
    print("=" * 50)
    print(price_counts.to_string())
    print(f"\nMost common price range: {most_common_price_range} "
          f"({price_counts.max()} restaurants)")

    print("\n" + "=" * 50)
    print("AVERAGE RATING PER PRICE RANGE")
    print("=" * 50)
    print(avg_rating_by_price.to_string())

    print("\n" + "=" * 50)
    print("RESULT")
    print("=" * 50)
    print(f"Highest average rating: {highest_avg_rating} "
          f"(Price range {highest_price_range})")
    print(f"Color representing the highest average rating: {color_for_highest}")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "data.csv"
    analyze(path)
