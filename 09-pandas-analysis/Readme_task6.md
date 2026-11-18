Notebook: [Task6-Filtering _and_grouping.ipynb](Task6-Filtering%20_and_grouping.ipynb)

# Filtering & Conditional Selection (Task 6)

This script demonstrates how to slice and filter data inside a Pandas DataFrame using dynamic boolean conditions to locate specific subsets of data.

## 📋 Task Overview
1. Filter students who scored more than 75 marks.
2. Filter students belonging to the "Math" subject.
3. Filter students who scored more than the calculated average marks.
4. Filter students who failed (scored less than 70 marks).

## 🛠️ Code Implementation

```python
import pandas as pd

# Define initial data
students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

# Convert to DataFrame
student_df = pd.DataFrame(students)

# 1. Students who scored more than 75 Marks 
top_performer = student_df[student_df["Marks"] > 75]
print("*"*10, "Top Performers", "*"*14)
print(top_performer)
print("*"*40)
print(" ")

# 2. Students belonging to Subject Math
MathStudent = student_df[student_df["Subject"] == "Math"]
print("*"*10, "List of Math Student", "*"*8)
print(MathStudent)
print("*"*40)
print(" ")

# 3. Students who scored more than average 
Average_marks = student_df["Marks"].mean()
above_average_performer = student_df[student_df["Marks"] > Average_marks]
count_of_Student = len(above_average_performer)

print("*"*5, "Student who scored above Avg", "*"*5)
print(f"Average Marks :{Average_marks}")
print(f"Count of student who scored above avaerage: {count_of_Student}")
print(above_average_performer)
print("*"*40)
print(" ")

# 4. Students who failed (marks < 70)
Bottom_performer = student_df[student_df["Marks"] < 70]
count_of_bottom_performer = len(Bottom_performer)

print("*"*5, "Student who scored below 70", "*"*5)
print(f"Count of Bottom performer: {count_of_bottom_performer}")
print(Bottom_performer)
print("*"*40)
```

## 🧠 Key Pandas Concepts Learned

### 1. Boolean Masking
When you pass a conditional statement inside brackets like `student_df[student_df["Subject"] == "Math"]`, Pandas temporarily evaluates every row to see if it is `True` or `False`. It then uses that boolean map to shield out `False` values and return only matching records.

### 2. Dynamic Metric Calculations
Instead of hardcoding a static number to check against the average, your script dynamically calls `student_df["Marks"].mean()`. This ensures that even if student scores change in the future, the script updates and calculates the correct cutoff value automatically.

### 3. Tallying Rows with `len()`
Using Python's built-in `len(dataframe)` is an efficient, beginner-friendly way to quickly count the number of rows currently matching your filtered subset.

## 🚀 How to Run

1. Execute the python file:
   Open the linked notebook and run its cells in order.
