import streamlit as st
from backend import menu, calculate_total

st.title("🍴 Online Food Ordering")

# Customer details
name = st.text_input("Enter Customer Name")

# Food selection
food = st.selectbox("Select Food", list(menu.keys()))

# Quantity
quantity = st.number_input("Enter Quantity", min_value=1, value=1)

# Calculate button
if st.button("Calculate Total"):
    total = calculate_total(food, quantity)

    st.subheader("🧾 Order Summary")
    st.write("Customer Name:", name)
    st.write("Food:", food)
    st.write("Quantity:", quantity)
    st.write("Total Price: ₹", total)

    if st.button("Place Order"):
        st.success("✅ Order placed successfully!")
        