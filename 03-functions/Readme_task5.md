Notebook: [Task5-FilterFunction.ipynb](Task5-FilterFunction.ipynb)

# Filter Expensive Products Using filter()

## Project Description

This Python program demonstrates how to use the `filter()` function to separate product prices into two categories:

* Prices greater than 500 (Expensive Products)
* Prices less than or equal to 500 (Affordable Products)

The program uses Python's built-in `filter()` function along with `lambda` expressions to create filtered lists.

---

## Problem Statement

Given the following list of product prices:

```python
prices = [100, 250, 400, 1200, 50, 2000, 850]
```

Perform the following tasks:

1. Create a list containing prices greater than 500.
2. Create another list containing prices less than or equal to 500.
3. Print both lists.

---

## Code

```python
prices = [100, 250, 400, 1200, 50, 2000, 850]

# Prices greater than 500
expensive_products = list(filter(lambda price: price > 500, prices))

# Prices less than or equal to 500
affordable_products = list(filter(lambda price: price <= 500, prices))

print("Prices greater than 500:", expensive_products)
print("Prices less than or equal to 500:", affordable_products)
```

---

## Output

```text
Prices greater than 500: [1200, 2000, 850]
Prices less than or equal to 500: [100, 250, 400, 50]
```

---

## Concepts Used

* Python Lists
* `filter()` Function
* Lambda Functions
* Conditional Expressions
* Type Conversion using `list()`

---

## How filter() Works

The `filter()` function applies a condition to each element in a list and keeps only the elements that satisfy the condition.

### Syntax

```python
filter(function, iterable)
```

Where:

* `function` returns `True` or `False`
* `iterable` is the list being filtered

---

## Learning Outcome

After completing this project, you will understand:

* How to filter data from a list
* How to use lambda functions with `filter()`
* How to create new lists based on specific conditions
* The difference between traditional loops and functional programming approaches in Python
