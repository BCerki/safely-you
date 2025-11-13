import pytest
from datetime import datetime, timedelta
from schemas import PerDeviceStats, DeviceStats, Heartbeat
from calculations import calculate_time_duration, calculate_uptime

def test_calculate_uptime():
    first_heartbeat_time = datetime(2025, 1, 1, 12, 0)
    heartbeats = [
        Heartbeat(first_heartbeat_time),
        Heartbeat(first_heartbeat_time + timedelta(minutes=2)),  
        Heartbeat(first_heartbeat_time + timedelta(minutes=5)), 
        Heartbeat(first_heartbeat_time + timedelta(minutes=7)),  
    ]
    result = calculate_uptime(heartbeats)
    assert result == 57.14285714285714

   
def test_calculate_time_duration():
    durations = [1_000_000_000, 2_000_000_000, 3_000_000_000]  # 1s, 2s, 3s
    result = calculate_time_duration(durations)
    assert result == "0m2.000000000s"