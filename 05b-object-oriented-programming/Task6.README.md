Notebook: [Task 6- Magic Methods & Operator Overloading.ipynb](Task%206-%20Magic%20Methods%20&%20Operator%20Overloading.ipynb)

# Task 6: Magic Methods & Operator Overloading

## Task Explanation
The objective of this task is to update a custom `Product` class using Python's special magic methods to control how objects behave:
1. **`__str__` method**: Overrides the default printing behavior to return a clean, human-readable layout displaying the product's name, price, and category.
2. **`__add__` method**: Overloads the mathematical `+` operator so that adding two custom product objects (`product1 + product2`) automatically extracts their prices and returns the plain combined numeric total.

---

## Code Implementation

```python
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __add__(self, other):
        # Calculates and returns the plain total price
        Total = self.price + other.price
        return Total

    def __str__(self):
        # Formats the product information cleanly when printed
        return f"Product({self.name}, Rs {self.price}, {self.category})"


# --- Running and Testing the Code ---

product1 = Product("Laptop", 90000, "Computers")
product2 = Product("Samsung S26 Ultra", 150000, "Phone")

# Testing the __str__ method
print(product1)
print(product2)

# Testing the __add__ method
Total_combined_price = product1 + product2
print(Total_combined_price)
```

---

## Expected Terminal Output

```text
Product(Laptop, Rs 90000, Computers)
Product(Samsung S26 Ultra, Rs 150000, Phone)
240000
```

---

## How to Run

1. Open your code editor or IDLE environment.
Open the linked notebook rather than creating a separate script.
3. Copy and paste the Python code from the implementation section above into your file.
4. Save the file.
5. Click the **Run** button in your editor, or open your terminal and run the file using the command:
   Open the linked notebook and run its cells in order.
