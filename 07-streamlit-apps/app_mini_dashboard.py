import streamlit as st

st.title("Simple Sales Dashboard")

selected_month= st.selectbox("Choose the month:",["January", "February", "March", "April"])

sales = {"January": 1200,"February": 1500,"March": 900,"April": 2000}
st.metric(label=f"Sales in {selected_month}", value=f"${sales[selected_month]}")

st.bar_chart({"Month": list(sales), "Sales (USD)": list(sales.values())}, x="Month", y="Sales (USD)", sort=False)
