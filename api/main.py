# api/main.py
import joblib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import warnings
import os

# Suppress sklearn version mismatch warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

# Initialize FastAPI app
app = FastAPI(
    title="UAV Fault Detection API",
    description="API for predicting UAV motor and sensor faults using a trained ML model",
    version="1.0.0"
)

# Allow cross-origin requests (for frontend integration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static folder for frontend assets
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

# Absolute path to the project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build correct model path
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "uav_fault_model.pkl")
try:
    model = joblib.load(MODEL_PATH)
    print("Model loaded successfully.")
except FileNotFoundError:
    print(f"Model file not found at {MODEL_PATH}. Please check the path.")
except Exception as e:
    print(f"Error loading model: {e}")


    # ------------------------------
# ADD detect_fault FUNCTION HERE
# ------------------------------
def detect_fault(data):
    X_input = [[
        data.motor_rpm,
        data.gyro_x,
        data.gyro_y,
        data.gyro_z,
        data.accel_x,
        data.accel_y,
        data.accel_z
    ]]
    prediction = model.predict(X_input)
    return prediction[0]
# ------------------------------

# Input schema for drone sensor data
class DroneData(BaseModel):
    motor_rpm: float
    gyro_x: float
    gyro_y: float
    gyro_z: float
    accel_x: float
    accel_y: float
    accel_z: float

# Prediction endpoint
@app.post("/predict")
def predict(data: DroneData):
    """
    Accepts drone sensor readings and returns the predicted fault type.
    """
    try:
        X_input = [[
            data.motor_rpm,
            data.gyro_x,
            data.gyro_y,
            data.gyro_z,
            data.accel_x,
            data.accel_y,
            data.accel_z
        ]]
        prediction = model.predict(X_input)
        return {"predicted_fault": prediction[0]}
    except Exception as e:
        return {"error": str(e)}

# Health check endpoint
@app.get("/")
def health_check():
    """
    Simple health check to verify API is running.
    """
    return {"status": "UAV Fault Detection API is running"}
