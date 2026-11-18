Notebook: [Task2_Mathematical_operations.ipynb](Task2_Mathematical_operations.ipynb)

# Learning NumPy: Task 2

This project contains simple practice exercises to learn basic mathematical operations on arrays using the NumPy library inside a Jupyter Notebook.

## Learning Resource Used

I learned these concepts using the **W3Schools NumPy Tutorial**:
* [W3Schools NumPy Introduction](https://w3schools.com)

---

## What This Notebook Does

### Task 2: Mathematical Operations
This notebook performs element-by-element basic math using two matching arrays (`A` and `B`):

1. **Addition**: Uses `np.add(A, B)` to add the items together.
2. **Subtraction**: Uses `np.subtract(A, B)` to find the difference.
3. **Multiplication**: Uses `np.multiply(A, B)` to multiply items position-by-position.
4. **Division**: Uses `np.divide(A, B)` to divide items, resulting in decimal numbers.
5. **Power**: Uses `np.power(A, 2)` to square each number in array A.

## Helpful Things to Remember

* **Element-wise Math**: NumPy automatically pairs up items in the exact same positions to calculate the math.
* **Shape Matching**: For functions like `np.add()`, these examples use matching array shapes for element-wise operations. NumPy also supports compatible shapes through broadcasting.

## How to Run the Notebook

1. Install NumPy in your environment:
   ```bash
   pip install numpy
   ```
2. Open your notebook file (`.ipynb`) in your code editor.
3. Click the **Play** button next to each code cell (or hit **Shift + Enter**) to run the blocks.
