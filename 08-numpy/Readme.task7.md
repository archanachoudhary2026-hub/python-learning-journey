Notebook: [Task7-Mini_project.ipynb](Task7-Mini_project.ipynb)

# Learning NumPy: Task 7 (Sales Analysis Mini Use Case)

This project contains a simple practice exercise applying multiple foundational NumPy functions to a real-world **Sales Analysis** scenario inside a Jupyter Notebook.

## Learning Resource Used

I learned these concepts using the **W3Schools NumPy Tutorial**:
* [W3Schools NumPy Introduction](https://w3schools.com)

---

## What This Notebook Does

This notebook analyzes a 1D array representing a full week of daily sales data `[1200, 1500, 900, 2000, 1800, 1700, 1600]`:

1. **Total Weekly Sales**: Uses `np.sum(sales)` to add up the revenue generated over the entire week.
2. **Average Daily Sales**: Uses `np.average(sales)` to calculate the daily performance benchmark.
3. **Highest & Lowest Sales Amounts**: Uses `np.max(sales)` and `np.min(sales)` to find the largest and smallest sales amounts; the code does not report day names or indices.
4. **Standard Deviation**: Uses `np.std(sales)` to see how much the daily sales numbers fluctuate from the weekly average.
5. **Above Average Counting**: Uses a conditional check `np.sum(sales > Average_Weekly_Sales)` to count exactly how many days beat the weekly average score.

## Helpful Things to Remember

* **`np.max()` and `np.min()`**: Using NumPy's built-in mathematical tools is preferred over Python's default variations because they are fully optimized for data arrays.
* **Variable References**: Always double-check your print statement targets. Accidentally typing an old variable name instead of your current output target will cause a code crash.

## How to Run the Notebook

1. Install NumPy in your environment:
   ```bash
   pip install numpy
   ```
2. Open your notebook file (`.ipynb`) in your code editor.
3. Click the **Play** button next to each code cell (or hit **Shift + Enter**) to run the blocks.
