from flask import Flask, jsonify, render_template, send_from_directory
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__, static_folder='.', template_folder='.')
CORS(app)

# Load CSV once at startup
df = pd.read_csv("ship_engine_telemetry_5000_rows.csv")

@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

@app.route("/ship-data")
def ship_data():
    row = df.sample(1).iloc[0]
    data = {
        "engine_temp":  round(float(row["engine_temp"]), 1),
        "rpm":           int(row["rpm"]),
        "engine_load":   int(row["engine_load"]),
        "fuel_rate":     round(float(row["fuel_rate"]), 1),
        "speed":         round(float(row["speed_knots"]), 1),
        "oil_pressure":  round(float(row["oil_pressure"]), 2),
        "coolant_temp":  round(float(row["coolant_temp"]), 1),
        "vibration":     round(float(row["vibration"]), 2),
        "weather":       str(row["weather_status"]),
        "status":        str(row["engine_status"]),
        "timestamp":     str(row["timestamp"])
    }
    return jsonify(data)

if __name__ == "__main__":
    print("\n✅ Server running! Open this in your browser:")
    print("   http://127.0.0.1:5000\n")
    app.run(debug=True)