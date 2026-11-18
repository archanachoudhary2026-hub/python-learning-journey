# Car sales charts with Matplotlib

This notebook uses Pandas to group car-sales data and Matplotlib to create line, scatter, vertical and horizontal bar, grouped bar, stacked bar, histogram and pie charts. Comparisons cover months, years, gender and selected dealer regions.

## Dataset and setup
The CSV is downloaded separately; it is not included in this repository.

1. Download `Car Sales.xlsx - car_data.csv` from the [Car Sales Report dataset on Kaggle](https://www.kaggle.com/datasets/missionjee/car-sales-report). A Kaggle sign-in may be required. The matching source page lists Apache 2.0 as its dataset licence. Follow the source terms when using the downloaded file.
2. Place the CSV beside `Sales_Analysis.ipynb`, keeping that exact filename.
3. Install the root `requirements.txt` dependencies, then open this folder in Jupyter or VS Code. Run the notebook with this folder as the working directory.

The notebook loads only the five columns used in the analysis: Date, Gender, Annual Income, Price ($) and Dealer_Region. Customer names, phone numbers and other unused columns are not loaded. The charts use an external practice dataset, not my own customer records.

Run the cells in order. The pie chart is also saved locally as `dealer_region_distribution.png`.
