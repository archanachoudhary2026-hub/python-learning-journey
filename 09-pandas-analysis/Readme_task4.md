Notebook: [Task4-Creating_A _Dataframe.ipynb](Task4-Creating_A%20_Dataframe.ipynb)

# Creating and Inspecting DataFrames (Task 4)

This script demonstrates how to convert a standard Python dictionary into a structured, two-dimensional Pandas DataFrame and inspect its structure, dimensions, and contents.

## 📋 Task Overview
1. Convert a dictionary of student details into a Pandas DataFrame.
2. Print the first 3 rows.
3. Print the last 2 rows.
4. Print the DataFrame's shape (dimensions) and column names.

## 🛠️ Code Implementation

```python
import pandas as pd

# Define initial dictionary data
students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

# 1. Convert it into a DataFrame
student_df = pd.DataFrame(students)

# 2. Print first three rows
first_three_rows = student_df.head(3)
print("="*10, "First three rows", "="*13)
print(first_three_rows)
print("="*41)
print(" ")

# 3. Print last 2 rows
Last_two_rows = student_df.tail(2)
print("="*10, "Last two rows", "="*16)
print(Last_two_rows)
print("="*41)
print(" ")

# 4. Print DataFrame shape and column names
shape_of_dataframe = student_df.shape
Columns_of_dataframe = student_df.columns

print("="*10, "Columns Name", "="*18)
print(Columns_of_dataframe)
print("="*41)
print(" ")

print("="*10, "Shape", "="*24)
print(shape_of_dataframe)
print("="*41)
```

## 🧠 Key Pandas Concepts Learned

### 1. Series vs. DataFrame
While a Pandas Series represents a single column of data (1D), a **DataFrame** represents an entire table (2D) with both rows and columns. Converting a dictionary of lists using `pd.DataFrame()` aligns each list as a column under its respective key.

### 2. Fast Inspections with `.head()` and `.tail()`
* **`.head(n)`**: Fetches the first `n` rows of data from the top. It is standard practice to use this to quickly peek at your data structure.
* **`.tail(n)`**: Fetches the last `n` rows of data from the bottom.

### 3. Understanding DataFrame Metadata Attributes
Notice that these are properties (attributes) of the data, so they do not use parentheses `()` at the end:
* **`.shape`**: Returns a tuple showing `(number_of_rows, number_of_columns)`. For this script, it outputs `(5, 3)`.
* **`.columns`**: Returns an Index object containing all the structural column headers (`Name`, `Marks`, `Subject`).

## 🚀 How to Run

1. Run the script file:
   Open the linked notebook and run its cells in order.
