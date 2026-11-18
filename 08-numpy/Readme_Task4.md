Notebook: [Task4-Aggregation_Operation.ipynb](Task4-Aggregation_Operation.ipynb)

# Learning NumPy: Task 4

This project contains practice exercises to learn **Aggregation Operations** (calculating sums, minimums, maximums, and averages) on 2D grids using the NumPy library inside a Jupyter Notebook.

## Learning Resource Used

I learned these concepts using the **W3Schools NumPy Tutorial**:
* [W3Schools NumPy Introduction](https://w3schools.com)

---

## What This Notebook Does

This notebook uses a 2x3 2D array matrix to find structural metrics:

1. **Row-wise Sum**: Uses `np.sum(data, axis=1)` to add up the numbers inside each row individually.
2. **Column-wise Sum**: Uses `np.sum(data, axis=0)` to add up the numbers down each column individually.
3. **Minimum Value**: Uses `data.min()` to find the smallest number in the entire grid.
4. **Maximum Value**: Uses `data.max()` to find the largest number in the entire grid.
5. **Overall Mean**: Uses `data.mean()` to calculate the average value of all numbers combined.

### ⭐ Extra Credit Exploration Added!
To better understand how dimensions work, I went beyond the basic assignment to calculate directional limits:
* **Row-wise Min/Max**: Used `axis=1` to find the highest and lowest numbers within each individual row.
* **Column-wise Min/Max**: Used `axis=0` to find the highest and lowest numbers down each individual column.

## Helpful Things to Remember

* **`axis=0`**: Think of this as working **down the columns**.
* **`axis=1`**: Think of this as working **across the rows**.
* **No axis specified**: When you call `.min()`, `.max()`, or `.mean()` without an axis, NumPy flattens the whole grid and looks at all numbers together.

## How to Run the Notebook

1. Install NumPy in your environment:
   ```bash
   pip install numpy
   ```
2. Open your notebook file (`.ipynb`) in your code editor.
3. Click the **Play** button next to each code cell (or hit **Shift + Enter**) to run the blocks.
