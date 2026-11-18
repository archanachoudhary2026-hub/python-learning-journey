import streamlit as st

st.sidebar.title("Product Form")

# Input fields inside the form
product_name = st.sidebar.text_input("Enter the name of the product")
category_name = st.sidebar.selectbox("Please choose from the list:",["Phone","Computer","Stationery","Footwear","Clothing"])
product_price = st.sidebar.number_input("Please enter the price", min_value=0.0, value=0.0, step=1.0)

# Actions happen only when clicked
if st.sidebar.button("Add product") and product_name.strip():
    st.sidebar.success(
        f"{product_name} has been applied in the {category_name} and final price is {product_price}",
        icon="😊"
    )
    st.subheader("Product Details Submitted")
    st.write(f"**Name:** {product_name}")
    st.write(f"**Category:** {category_name}")
    st.write(f"**Price:** Rs{product_price:,.2f}")

if not product_name.strip():
    st.sidebar.caption("Enter a product name before adding a product.")
