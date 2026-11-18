# My Python Learning Journey

I'm organising my Python practice by topic, from basic collections and loops to small apps and data analysis. All examples use demo data.

Each folder contains the related exercises and instructions to run them. These are learning projects with basic input checks. The calculators use sample tax rates, and the apps don't save entered data. Please use dummy inputs for the password checker.

## Projects
1. [Data Structures: lists, tuples, sets and dictionaries](01-data-structures/)
2. [Conditions and loops](02-conditions-and-loops/)
3. [Functions](03-functions/)
4. [File handling](04-file-handling/)
5. [Modules and packages](05-modules-and-packages/)
6. [Exception handling](05a-exception-handling/)
7. [Object-oriented programming](05b-object-oriented-programming/)
8. [Mini-projects: number guessing and password checker](06-mini-projects/)
9. [Streamlit apps](07-streamlit-apps/)
10. [NumPy](08-numpy/)
11. [Pandas analysis and Matplotlib graphs](09-pandas-analysis/)
12. [Matplotlib car-sales charts](10-matplotlib-sales/)

## Run the notebooks
Install Python and use VS Code with Python and Jupyter support, or JupyterLab. Install dependencies with `python -m pip install -r requirements.txt`. Open an `.ipynb` file, choose a Python kernel and run cells in order. Menu notebooks wait for input. Enter one price or order at a time and use `q` to quit.

## Run a Streamlit app
From this repository folder, run `python -m streamlit run 07-streamlit-apps/app_discount.py`. Replace the filename with `app_basics.py`, `app_product_form.py` or `app_mini_dashboard.py` for the other apps.
