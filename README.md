🚢 Ship Digital Twin
Real-Time Ship Telemetry Dashboard
📌 Overview

Ship Digital Twin is a real-time monitoring system that displays ship engine data on a web dashboard.

Backend (Flask) reads data from a CSV file

Frontend displays live data using charts

Data updates every 2 seconds

📁 Project Structure
ship-digital-twin/
│
├── app.py
├── index.html
├── simulation.py
├── ship_engine_telemetry_5000_rows.csv
└── README.md
⚙️ Tech Stack

Backend: Python, Flask, Pandas

Frontend: HTML, CSS, JavaScript, Chart.js

Data: CSV (5000 rows, 11 columns)

📊 Dataset Columns

timestamp

engine_temp

rpm

engine_load

fuel_rate

speed_knots

oil_pressure

coolant_temp

vibration

weather_status

engine_status

🚀 How It Works

Flask reads data from CSV

API sends one random row

Frontend fetches data every 2 seconds

Dashboard updates automatically

▶️ Run in VS Code
Step 1: Open Folder

Open VS Code

Click File → Open Folder

Select your project folder

Step 2: Open Terminal

In VS Code:

Ctrl + `
Step 3: Install Dependencies
pip install flask flask-cors pandas
Step 4: Run Backend
python app.py
Step 5: Open Browser
http://127.0.0.1:5000

⚠️ Do NOT open index.html directly

🔗 API

GET /ship-data

Returns JSON data like:

{
"engine_temp": 87.3,
"rpm": 1243,
"engine_load": 69,
"fuel_rate": 209.0
}
⚠️ Common Errors
Problem Solution
Module not found Install using pip
Server not running Run app.py
Port busy Change port number
No data Check CSV file
📝 Notes

Updates every 2 seconds

Shows last 20 data points

Status colors:

Green → Normal

Yellow → Warning

Red → Critical

🎯 Conclusion

This project shows how real-time monitoring systems work using Flask and web technologies.
