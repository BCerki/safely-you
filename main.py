from typing import Union
from starlette.responses import Response
from fastapi import FastAPI
from schemas import PerDeviceStats, DeviceStats, Heartbeat
from calculations import calculate_time_duration, calculate_uptime
from create_mock_db import create_mock_db

# Create a mock database on startup
device_data = create_mock_db()

# Set up the API
app = FastAPI(title="Fleet Management Simple Metrics Server",
    description="Simple and correct implementation of the Fleet Management Metrics Coding Assessment",
    version="1.0.0",
    contact={
        "name": "API Support",
        "url": "http://www.example.com/support",
        "email": "support@example.com"
    },
    license_info={
        "name": "None",
        "url": "https://safely-you.com/"
    },
    root_path="/api/v1")


responses = {
    204: {"description": "The request was completed successfully"},
    404: {"description": "Device not found"},
    500: {"description": "Server error"},
}


# GET routes
@app.get("/devices/{device_id}/stats", responses=responses, description="Return device stats")
def return_device_stats(device_id: str):
    uptime = calculate_uptime(device_data[device_id]['heartbeats'])
    avg_upload_time = calculate_time_duration(device_data[device_id]['upload_times'])
    return DeviceStats(uptime=uptime,avg_upload_time=avg_upload_time)


# POST routes
@app.post("/devices/{device_id}/heartbeat", responses=responses, description="Register a heartbeat from a device")
def register_a_heartbeat_from_a_device(device_id: str, heartbeat: Heartbeat):
    device_data[device_id]['heartbeats'].append(heartbeat)
    return Response(status_code=204)

@app.post("/devices/{device_id}/stats", responses=responses)
def add_per_device_statistics(device_id: str, stats: PerDeviceStats):
    device_data[device_id]['upload_times'].append(stats.upload_time)
    return Response(status_code=204)