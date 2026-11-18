# Task 1: Basic Streamlit App 

Welcome to my first web application built using Python and Streamlit! This simple program asks for a user's name and displays a personalized greeting when a button is clicked.

---

##  File Name
* `app_basics.py`

---

##  What I Learned

By building this basic application, I learned how to use core Streamlit elements:
* **`st.title()`**: Used to add a large, bold header to the top of the web page.
* **`st.text_input()`**: Used to create an entry box that captures text typed by a user.
* **`st.button()`**: Used to create a clickable button and trigger specific code actions.
* **`st.write()`**: Used to print text dynamically on the screen using Python f-strings.
* **State Management**: Learned how Streamlit captures input data into variables and processes them when a button is clicked.

---

## Requirements

Before running the app, make sure you install the Streamlit library on your computer.

### Installation Command
Open your terminal (Mac/Linux) or Command Prompt (Windows) and run:
```bash
pip install streamlit
```

---

## 🚀 How to Run the App

1. Open your terminal or command prompt inside the folder where `app_basics.py` is saved.
2. Type the following command and press Enter:
   ```bash
   streamlit run app_basics.py
   ```

💡 **Note:** Your web browser will automatically open a new tab showing your live application! To stop the app from running, press `Ctrl + C` in your terminal.


# Task 2: Price Calculator 💰

Welcome to my second web application built using Python and Streamlit! This interactive calculator computes the final discounted price of a product based on user inputs.

---

## 📂 File Name
* `app_discount.py`

---

## 🧠 What I Learned

By building this application, I learned how to use these essential Streamlit elements:
* **`st.number_input()`**: Used to accept numerical values like product prices.
* **`st.slider()`**: Used to create an adjustable slider bar with specified boundaries (0% to 50%) for picking percentages easily.
* **`st.success()`**: Used to display a green, formatted banner to elegantly show the final output.
* **`st.table()`**: Used to present raw structured data (lists of lists) cleanly on screen without needing external libraries.
* **Math Operations**: Learned how to link UI inputs directly to active Python calculations.

---

## 🛠️ Requirements

Make sure you have Streamlit installed on your computer.

### Installation Command
Open your terminal (Mac/Linux) or Command Prompt (Windows) and run:
```bash
pip install streamlit
```

---

## 🚀 How to Run the App

1. Open your terminal or command prompt inside the folder where `app_discount.py` is saved.
2. Type the following command and press Enter:
   ```bash
   streamlit run app_discount.py
   ```

---



# Task 3: Product Form 📦

Welcome to my third web application built using Python and Streamlit! This application creates a structured data entry form inside the sidebar to collect, validate, and display product information.

---

## 📂 File Name
* `app_product_form.py`

---

## 🧠 What I Learned

By building this application, I learned how to move elements into the sidebar layout and format structural responses:
* **`st.sidebar.text_input()`**: Used to collect the text name of a product from a dedicated side layout pane.
* **`st.sidebar.selectbox()`**: Used to provide a dropdown list of preset categories for clean data collection.
* **`st.sidebar.number_input()`**: Used to securely accept price integers/floats without risking alphabetical formatting errors.
* **`st.sidebar.button()`**: Used to handle form execution triggers within the sidebar interface.
* **UI Formatting**: Learned how to pair markdown outputs on the main page to show captured data dynamically upon interaction.

---

## 🛠️ Requirements

Before running the app, make sure you install the Streamlit library on your computer.

### Installation Command
Open your terminal (Mac/Linux) or Command Prompt (Windows) and run:
```bash
pip install streamlit
```

---

## 🚀 How to Run the App

1. Open your terminal or command prompt inside the folder where `app_product_form.py` is saved.
2. Type the following command and press Enter:
   ```bash
   streamlit run app_product_form.py
   ```

---

## 📊 Application Testing & Execution

This sidebar application has been completely built and verified locally. The submission action correctly captures user inputs, isolates actions to the sidebar button click, and prints clean product specifications onto the main view layout.


# Task 4: Simple Sales Dashboard 📊

This is a simple data dashboard built using Python and Streamlit. It lets users select a month from a dropdown menu to see that month's sales and shows a bar chart of the full data.

---

## 📂 File Name
* `app_mini_dashboard.py`

---

## 📋 What the App Does

This project meets the following requirements:
1. **Title**: Shows a main header named "Simple Sales Dashboard".
2. **Month Picker**: Has a dropdown selection box with January, February, March, and April.
3. **Sales Data**: Uses a Python dictionary to store monthly sales values.
4. **Display**: Shows the chosen month's sales numbers using text or metrics.
5. **Chart**: Displays a visual bar chart of all sales values.

---

## 🧠 What I Learned

By building this app, I learned how to:
* Create dropdown menus using `st.selectbox()`.
* Pull specific values out of a Python dictionary based on user selection.
* Generate automatic charts on a web page using `st.bar_chart()`.

---

## 🛠️ How to Setup and Run

### Step 1: Install Streamlit
Open your command prompt or terminal and run this command:
```bash
pip install streamlit
```

### Step 2: Run the Application
Navigate to your project folder and run:
```bash
streamlit run app_mini_dashboard.py
```
