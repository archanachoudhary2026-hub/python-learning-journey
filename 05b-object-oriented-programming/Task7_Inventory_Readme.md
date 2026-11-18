Notebook: [Task 7- Mini Project.ipynb](Task%207-%20Mini%20Project.ipynb)

# Store Inventory Management System

## Project Overview

This project is a simple Store Inventory Management System built using Object-Oriented Programming (OOP) concepts in Python.

The system allows users to:

* Create a store
* Add products to inventory
* Remove products from inventory
* Display all products
* Calculate the sum of unit prices
* View a summary of the store

This project uses only classes, objects, methods, lists, and basic Python concepts.

---

## Features

### Inventory Class

The Inventory class manages all products in the store.

#### Methods

* `add_product(name, price, quantity)`

  * Adds a new product to the inventory.

* `remove_product(name)`

  * Removes a product using its name.

* `get_total_value()`

  * Calculates and returns the total value of all product prices.

* `show_all_products()`

  * Displays all products stored in the inventory.

---

### Store Class

The Store class represents a store and contains an Inventory object.

#### Methods

* `add_new_product(name, price, quantity)`

  * Adds a new product to the store inventory.

* `show_summary()`

  * Displays:

    * Store name
    * Total number of products
    * Sum of unit prices

---

## OOP Concepts Used

* Classes
* Objects
* Constructors (`__init__`)
* Encapsulation
* Composition (Store contains an Inventory object)
* Methods
* Lists for data storage

---

## Sample Output

```text

Products in Inventory
-------------------------
Name: Laptop
Price: 50000
Quantity: 5

Name: Mouse
Price: 1000
Quantity: 10

Name: Keyboard
Price: 2000
Quantity: 8


Store Name: ABC Store
Total Products: 3
Total Value: 53000

Combined Price = 51000
```

---

## How to Run

1. Open the Python file in VS Code or Jupyter Notebook.
2. Run the program.
3. Products will be added to the inventory.
4. The inventory details and store summary will be displayed.

---
\
