import json
from models import VehicleData
def parse_message(raw_str: str) -> VehicleData:
    data = json.loads(raw_str)
    return VehicleData(
        device_id=data["device_id"],
        timestamp=data["timestamp"],
        speed=float(data["speed"])
    )