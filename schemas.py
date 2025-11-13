from dataclasses import dataclass
import datetime
from pydantic import Field

@dataclass
class DeviceStats:
    uptime: float = Field(...,description="Uptime as a percentage. eg: 98.999")
    avg_upload_time: str = Field(..., description="returned as a time duration string. Eg: 5m10s")

@dataclass
class Heartbeat:
    sent_at: datetime.datetime 

@dataclass
class PerDeviceStats:
    sent_at: datetime.datetime
    upload_time: int = Field(..., description="the number of nanoseconds it took to upload a video")