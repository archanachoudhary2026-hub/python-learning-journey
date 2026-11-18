Notebook: [Task3-Python _Functionalities _On_ series.ipynb](Task3-Python%20_Functionalities%20_On_%20series.ipynb)

# Python Functionalities on Pandas Series (Task 3)

This script demonstrates built-in statistical functions in Pandas and highlights how to use lambda functions alongside conditional filtering to analyze student performance.

## 📋 Task Overview
1. Find the Maximum marks.
2. Find the Minimum marks.
3. Calculate the Sum of all marks.
4. Calculate the Mean (average) marks.
5. Apply a `lambda` function to check if each student passed (Score \(\ge\) 70).
6. Count how many total students passed.

## 🛠️ Code Implementation

```python
import pandas as pd

# Define data
marks = [78, 85, 90, 66, 72]
Index = ["Archana", "Amit", "Preeti", "Sahil", "Shubham"]

# Create the Pandas Series
series_data = pd.Series(data=marks, index=Index, name="Details")

# 1. Maximum Values 
print("="*20, "Maximum Marks", "="*20)
print(f"Maximum Marks: {series_data.max()}")
print("="*55)
print(" ")

# 2. Minimum Values 
print("="*20, "minimum Marks", "="*20)
print(f"minimum Marks: {series_data.min()}")
print("="*55)
print(" ")

# 3. Sum of all marks
print("="*20, "Sum of Marks", "="*22)
print(f"Sum of Marks: {series_data.sum()}")
print("="*55)
print(" ")

# 4. Mean marks
print("="*20, "Mean Marks", "="*23)
print(f"Mean Marks: {series_data.mean()}")
print("="*55)
print(" ")

# 5. Apply a lambda function to check whether each student has passed (>= 70)
passed_students = series_data[series_data.apply(lambda x: x >= 70)]
print("="*20, "Passed Students", "="*19)
print(passed_students)
print("="*55)
print(" ")

# 6. Count of students who passed 
count = passed_students.count()
print("="*10, "Count of passed_students", "="*19)
print(f"Count of passed_students: {count}")
print("="*55)
```

## 🧠 Key Pandas Concepts Learned

### 1. Descriptive Statistics
Pandas provides fast, out-of-the-box mathematical methods for core aggregation metrics:
* `.max()` / `.min()`: Finds boundary limits inside data values.
* `.sum()`: Totals all values in the column.
* `.mean()`: Computes the arithmetic average.

### 2. Lambda Functions & Masking
Your code showcases an advanced technique. By writing `series_data.apply(lambda x: x >= 70)`, Pandas looks at each score and turns it into `True` or `False`. 

When you wrap that check back inside brackets-`series_data[...]`-it acts as a filter mask. It drops any rows marked `False` and preserves only the students who actually passed (`Archana`, `Amit`, `Preeti`, and `Shubham`).

### 3. Aggregating Filters with `.count()`
Once filtered down, the `.count()` method tallies up only the remaining elements, giving you the final count of successful students (4).

## 🚀 How to Run

1. Run the script file:
   Open the linked notebook and run its cells in order.
