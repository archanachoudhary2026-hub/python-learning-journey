Notebook: [Task5_Statistical _Operation.ipynb](Task5_Statistical%20_Operation.ipynb)

# Learning NumPy: Task 5

This project contains simple practice exercises to learn **Statistical Operations** (analyzing spreads, averages, and data distribution metrics) on a 1D dataset using the NumPy library inside a Jupyter Notebook.

## Learning Resource Used

I learned these concepts using the **W3Schools NumPy Tutorial**:
* [W3Schools NumPy Introduction](https://w3schools.com)

---

## What This Notebook Does

This notebook uses a 1D array of grades (`marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])`) to calculate key statistical metrics:

1. **Mean**: Uses `np.mean(marks)` to calculate the normal average score.
2. **Median**: Uses `np.median(marks)` to find the exact middle score in the sorted data.
3. **Variance**: Uses `np.var(marks)` to calculate how spread out the scores are from the average.
4. **Standard Deviation**: Uses `np.std(marks)` to measure the typical distance of scores from the mean.
5. **Minimum & Maximum**: Uses `np.min(marks)` and `np.max(marks)` to find the lowest and highest boundaries.
6. **Range**: Subtracts the lowest value from the highest value (`Maximum - Minimum`) to measure the absolute span of the data.

## Helpful Things to Remember

* **`np.round(..., 2)`**: This keeps long decimal values (like variance or standard deviation) short and legible by trimming them down to exactly two decimal places.

## How to Run the Notebook

1. Install NumPy in your environment:
   ```bash
   pip install numpy
   ```
2. Open your notebook file (`.ipynb`) in your code editor.
3. Click the **Play** button next to each code cell (or hit **Shift + Enter**) to run the blocks.
