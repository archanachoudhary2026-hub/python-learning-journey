Notebook: [Task2-Mathematical_Operations_on_Series.ipynb](Task2-Mathematical_Operations_on_Series.ipynb)

# Mathematical Operations on Pandas Series (Task 2)

This script demonstrates the power of vectorization in Pandas by performing basic arithmetic operations (addition, subtraction, multiplication, and division) across an entire Series instantly without using loops.

## 📋 Task Overview
1. Add 5 grace marks to all students.
2. Subtract 2 marks from all values.
3. Multiply all marks by 1.05 (a 5% increase).
4. Divide all marks by 2.
5. Print the clear terminal results for each separate operation.

## 🛠️ Code Implementation

```python
import pandas as pd

# Define initial data
marks = [78, 85, 90, 66, 72]
Index = ["Maths", "Science", "Biology", "Humanity", "Hindi"]

# Create the starting Series
series_data = pd.Series(data=marks, index=Index, name="Details")

# 1. Add 5 grace marks to all students
Addition = series_data + 5
print("="*20, "Addition", "="*20)
print("Series after grace marks:")
print(Addition)
print("="*20, "grace_marks", "="*20)
print(" ")

# 2. Subtract 2 marks from all the values
subtraction_series = series_data - 2
print("="*20, "Subraction", "="*20)
print("Series After Subtraction:")
print(subtraction_series)
print("="*20, "Subraction", "="*20)
print(" ")

# 3. Multiply all the values by 1.05
Multiple_Series = series_data * 1.05
print("="*20, "Multiplication", "="*20)
print("Series after Multiplication:")
print(Multiple_Series)
print("="*20, "Multiplication", "="*20)
print(" ")

# 4. Divide all marks by 2
division_series = series_data / 2
print("="*20, "Division", "="*20)
print("Series after division:")
print(division_series)
print("="*20, "Division", "="*20)
print(" ")
```

## 🧠 Key Pandas Concepts Learned

### 1. Vectorized Operations (No Loops!)
In plain Python, if you want to add `5` to every item in a list, you have to write a `for` loop or a list comprehension. 

Pandas uses **vectorization**. When you write `series_data + 5`, Pandas automatically applies the addition to *every single element* in the backend simultaneously. This makes code shorter, cleaner, and incredibly fast.

### 2. New results without changing the original
Notice that when you ran `series_data + 5`, your original `series_data` variable did not change. Instead, Pandas calculated the new math values and returned a brand new Series, which you successfully captured inside separate variables like `Addition` or `subtraction_series`.

A Series itself is mutable; these arithmetic expressions return new values.

### 3. Automatic Data Type Conversion (Upcasting)
* The original marks were integers (whole numbers).
* When multiplying by `1.05` or dividing by `2`, Pandas automatically changed the resulting Series data type to `float64` (decimals) to keep the fractional values precise.

## 🚀 How to Run

1. Run the script in your terminal window:
   Open the linked notebook and run its cells in order.
