import requests
import time
import os
from datetime import datetime

# Streamlined list of locations
locations = [
    {"city": "Marquette, MI", "lat": 46.54, "lon": -87.40, "station": "KESC"},
    {"city": "St. Ignace, MI", "lat": 45.86, "lon": -84.74, "station": "KMCD"},
    {"city": "Gaylord, MI", "lat": 45.03, "lon": -84.68, "station": "KGLR"},
    {"city": "Ludington, MI", "lat": 43.98, "lon": -86.47, "station": "KLDM"},
    {"city": "Cass City, MI", "lat": 43.60, "lon": -83.17, "station": "KBAX"},
    {"city": "Grand Rapids, MI", "lat": 42.96, "lon": -85.67, "station": "KGRR"},
    {"city": "Lansing, MI", "lat": 42.73, "lon": -84.55, "station": "KLAN"},
    {"city": "Detroit, MI", "lat": 42.33, "lon": -83.05, "station": "KDTW"},
    {"city": "Jackson, MI", "lat": 42.24, "lon": -84.41, "station": "KJXN"},
    {"city": "Benton Harbor, MI", "lat": 42.12, "lon": -86.45, "station": "KBEH"},
    {"city": "Cedar Rapids, IA", "lat": 41.98, "lon": -91.67, "station": "KCID"},
    {"city": "Des Moines, IA", "lat": 41.59, "lon": -93.60, "station": "KDSM"},
    {"city": "Neola, IA", "lat": 41.45, "lon": -95.61, "station": "KCBF"}
]
HEADERS = {'User-Agent': '(my-weather-app, contact@example.com)'}

def fetch_json(url):
    """Helper function to safely fetch JSON data from APIs."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        if resp.status_code == 200:
            return resp.json()
    except Exception:
        pass
    return None

def get_weather_data(lat, lon, station_id):
    """Fetches alerts, live conditions, and forecast in an optimized way."""
    # 1. Get active alerts
    alerts_data = fetch_json(f"https://api.weather.gov/alerts/active?point={lat},{lon}")
    features = alerts_data.get('features', []) if alerts_data else []
    alerts = ", ".join(set([f['properties']['event'] for f in features])) if features else "None"

    # 2. Get live station temperature and conditions
    obs_data = fetch_json(f"https://api.weather.gov/stations/{station_id}/observations/latest")
    props = obs_data.get('properties', {}) if obs_data else {}
    
    temp_c = props.get('temperature', {}).get('value')
    temp_str = f"{round((temp_c * 9/5) + 32)}°F" if temp_c is not None else "N/A"
    condition = props.get('textDescription', 'Unavailable')

    # 3. Get forecast text via points grid
    point_data = fetch_json(f"https://api.weather.gov/points/{lat},{lon}")
    forecast_text = "Forecast unavailable"
    if point_data:
        forecast_url = point_data.get('properties', {}).get('forecast')
        forecast_data = fetch_json(forecast_url)
        if forecast_data:
            periods = forecast_data.get('properties', {}).get('periods', [])
            if periods:
                forecast_text = periods[0].get('detailedForecast', '')

    return alerts, temp_str, condition, forecast_text

def create_weather_file():
    filename = "Weather_Report.html"
    date_str = datetime.now().strftime("%A, %B %d, %Y")
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Weather & Road Report - {date_str}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 30px; background-color: #f9f9f9; color: #333; }}
        .container {{ max-width: 800px; margin: auto; background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
        h1 {{ color: #2c3e50; border-bottom: 2px solid #eee; padding-bottom: 10px; }}
        .city-block {{ margin-bottom: 25px; padding-bottom: 15px; border-bottom: 1px solid #eee; }}
        .city-name {{ font-size: 1.25em; font-weight: bold; color: #2980b9; margin-bottom: 5px; }}
        .alert-text {{ color: #c0392b; font-weight: bold; }}
        .error {{ color: #e74c3c; }}
    </style>
</head>
<body>
<div class="container">
    <h1>Weather & Road Report</h1>
    <p><strong>Date:</strong> {date_str}</p>
    <hr style="border: 0; border-top: 1px solid #ddd; margin-bottom: 20px;">
"""

    print("Fetching weather reports... please wait.")

    for loc in locations:
        alerts, temp, condition, forecast = get_weather_data(loc['lat'], loc['lon'], loc['station'])
        alert_class = "alert-text" if alerts != "None" else ""
        map_link = f"https://www.google.com/maps/@{loc['lat']},{loc['lon']},11z/data=!5m1!1e1"

        html += f"""
    <div class="city-block">
        <div class="city-name">{loc['city']}</div>
        <div><strong>Alerts:</strong> <span class="{alert_class}">{alerts}</span></div>
        <div><strong>Current Temp:</strong> {temp} ({condition})</div>
        <div><strong>Forecast:</strong> {forecast}</div>
        <div style="margin-top: 10px;"><a href="{map_link}" target="_blank" style="color: #2980b9; font-weight: bold; text-decoration: underline;">🗺️ Click here for Live Traffic Map</a></div>
    </div>
"""
        time.sleep(0.5)

    html += "\n</div>\n</body>\n</html>"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"Success! Report saved locally as '{filename}'.")
    
    try:
        os.startfile(filename)
    except AttributeError:
        pass

if __name__ == "__main__":
    create_weather_file()
