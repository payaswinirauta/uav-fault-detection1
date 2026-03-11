import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "motor_rpm": 5000,
    "gyro_x": 0.1,
    "gyro_y": 0.2,
    "gyro_z": 0.3,
    "accel_x": 9.7,
    "accel_y": 0.1,
    "accel_z": 0.2
}

response = requests.post(url, json=data)

print(response.json())