# app.py
import streamlit as st
import joblib
import os

st.set_page_config(page_title="UAV Fault Detection", page_icon="🚁")

st.title("UAV Fault Detection 🚁")
st.write("Enter your UAV sensor readings below:")

# Absolute path to the model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "uav_fault_model.pkl")

# Load the model
try:
    model = joblib.load(MODEL_PATH)
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Failed to load model: {e}")
    st.stop()  # stop further execution if model not loaded

# Streamlit inputs for all 7 features
motor_rpm = st.number_input("Motor RPM", value=1200.0, step=10.0)
gyro_x = st.number_input("Gyro X", value=0.0, step=0.01)
gyro_y = st.number_input("Gyro Y", value=0.0, step=0.01)
gyro_z = st.number_input("Gyro Z", value=0.0, step=0.01)
accel_x = st.number_input("Accel X", value=0.0, step=0.01)
accel_y = st.number_input("Accel Y", value=0.0, step=0.01)
accel_z = st.number_input("Accel Z", value=9.8, step=0.01)

# Prediction button
if st.button("Check Fault"):
    try:
        # Prepare input in 2D array format for model
        X_input = [[motor_rpm, gyro_x, gyro_y, gyro_z, accel_x, accel_y, accel_z]]
        prediction = model.predict(X_input)[0]  # get the first prediction
        st.success(f"Prediction: {prediction}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")