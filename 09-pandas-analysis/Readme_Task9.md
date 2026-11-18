Notebook: [Task9 - Mini _Use _Case - Sales Analysis.ipynb](Task9%20-%20Mini%20_Use%20_Case%20-%20Sales%20Analysis.ipynb)

# Mini Use Case : Sales Analysis (Task 9)

    Create a DataFrame:
    sales = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Revenue': [1200, 1500, 900, 2000, 1800]
    }

## 📋 Task Overview
1. Total revenue
2. Average daily revenue
3. Day with highest revenue
4. Days where revenue > average
5. Plot revenue vs day

## 🛠️ Code Implementation

```python
import pandas as pd
# Create a DataFrame 
sales = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Revenue': [1200, 1500, 900, 2000, 1800]
    }

print("*"*35)
sale_df = pd.DataFrame(sales)
print(sale_df)
print("*"*35)
print(" ")
# total revenue 

Total_Revenue = sale_df["Revenue"].sum()
print("*"*10,"Total Revenue","*"*10)
print(f"Total Revenue : {Total_Revenue}")
print("*"*35)

Average_Revenue = sale_df["Revenue"].mean()
print("*"*10,"Average Revenue","*"*10)
print(f"Average Revenue : {Average_Revenue}")
print("*"*35)


# Day with highest Revenue

highest_revenue_day = sale_df.loc[sale_df["Revenue"] ==sale_df["Revenue"].max(),"Day"]
print("*"*6,"Highest_revenue_day","*"*8)
print(highest_revenue_day)
print("*"*35)

# Days where revenue > average

above_avg_revenue_days = sale_df.loc[sale_df["Revenue"] > sale_df["Revenue"].mean(),"Day"]
print("*"*6,"above_avg_revenue_days","*"*8)
print(above_avg_revenue_days)
print("*"*35)

# Plot revenue vs day
sale_df.plot(x="Day",y="Revenue",kind="bar")
```

## 🧠 What You Learnt Section

### 1. Vectorized Statistical Aggregation
* **`.sum()` and `.mean()`**: These methods compute totals and averages across entire columns without using loops.

### 2. Conditional Selection with `.loc`
* **Label-Based Indexing**: Using `sale_df.loc[condition, "Day"]` filters the rows that match a true/false condition and extracts values from the specified column.

### 3. Categorical Plotting
* **Bar Chart Parameter**: Using `kind="bar"` compares values across categories on the axes.

## 🚀 How to Run

1. Execute the python file:
   Open the linked notebook and run its cells in order.
