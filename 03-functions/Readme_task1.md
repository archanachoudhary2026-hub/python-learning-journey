Notebook: [Task 1-Basic _Function.ipynb](Task%201-Basic%20_Function.ipynb)

# Price Discount Calculator

A simple Python utility function that calculates the final price of an item after applying a percentage-based discount.

## Features

- **Optional Discount Rates**: Automatically applies a default 5% discount if no rate is provided.
- **Safety Cap**: Ensures discount rates never exceed 60% to protect business margins.
- **Precision Math**: Accurately computes the final price using standard percentage deduction formulas.

## Function Signature

```python
def apply_discount(price, discount_percent=5):
    """
    Calculates the price of an item after applying a discount.
    
    Parameters:
    price (float/int): The original price of the item.
    discount_percent (float/int, optional): The discount percentage to apply. Defaults to 5.
    
    Returns:
    float: The final price after the discount.
    """
```

## Installation & Usage

1. Copy the function into your Python script.
2. Call the function by passing the original price and an optional discount percentage.

### Examples

```python
# Example 1: Applying a specific 10% discount on a 1000 item
print(apply_discount(1000, 10)) 
# Output: 900.0

# Example 2: Using the default 5% discount
print(apply_discount(500)) 
# Output: 475.0

# Example 3: Attempting a 80% discount (Capped at 60%)
print(apply_discount(200, 80)) 
# Output: 80.0
```

## Implementation Details

- **Default Parameters**: Handled natively in the function header (`discount_percent=5`) to prevent missing argument runtime errors.
- **Discount Capping**: Enforced using an internal conditional boundary check before calculation.
