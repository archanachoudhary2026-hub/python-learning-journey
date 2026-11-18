Notebook: [Task-7-Mini_problem.ipynb](Task-7-Mini_problem.ipynb)

# Task 7: Menu-Driven Price Tracker

A lightweight, terminal-based Python application that tracks prices using functional programming principles. It allows users to dynamically add prices, calculate averages, and find the maximum price through an interactive loop interface.

## 🚀 Features

*   **Interactive Menu**: Simple, user-friendly text interface.
*   **Price Tracking**: Dynamically append float or integer values to a central list.
*   **Statistical Breakdown**: Instant calculations for average and highest prices.
*   **Error Handling**: Built-in safeguards against invalid inputs (e.g., entering letters instead of numbers).

## 🛠️ Requirements

*   Python 3.x or higher
*   No external dependencies or libraries required.

## 📂 Core Structure

The application strictly uses loops and function calls, adhering to a functional workflow with zero Object-Oriented Programming (OOP):

1.  `add_price(prices_list, price)`: Updates the core data array.
2.  `get_average_price(prices_list)`: Computes the arithmetic mean.
3.  `get_max_price(prices_list)`: Identifies the highest value.

## 💻 How to Run

Open the linked notebook rather than creating a separate script.
2. Open your terminal or command prompt.
3. Execute the script using:
   Open the linked notebook and run its cells in order.

## 📝 Example Usage

```text
--- Menu ---
1 → Add price
2 → Show average price
3 → Show highest price
q → Quit
Enter your choice: I choose 1,1 and then  ,2 then 3, and then q
Enter the price to add: 2000 3000
Price 2000,3000 added successfully.
average price = 2500
highest price =3000
```
