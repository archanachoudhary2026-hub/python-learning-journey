Notebook: [Task1-Basic Class and Objecr creation.ipynb](Task1-Basic%20Class%20and%20Objecr%20creation.ipynb)

# Object-Oriented Programming (OOP) Assignments

This repository contains Python programming assignments focused on mastering foundational Object-Oriented Programming principles.

---

## 🚀 Task 1: Basic Class & Object Creation

### Objective
Create a structured blueprint for a retail environment by implementing a standalone `Product` class with properties, details-printing functionality, and dynamic discount processing.

### Features
*   **Encapsulation**: Manages individual product state attributes cleanly within initialization definitions.
*   **Information Display**: Dynamically builds formatted structural strings outputting specific state realities.
*   **Dynamic Modifiers**: Evaluates direct parameter inputs to correctly deduct variable percentage values from operational baselines.

### Code Implementation

```python
class Product:
    def __init__(self, name, price, category):
        """Initializes a new Product instance with core traits."""
        self.name = name
        self.price = price
        self.category = category
    
    def get_info(self):
        """Prints out clear, cleanly formatted product details."""
        print(f"Hello your product {self.name}, in category {self.category} has a price {self.price}")
        
    def apply_discount(self, discount):
        """Calculates and returns a dynamically adjusted discount valuation."""
        discounted_price = self.price - (self.price * discount / 100)
        return discounted_price
```

### Usage Verification Example

```python
# Instantiating custom entities
iPhone = Product("iPhone", 170000, "Electronics")

# Executing structural description printing
iPhone.get_info()
# Output: Hello your product iPhone, in category Electronics has a price 170000

# Executing discount method calculation
final_price = iPhone.apply_discount(30)
print(f"Final price after discount: {final_price}")
# Output: Final price after discount: 119000.0
```
