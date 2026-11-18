Notebook: [Task4.Polymorphsim.ipynb](Task4.Polymorphsim.ipynb)

# Task 4: Polymorphism in Python

This project demonstrates the core object-oriented programming (OOP) concept of **Polymorphism** using Python subclasses.

## Project Structure

- **`Product` (Base Class):** The parent class containing shared attributes (`name`, `price`, `category`) and a default formatting method.
- **`Laptop` (Subclass):** Inherits from `Product` and adds a unique `color` attribute. Overrides `get_info()` to print details in a laptop-specific format.
- **`Mobile` (Subclass):** Inherits from `Product` and adds a unique `size` attribute. Overrides `get_info()` to print details in a mobile-specific format.

## Implementation Details

### Polymorphism Demonstration
Polymorphism allows different classes to share the same method name (`get_info`) but execute different code behaviors depending on the object type. 

By storing both `Laptop` and `Mobile` objects inside a single unified list (`product_list`), a single `for` loop can iterate through them and dynamically trigger the correct class-specific string outputs without needing explicit type checks.

## How to Run the Code

1. Open your Jupyter Notebook or Python environment.
2. Copy and paste the full script containing the class definitions, object initializations, and the loop into a cell.
3. Run the cell (`Shift + Enter`).

### Expected Output Format
```text
Hello your product MacBook Pro in Space Gray, in category Electronics has a price 1999. 
Hello your product iPhone 15 in 6.1 inch, in category Electronics has a price 999. 
Hello your product Dell XPS in Silver, in category Electronics has a price 1399. 
Hello your product Galaxy S24 in 6.2 inch, in category Electronics has a price 799.
```
