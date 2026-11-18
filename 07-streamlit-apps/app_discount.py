import streamlit as st

st.title("Price Calculator")

product_price = st.number_input("Please enter your price", min_value=0.0, value=0.0, step=1.0)

discount = st.slider("Select the discount:", 0, 50, 0, 10)
st.write(f"The discount is {discount}%")

discounted_price = product_price - (product_price * (discount / 100))

if st.button("Get the Discount price"):
    st.success(
        f"Discount has been applied, Price after the discount: {discounted_price:.2f}",
        icon="😊"
    )

my_table = {
    "Status": ["Original Price", "Price After Discount"],
    "Price": [
        f"{product_price:.2f}",
        f"{discounted_price:.2f}"
    ]
}

st.table(my_table)
