Notebook: [Task6-Combined Utility.ipynb](Task6-Combined%20Utility.ipynb)

# Combined Utility Function: Price Processor

A Python utility function that processes a list of prices by applying a uniform discount and filtering the results based on a threshold. This project demonstrates the practical use of functional programming concepts in Python, specifically `map()`, `filter()`, and `lambda` expressions.

## Table of Contents
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation & Requirements](#installation--requirements)
- [Usage & Example](#usage--example)

## Features
* **Bulk Discounting**: Applies a 10% discount to an entire list of prices simultaneously.
* **Conditional Filtering**: Extracts only the high-value items (prices above 300) from the discounted list.
* **Dual Output**: Returns both the fully discounted list and the filtered list for further analysis.

## How It Works
The function `process_prices(prices)` executes the following pipeline:
1. **`map()` + `lambda`**: Iterates through the original `prices` list and multiplies each value by `0.90` to deduct 10%.
2. **`filter()` + `lambda`**: Evaluates the discounted list and retains only elements where the value is strictly greater than `300`.
3. **Data Conversion**: Converts the lazy iterator objects returned by `map` and `filter` into standard Python lists.

## Installation & Requirements
No external dependencies are required. This script runs on standard Python 3.x installations.

Open the linked notebook rather than creating a separate script.
2. Ensure you have Python installed:
   ```bash
   python --version
   ```

## Usage & Example

### Code Implementation
```python
def process_prices(prices):
    """
    Processes a list of prices by applying a 10% discount and 
    filtering for items above 300.
    
    Args:
        prices (list): A list of numerical prices (ints or floats).
        
    Returns:
        tuple: A tuple containing two lists: (discounted_prices, filtered_prices).
    """
    discounted_prices = list(map(lambda price: price * 0.90, prices))
    filtered_prices = list(filter(lambda price: price > 300, discounted_prices))
    
    return discounted_prices, filtered_prices
```

### Execution Example
```python
# Test data
test_prices = [100, 500, 900, 50, 750]

# Run the function
discounted, filtered = process_prices(test_prices)

# Display results
print("Original Prices:  ", test_prices)
print("Discounted (10%): ", discounted)
print("Filtered (> 300): ", filtered)
```

### Output
```text
Original Prices:   [100, 500, 900, 50, 750]
Discounted (10%):  [90.0, 450.0, 810.0, 45.0, 675.0]
Filtered (> 300):  [450.0, 810.0, 675.0]
```
