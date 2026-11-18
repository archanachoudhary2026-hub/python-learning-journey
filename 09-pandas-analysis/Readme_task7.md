Notebook: [Task7-Grouping _basics_Analysis.ipynb](Task7-Grouping%20_basics_Analysis.ipynb)

# Grouping & Basic Analysis (Task 7)

This script demonstrates how to split data into separate groups based on a categorical column (like subjects) and calculate aggregate statistical metrics for each group.

## 📋 Task Overview
1. Find the average marks per subject using `groupby()`.
2. Count the total number of students enrolled per subject.
3. Find the maximum (highest) marks scored per subject.

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

# 1. Find average marks per subject using groupby()
avg_marks_by_subject = student_df.groupby("Subject")["Marks"].mean().round(2)
print("*"*10, "Average Marks per Subject", "*"*10)
print(avg_marks_by_subject)
print("*"*48)
print(" ")

# 2. Count number of students per subject
student_count_by_subject = student_df.groupby("Subject")["Name"].count()
print("*"*10, "Student_count_by_subject", "*"*10)
print(student_count_by_subject)
print("*"*48)
print(" ")

# 3. Maximum marks per subject
max_marks_by_subject = student_df.groupby("Subject")["Marks"].max()
print("*"*10, "max_marks_by_subject ", "*"*10)
print(max_marks_by_subject)
print("*"*48)
```

## 🧠 Key Pandas Concepts Learned

### 1. The Split-Apply-Combine Pattern
The `.groupby()` method works in three invisible backend stages:
* **Split**: It breaks your DataFrame into smaller sub-tables based on unique values in your grouping column (e.g., creating a "Math" bucket and a "Science" bucket).
* **Apply**: It target-selects a specific column (like `["Marks"]` or `["Name"]`) and applies an mathematical operation (`.mean()`, `.count()`, or `.max()`).
* **Combine**: It stitches those individual results back together into a clean, easy-to-read Pandas Series output.

### 2. Descriptive Variable Naming
Your variable choices (`avg_marks_by_subject`, `student_count_by_subject`, and `max_marks_by_subject`) follow industry best practices. They clearly convey exactly what metric is being calculated and how the data is grouped.

### 3. Polish Output formatting with `.round()`
Just like in `Task 5`, attaching `.round(2)` onto your mean scores keeps long floating-point decimals from cluttering up your user terminal.

## 🚀 How to Run

1. Run the python script file:
   Open the linked notebook and run its cells in order.
