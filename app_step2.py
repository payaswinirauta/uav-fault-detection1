import streamlit as st
import pickle

st.title("UAV Fault Detection 🚁")
st.write("Step 2: Model load test")

# Try to load your ML model
try:
    with open('models/uav_fault_model.pkl', 'rb') as f:
        model = pickle.load(f)
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Model load failed: {e}")