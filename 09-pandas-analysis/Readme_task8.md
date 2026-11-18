Notebook: [Task8-Pandas _Plotting_ Simple _Graphs.ipynb](Task8-Pandas%20_Plotting_%20Simple%20_Graphs.ipynb)

# Pandas Plotting Simple Graphs (Task 8)

    # Plot a graph of Student Names vs Marks 

## 📋 Task Overview
1. Plot a graph of Student Names vs Marks.

## 🛠️ Code Implementation

```python
import pandas as pd

students = {
'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
'Marks': [78, 85, 90, 66, 72],
'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

student_df = pd.DataFrame(students)
# Plot a graph of Student Names vs Marks 

(student_df.plot(x="Name",y="Marks",kind="bar"))

# Plot line graph of marks 

(student_df.plot(x="Name",y="Marks",kind="line"))


# Plot histrogram of marks 

(student_df["Marks"].plot(kind="hist"))
```

## 🧠 What You Learnt Section

### 1. The `kind` Parameter
The `.plot()` function acts as a wrapper around the `matplotlib` library. Altering the `kind` keyword string tells the engine which visualization type to use:
* **`kind="bar"`**: Compares distinct categorical data (individual student names vs. scores).
* **`kind="line"`**: Displays trends across data points.
* **`kind="hist"`**: Groups numerical values into intervals to track data distribution.

### 2. Plotting Configurations
* **Two-Column Comparisons**: Using `student_df.plot()` requires defining data mapping with explicit `x="Name"` and `y="Marks"` arguments.
* **Single-Column Frequencies**: Using `student_df["Marks"].plot(kind="hist")` isolates a single column to calculate data intervals automatically.

## 🚀 How to Run

1. Execute the python file:
   Open the linked notebook and run its cells in order.
