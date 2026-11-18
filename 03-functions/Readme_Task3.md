Notebook: [Task3_Lambda Function.ipynb](Task3_Lambda%20Function.ipynb)

# GST and Discount Calculator

A lightweight Python script demonstrating the use of lambda (anonymous) functions to compute product pricing after applying discounts and Goods and Services Tax (GST).

## Features

- **Basic GST Calculation**: Adds a flat 18% GST to any base price.
- **Discount + GST Calculation**: Applies a percentage discount to the base price first, then calculates the final price inclusive of 18% GST.

## Mathematical Formula

The final price logic follows standard retail sequencing:
1. **Total Price (Post-Discount)** = `Price - (Price * Discount / 100)`
2. **Final Price (Post-GST)** = `Total Price + (Total Price * 0.18)`

## Code Implementation

```python
# 1. Core GST Lambda Function
gst = lambda price: price * 1.18

# 2. Advanced Discount + GST Lambda Function
gst_discount = lambda price, discount: (price - (price * discount / 100)) + ((price - (price * discount / 100)) * 0.18)

# Examples
if __name__ == "__main__":
    print(f"Base price 100 with 18% GST: {gst(100)}") 
    # Output: 118.0

    print(f"Base price 100 with 10% discount and 18% GST: {gst_discount(100, 10)}") 
    # Output: 106.2
```

## How to Run

1. Ensure you have **Python 3.x** installed.
Open the linked notebook rather than creating a separate script.
3. Run the script using your terminal:
   Open the linked notebook and run its cells in order.
