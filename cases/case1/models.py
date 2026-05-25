from dataclasses import dataclass
@dataclass
class VehicleData:
    device_id: str
    timestamp: int
    speed: float