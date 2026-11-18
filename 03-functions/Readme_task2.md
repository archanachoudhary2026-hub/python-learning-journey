Notebook: [Task2-Recrusive _1Function.ipynb](Task2-Recrusive%20_1Function.ipynb)

# Factorial Calculator in Python

## Overview

This project calculates the factorial of a number using recursion. It also handles edge cases such as negative numbers, 0, and 1.

## Features

* Validates user input for negative numbers.
* Returns `1` for factorial of `0` and `1`.
* Uses a recursive calculation.
* Uses base cases for 0 and 1; large inputs remain subject to Python recursion depth limits.
* Simple and beginner-friendly Python implementation.

## Code

```python
def factorial(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError("Use a whole number.")
    if n < 0:
        print("Error: Factorial is not defined for negative numbers.")
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Testing factorial(5):", factorial(5))
print("Testing factorial(0):", factorial(0))
print("Testing factorial(-3):", factorial(-3))

```

## How It Works

1. Checks if the number is negative.
2. Returns an error message if the number is less than zero.
3. Returns `1` when the input is `0` or `1`.
4. Returns `n * factorial(n - 1)` after checking the base cases.
5. Returns the final factorial value.

## Example Usage

```python
print(factorial(5))
```

### Output

```text
120
```

## Test Cases

| Input | Output        |
| ----- | ------------- |
| -5    | Error Message |
| 0     | 1             |
| 1     | 1             |
| 5     | 120           |
| 7     | 5040          |

## What I Learned

* Writing and using Python functions
* Handling edge cases
* Using recursion for calculations
* Input validation
* Understanding factorial logic

## Author

Archana Choudhary
 Python Learner
