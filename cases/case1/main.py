from parser import parse_message
if __name__ == "__main__":
    mock_data = '{"device_id": "car_01", "timestamp": 1716639563, "speed": 115.5}'
    parsed = parse_message(mock_data)
    print(f"解析成功: {parsed}")