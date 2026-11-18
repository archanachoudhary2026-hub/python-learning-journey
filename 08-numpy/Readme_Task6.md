Notebook: [Task6-Percentilies_Sorting.ipynb](Task6-Percentilies_Sorting.ipynb)

# Learning NumPy: Task 6

This project contains simple practice exercises to learn **Sorting, Percentiles, and Conditional Counting** functions using the NumPy library inside a Jupyter Notebook.

## Learning Resource Used

I learned these concepts using the **W3Schools NumPy Tutorial**:
* [W3Schools NumPy Introduction](https://w3schools.com)

---

## What This Notebook Does

This notebook uses a 1D array of grades (`marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])`) to perform three primary operations:

1. **Array Sorting**: Uses `np.sort(marks)` to arrange the unsorted test scores from lowest to highest.
2. **Percentile Computation**: Uses `np.percentile()` to split data distributions into quartiles:
   * **25th Percentile**: The cutoff point where 25% of students scored below.
   * **50th Percentile**: The median value of the test score dataset.
   * **75th Percentile**: The cutoff point where 75% of students scored below.
3. **Conditional Counting**: Computes the class `np.average()`, creates a boolean truth filter (`marks > Average`), and uses `np.sum()` to find out exactly how many elements meet the condition.

## Helpful Things to Remember

* **Boolean Mask Summing**: In Python and NumPy, a `True` value counts as `1` and a `False` value counts as `0`. When you run `np.sum(marks > Average)`, it adds up all the `True` responses to tell you the exact count!
* **`np.average()` vs `np.mean()`**: For a simple dataset like this, both functions yield the exact same result. However, `np.average()` allows for optional weighted averaging if needed later.

## How to Run the Notebook

1. Install NumPy in your environment:
   ```bash
   pip install numpy
   ```
2. Open your notebook file (`.ipynb`) in your code editor.
3. Click the **Play** button next to each code cell (or hit **Shift + Enter**) to run the blocks.
