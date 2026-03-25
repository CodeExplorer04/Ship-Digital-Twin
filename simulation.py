import pandas as pd
import time
import random

df = pd.read_csv("ship_engine_telemetry_5000_rows.csv")

def generate_ship_data():
    row = df.sample(1).iloc[0]
    return {
        "engine_temp": round(float(row["engine_temp"]), 1),
        "rpm":          int(row["rpm"]),
        "engine_load":  int(row["engine_load"]),
        "fuel_rate":    round(float(row["fuel_rate"]), 1),
        "speed":        round(float(row["speed_knots"]), 1),
        "oil_pressure": round(float(row["oil_pressure"]), 2),
        "coolant_temp": round(float(row["coolant_temp"]), 1),
        "vibration":    round(float(row["vibration"]), 2),
        "weather":      str(row["weather_status"]),
        "status":       str(row["engine_status"]),
        "timestamp":    str(row["timestamp"])
    }

while True:
    ship = generate_ship_data()
    print(ship)
    time.sleep(2)