# Price Range Analysis — Cognifyz Data Analyst Internship (Task 2)

Analysis of the Zomato restaurant dataset to find patterns between a
restaurant's **price range** and its **rating**.

**Live dashboard:** deploy with Vercel and drop the link here.

## Task

- Determine the most common price range among all restaurants.
- Calculate the average rating for each price range.
- Identify the color that represents the highest average rating among
  different price ranges.

## Findings

| Price Range | Restaurants | % of total | Avg. Rating |
|:-----------:|:-----------:|:----------:|:-----------:|
| 1 ($)       | 4,444       | 46.5%      | 2.00        |
| 2 ($$)      | 3,113       | 32.6%      | 2.94        |
| 3 ($$$)     | 1,408       | 14.7%      | 3.68        |
| 4 ($$$$)    | 586         | 6.1%       | 3.82        |

- **Most common price range:** 1 (budget-friendly), with 4,444 restaurants.
- **Average rating rises with price range** — pricier restaurants are
  rated meaningfully higher on average.
- **Highest average rating:** Price range 4, at **3.82**, which falls
  in the **Yellow** rating-color band (3.5–3.9).

Rating color reference used in the dataset:

| Color      | Rating band |
|------------|:-----------:|
| White      | 0.0         |
| Red        | 1.8 – 2.4   |
| Orange     | 2.5 – 3.4   |
| Yellow     | 3.5 – 3.9   |
| Green      | 4.0 – 4.4   |
| Dark Green | 4.5 – 4.9   |

## Files

- `index.html` — dark-themed, interactive dashboard (Chart.js) showing the
  distribution, ratings, and result. This is the file Vercel serves.
- `price_range_analysis.py` — standalone Python script that recomputes
  everything above from `data.csv` using pandas.
- `data.csv` — Zomato restaurant dataset used for the analysis (add this
  yourself when uploading, see below).
- `vercel.json` — minimal static-site config.

## Run the analysis locally

```bash
pip install pandas
python price_range_analysis.py data.csv
```

## Deploy

### GitHub (mobile, via github.dev)

1. Create a new repo, e.g. `cognifyz-price-range-analysis`.
2. Upload `index.html`, `README.md`, `vercel.json`, and
   `price_range_analysis.py` individually (drag-and-drop or "Add file →
   Upload files").
3. Optionally add `data.csv` if you want the raw dataset in the repo.

### Vercel

1. Go to vercel.com → **New Project** → import the GitHub repo.
2. Framework preset: **Other** (static site) — no build command needed.
3. Deploy. `index.html` will be served at the root URL.

## Author

Jayesh Bapurao Kadam — F.Y. B.Tech AI & Data Science, KBPCOES (DBATU)
