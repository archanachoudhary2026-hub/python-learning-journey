Notebook: [Task 1- Panda _Series_ Basics.ipynb](Task%201-%20Panda%20_Series_%20Basics.ipynb)

# Pandas Series Basics (Task 1)

## 📋 Task Overview
1. Import the `pandas` library.
2. Create a Pandas Series from a given list of marks.
3. Print the Series values, index, and data type.
4. Access specific elements (the first element and the last two elements).

## 🛠️ Code Implementation

```python
import pandas as pd

# 1. Define the data and custom index labels
marks = [78, 85, 90, 66, 72]
Index = ["Maths", "Science", "Biology", "Humanity", "Hindi"]

# 2. Create the Pandas Series
series_data = pd.Series(data=marks, index=Index, name="Details")

# 3. Print Series Values
print("="*20, "Series Value", "="*20)
print(series_data)
print("="*20, "Series Value", "="*20)
print(" ")

# 4. Print Index
print("="*35, "Index", "="*35)
print(series_data.index)
print("="*35, "Index", "="*35)
print(" ")

# 5. Print Datatype
print("="*20, "DataType", "="*20)
print(series_data.dtype)
print("="*20, "DataType", "="*20)
print(" ")

# 6. Access the first element
print("="*20, "First Element", "="*20)
print(series_data.iloc[0])
print("="*20, "First Element", "="*20)
print(" ")

# 7. Access the last two Elements 
print("="*20, "Last two Element", "="*20)
print(series_data.iloc[-2:])
print("="*20, "Last two Element", "="*20)
print(" ")
```

## 🧠 Key Pandas Concepts Learned

### 1. What is a Pandas Series?
A Series is a one-dimensional array capable of holding any data type. It consists of:
* **Data**: The actual values (e.g., your `marks` list).
* **Index**: The labels corresponding to the values (e.g., your `Index` list of subjects). If no index is provided, Pandas defaults to numbers starting from `0`.

### 2. Attributes Used
* **`.index`**: Returns the label layer of the Series.
* **`.dtype`**: Returns the underlying data type of the values (e.g., `int64` for integers).

### 3. Slicing with `.iloc` (Integer-based Indexing)
* **`series_data.iloc[0]`**: Extracts the very first element at position `0` (`Maths`).
* **`series_data.iloc[-2:]`**: Uses negative indexing to count backward from the end. It grabs everything from the second-to-last item to the very end (`Humanity` and `Hindi`).

## 🚀 How to Run

1. Make sure you have Pandas installed:
   ```bash
   pip install pandas
   ```
Open the linked notebook rather than creating a separate script.
3. Run the script in your terminal:
   Open the linked notebook and run its cells in order.
