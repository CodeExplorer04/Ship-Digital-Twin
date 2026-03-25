# 🚢 Ship Digital Twin

**Real-Time Ship Engine Telemetry Dashboard**

---

## Overview

Ship Digital Twin is a real-time monitoring system that simulates and visualizes ship engine telemetry. A Flask backend serves randomized rows from a 5,000-row CSV dataset, while a lightweight HTML/JS frontend polls the API every 2 seconds and renders live charts and status cards.

---

## Project Structure

```
ship-digital-twin/
├── app.py
├── index.html
├── simulation.py
├── ship_engine_telemetry_5000_rows.csv
└── README.md
```

---

## Tech Stack

- **Backend:** Python 3, Flask, Pandas
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Charts:** Chart.js (loaded via CDN)
- **Data:** CSV with 5,000 rows, 11 columns

---

## Dataset Columns

| Column         | Unit     | Description                   |
| -------------- | -------- | ----------------------------- |
| timestamp      | ISO 8601 | Date and time of the reading  |
| engine_temp    | °C       | Engine temperature            |
| rpm            | rev/min  | Engine revolutions per minute |
| engine_load    | %        | Engine load percentage        |
| fuel_rate      | L/h      | Fuel consumption rate         |
| speed_knots    | kn       | Vessel speed in knots         |
| oil_pressure   | bar      | Engine oil pressure           |
| coolant_temp   | °C       | Coolant temperature           |
| vibration      | g        | Engine vibration level        |
| weather_status | enum     | Ambient weather condition     |
| engine_status  | enum     | normal / warning / critical   |

---

## API

**GET /ship-data** — Returns one randomly sampled row as JSON.

```json
{
  "engine_temp": 87.3,
  "rpm": 1243,
  "engine_load": 69,
  "fuel_rate": 209.0,
  "speed": 14.2,
  "oil_pressure": 4.12,
  "coolant_temp": 83.5,
  "vibration": 0.07,
  "weather": "clear",
  "status": "normal",
  "timestamp": "2024-01-15T08:42:00"
}
```

---

## Setup & Run

**1. Install dependencies**

```
pip install flask flask-cors pandas
```

**2. Start the server**

```
python app.py
```

**3. Open in browser**

```
http://127.0.0.1:5000
```

> ⚠️ Do NOT open index.html directly — it must be served through Flask.

---

## Troubleshooting

| Problem             | Solution                                   |
| ------------------- | ------------------------------------------ |
| ModuleNotFoundError | Run: pip install flask flask-cors pandas   |
| Cannot reach server | Run: python app.py                         |
| Port 5000 in use    | Change port: app.run(port=5001)            |
| No data displayed   | Ensure CSV is in the same folder as app.py |

---

## Notes

- Data is randomly sampled, so timestamps on the chart may not be chronological.
- `simulation.py` is a standalone CLI tool and does not connect to the dashboard.
- Flask runs in debug mode by default — disable for production.
- Charts show a rolling window of the last 20 data points.
- Status badge colors: 🟢 Normal · 🟡 Warning · 🔴 CriticalHere's the README as plain text:

---

# 🚢 Ship Digital Twin

**Real-Time Ship Engine Telemetry Dashboard**

---

## Overview

Ship Digital Twin is a real-time monitoring system that simulates and visualizes ship engine telemetry. A Flask backend serves randomized rows from a 5,000-row CSV dataset, while a lightweight HTML/JS frontend polls the API every 2 seconds and renders live charts and status cards.

---

## Project Structure

```
ship-digital-twin/
├── app.py
├── index.html
├── simulation.py
├── ship_engine_telemetry_5000_rows.csv
└── README.md
```

---

## Tech Stack

- **Backend:** Python 3, Flask, Pandas
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Charts:** Chart.js (loaded via CDN)
- **Data:** CSV with 5,000 rows, 11 columns

---

## Dataset Columns

| Column         | Unit     | Description                   |
| -------------- | -------- | ----------------------------- |
| timestamp      | ISO 8601 | Date and time of the reading  |
| engine_temp    | °C       | Engine temperature            |
| rpm            | rev/min  | Engine revolutions per minute |
| engine_load    | %        | Engine load percentage        |
| fuel_rate      | L/h      | Fuel consumption rate         |
| speed_knots    | kn       | Vessel speed in knots         |
| oil_pressure   | bar      | Engine oil pressure           |
| coolant_temp   | °C       | Coolant temperature           |
| vibration      | g        | Engine vibration level        |
| weather_status | enum     | Ambient weather condition     |
| engine_status  | enum     | normal / warning / critical   |

---

## API

**GET /ship-data** — Returns one randomly sampled row as JSON.

```json
{
  "engine_temp": 87.3,
  "rpm": 1243,
  "engine_load": 69,
  "fuel_rate": 209.0,
  "speed": 14.2,
  "oil_pressure": 4.12,
  "coolant_temp": 83.5,
  "vibration": 0.07,
  "weather": "clear",
  "status": "normal",
  "timestamp": "2024-01-15T08:42:00"
}
```

---

## Setup & Run

**1. Install dependencies**

```
pip install flask flask-cors pandas
```

**2. Start the server**

```
python app.py
```

**3. Open in browser**

```
http://127.0.0.1:5000
```

> ⚠️ Do NOT open index.html directly — it must be served through Flask.

---

## Troubleshooting

| Problem             | Solution                                   |
| ------------------- | ------------------------------------------ |
| ModuleNotFoundError | Run: pip install flask flask-cors pandas   |
| Cannot reach server | Run: python app.py                         |
| Port 5000 in use    | Change port: app.run(port=5001)            |
| No data displayed   | Ensure CSV is in the same folder as app.py |

---

## Notes

- Data is randomly sampled, so timestamps on the chart may not be chronological.
- `simulation.py` is a standalone CLI tool and does not connect to the dashboard.
- Flask runs in debug mode by default — disable for production.
- Charts show a rolling window of the last 20 data points.
- Status badge colors: 🟢 Normal · 🟡 Warning · 🔴 Critical
