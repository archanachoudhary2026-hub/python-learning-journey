# Car sales charts with Matplotlib

This notebook uses Pandas to group car-sales data and Matplotlib to create line, scatter, vertical and horizontal bar, grouped bar, stacked bar, histogram and pie charts. Comparisons cover months, years, gender and selected dealer regions.

## Run the notebook
1. Download or clone this repository. Keep all files in this folder together.
2. Install the root `requirements.txt` dependencies.
3. Open this folder in Jupyter or VS Code and run `Sales_Analysis.ipynb` with this folder as the working directory. Run the cells in order.

No separate dataset download is needed. The notebook reads the included `sales_data.csv.gz.b64` file using Python standard-library Base64 and gzip decoding, then loads the CSV with Pandas. This compact text format preserves all 23,906 rows. The pie chart is also saved locally as `dealer_region_distribution.png`.

## Dataset source and licence
The practice data comes from the [Car Sales Report dataset on Kaggle](https://www.kaggle.com/datasets/missionjee/car-sales-report), whose source page lists Apache 2.0. A copy of that licence is in `DATA-LICENSE.txt`; it applies to the included dataset, not to all code in this repository.

Changes to the source CSV: retained only Date, Gender, Annual Income, Price ($) and Dealer_Region, then saved as a gzip-compressed, Base64-encoded CSV. No rows were dropped. Customer names, phone numbers and other unused fields are excluded. This is fictional practice data, not my customer records. The original source CSV is not redistributed here.

## Task explanations

- [TASK_NOTES.md](TASK_NOTES.md)
