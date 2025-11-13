import pandas as pd

def create_mock_db():
    mock_db = {}
    df = pd.read_csv('devices.csv')
    for device_id in df['device_id']:
        mock_db[device_id] = {"heartbeats": [], "upload_times": []}
    return mock_db
