import streamlit as st

st.title("UAV Fault Detection 🚁")
st.write("Step 1: Basic interface test")

param1 = st.number_input("Parameter 1")
param2 = st.number_input("Parameter 2")
param3 = st.number_input("Parameter 3")

if st.button("Check Fault"):
    st.success(f"You entered: {param1}, {param2}, {param3}")