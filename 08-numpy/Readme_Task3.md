Notebook: [Task3_Important_Mathematical_formula.ipynb](Task3_Important_Mathematical_formula.ipynb)

# Learning NumPy: Task 3

This project contains simple practice exercises to learn mathematical formulas and aggregation functions using the NumPy library inside a Jupyter Notebook.

## Learning Resource Used

I learned these concepts using the **W3Schools NumPy Tutorial**:
* [W3Schools NumPy Introduction](https://w3schools.com)

---

## What This Notebook Does

### Task 3: Important Mathematical Formulas
This notebook applies math functions across a single array of values `[2, 4, 6, 8, 10]`:

1. **Square Root**: Uses `np.sqrt(values)` to calculate the square root of each number, cleaned up to 2 decimal places using `np.round()`.
2. **Exponential**: Uses `np.exp(values)` to find the natural exponential ($e^x$) of each number.
3. **Natural Logarithm**: Uses `np.log(values)` to find the natural log (base $e$) of each number.
4. **Sum**: Uses `np.sum(values)` to add all elements together into a single total.
5. **Cumulative Sum**: Uses `np.cumsum(values)` to create a running total array that adds up numbers step-by-step.

## Helpful Things to Remember

* **`np.round(..., 2)`**: This keeps long decimal results clean by rounding them to exactly two decimal places.
* **`np.cumsum()`**: Notice how the name is shortened in NumPy! Writing out the full word `np.cumulative_sum()` will cause a code error.

## How to Run the Notebook

1. Install NumPy in your environment:
   ```bash
   pip install numpy
   ```
2. Open your notebook file (`.ipynb`) in your code editor.
3. Click the **Play** button next to each code cell (or hit **Shift + Enter**) to run the blocks.
