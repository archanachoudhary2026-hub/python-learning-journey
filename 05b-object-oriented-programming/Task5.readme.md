Notebook: [Task-5 Abstraction.ipynb](Task-5%20Abstraction.ipynb)

# Abstract Payment Processing System

A simple Python application demonstrating Object-Oriented Programming (OOP) concepts, specifically **Abstraction** and **Inheritance**, using Python's built-in `abc` (Abstract Base Classes) module.

## 📌 Project Overview

This project defines an abstract base class `Payment` that acts as a blueprint for different payment gateways. It enforces that any subclass must implement its own version of the `process_payment` method. 

Two payment methods are implemented as subclasses:
1. **Credit Card Payment** (`Creditcardpayment`)
2. **UPI Payment** (`UPIPayment`)

## 🛠️ Concepts Demonstrated

- **Abstraction**: Preventing direct instantiation of the parent `Payment` class and forcing a common interface structure.
- **Inheritance**: Subclasses inheriting initial properties while defining unique behaviors.
- **Polymorphism**: The same method name (`process_payment`) performing different actions depending on the object type.
- **F-Strings**: Dynamically formatting strings in Python.

## 🚀 How to Run the Code

1. Make sure you have **Python 3.x** installed.
Open the linked notebook rather than creating a separate script.
3. Open your terminal or command prompt and run:
   Open the linked notebook and run its cells in order.

## 📋 Sample Output

When you run the testing script, the console will output the simulated payment messages (no actual payment is made):

```text
Thank you! Your Credit card Payment of 5000 is Successful
Sorry Your credit card Payment of 50000 is Unsuccessful
Thank you! Your UPI Payment of 1000 is Successful
Sorry Your UPI Payment of 2500 is Unsuccessful
```
