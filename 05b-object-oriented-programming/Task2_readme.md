Notebook: [Task 2. constructor&Encapsulation.ipynb](Task%202.%20constructor&Encapsulation.ipynb)

# Product Management System (Encapsulation Practice)

A simple Python implementation demonstrating core Object-Oriented Programming (OOP) concepts, specifically focusing on **Constructors** and **Encapsulation** with data validation.

## 🚀 Features

*   **Data Encapsulation**: Restricts direct access to the product's price attribute using a private variable (`__price`).
*   **Data Validation**: Features a robust setter method that prevents setting invalid or negative prices.
*   **Safe Object Modification**: Clean interfaces via getter and setter methods to access and modify data securely.

## 🛠️ Code Structure

The project implements a `Product` class with the following components:

*   **Constructor (`__init__`)**: Initializes the product name, price, and category.
*   **Getter (`get_price`)**: Safely retrieves or displays the current price of the product.
*   **Setter (`set_price`)**: Evaluates incoming values and updates the price only if `new_price > 0`.

## 💻 Usage Example

```python
# Instantiate a new product
product = Product("Parker Pen", 3500, "Stationery")

# Test invalid price modification (fails validation)
product.set_price(0)
# Output: Error: New price should be greater than Zero

# Test valid price modification (succeeds)
product.set_price(3500)
# Output: The new price after discount and taxes are: 3500
```
