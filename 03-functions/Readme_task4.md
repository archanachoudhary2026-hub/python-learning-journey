Notebook: [Task4-Map_Function.ipynb](Task4-Map_Function.ipynb)

# Task 4: Batch GST Processing Using map()

A clean Python implementation demonstrating how to use the built-in `map()` function to perform batch processing on a list of product prices using a lambda function.

## Overview

This script takes an array of original base prices, applies an 18% Goods and Services Tax (GST) calculation to each element using an anonymous (`lambda`) function, and outputs both collections for comparison.

## Code Implementation

```python
# 1. Define the lambda function for 18% GST
gst = lambda price: price * 1.18

# 2. Given input list of prices
prices = [100, 250, 400, 1200, 50]

# 3. Use map() to apply the lambda to each item and convert the iterator to a list
prices_with_gst = list(map(gst, prices))

# 4. Print both collections
print("Original prices:", prices)
print("Prices after GST:", prices_with_gst)
```

## Output

```text
Original prices: [100, 250, 400, 1200, 50]
Prices after GST: [118.0, 295.0, 472.0, 1416.0, 59.0]
```

## How It Works

* **`lambda price: price * 1.18`**: A compact, anonymous function that takes an individual price and increments it by 18%.
* **`map(gst, prices)`**: Iterates over the `prices` list, passing each element directly into the `gst` function. This avoids the need for explicit `for` loops.
* **`list(...)`**: Casts the lazy `map` generator object back into a standard Python list format so it can be indexed, modified, or cleanly printed.
