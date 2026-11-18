Notebook: [Task5-Important_DataFrame Functions.ipynb](Task5-Important_DataFrame%20Functions.ipynb)

# Important DataFrame Functions (Task 5)

This script demonstrates core Pandas functions used to audit data health, generate statistical summaries, sort rows by specific criteria, and clean up index flags afterward.

## 📋 Task Overview
1. Use and print outputs for `.info()`, `.describe()`, `.head()`, and `.tail()`.
2. Sort the students by their `Marks` in descending order.
3. Reset the DataFrame index after sorting to maintain a clean sequential order.

## 🛠️ Code Implementation

```python
import pandas as pd

# Define initial data
students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

# Convert into a DataFrame
student_df = pd.DataFrame(students)

# 1. Use and print output of .info()
print("*"*10, "Output of .info()", "*"*13)
student_df.info()  # Note: .info() prints directly to console by default
print("*"*41)
print(" ")

# 2. Use and print output of .describe()
print("*"*10, "Output of .describe()", "*"*8)
print(student_df.describe().round(2))
print("*"*41)
print(" ")

# 3. Use and print output of .head()
print("*"*10, "Output of .head()", "*"*11)
print(student_df.head())
print("*"*41)
print(" ")

# 4. Use and print output of .tail()
print("*"*10, "Output of .tail()", "*"*11)
print(student_df.tail())
print("*"*41)
print(" ")

# 5. Sort Marks in descending order
Sort_data = student_df.sort_values(by="Marks", ascending=False)
print("*"*5, "Marks in descending order", "*"*8)
print(Sort_data)
print("*"*41)
print(" ")

# 6. Reset index after sorting
index_reset = Sort_data.reset_index(drop=True)
print("*"*5, "Reset Index after Sorting", "*"*8)
print(index_reset)
print("*"*41)
```

## 🧠 Key Pandas Concepts Learned

### 1. Data Auditing with `.info()` and `.describe()`
* **`.info()`**: Provides structural metadata. It details the number of entries, column names, memory usage, and counts any missing (`null`) values.
* **`.describe()`**: Instantly generates quick descriptive statistics (mean, min, max, standard deviation, and quartiles) for all numeric columns.

### 2. Sorting Values
By using `.sort_values(by="Marks", ascending=False)`, Pandas shuffles the rows so the highest scorer (`Rahul` with 90) appears at the top, and the lowest scorer (`Sneha` with 66) moves to the bottom.

### 3. Cleaning Indices with `.reset_index()`
When you sort data, the original row numbers (indices) get scrambled along with the rows (e.g., row index sequence becomes `2, 1, 0, 4, 3`). 
* Using `.reset_index(drop=True)` tells Pandas to throw away those jumbled old row numbers and reset them back to a clean, logical sequence starting from `0`.

## 🚀 How to Run

1. Execute the file using python:
   Open the linked notebook and run its cells in order.
