import requests
import time
import os
from datetime import datetime

# Your list of cities updated with direct map links and NWS station IDs for current observations
locations = [
    {
        "city": "Marquette, MI", "lat": 46.54, "lon": -87.40, "station": "KMQT",
        "map_link": "https://www.google.com/maps/@46.54,-87.40,11z/data=!5m1!1e1"
    },
    {
        "city": "Gaylord, MI", "lat": 45.03, "lon": -84.68, "station": "KGLR",
        "map_link": "https://www.google.com/maps/@45.03,-84.68,11z/data=!5m1!1e1"
    },
    {
        "city": "Grand Rapids, MI", "lat": 42.96, "lon": -85.67, "station": "KGRR",
        "map_link": "https://www.google.com/maps/@42.96,-85.67,11z/data=!5m1!1e1"
    },
    {
        "city": "Cass City, MI", "lat": 43.60, "lon": -83.17, "station": "KBAX",
        "map_link": "https://www.google.com/maps/@43.60,-83.17,11z/data=!5m1!1e1"
    },
    {
        "city": "Lansing, MI", "lat": 42.73, "lon": -84.55, "station": "KLAN",
        "map_link": "https://www.google.com/maps/@42.73,-84.55,11z/data=!5m1!1e1"
    },
    {
        "city": "Benton Harbor, MI", "lat": 42.12, "lon": -86.45, "station": "KBEH",
        "map_link": "https://www.google.com/maps/@42.12,-86.45,11z/data=!5m1!1e1"
    },
    {
        "city": "Detroit, MI", "lat": 42.33, "lon": -83.05, "station": "KDTW",
        "map_link": "https://www.google.com/maps/@42.33,-83.05,11z/data=!5m1!1e1"
    },
    {
        "city": "Des Moines, IA", "lat": 41.59, "lon": -93.60, "station": "KDSM",
        "map_link": "https://www.google.com/maps/@41.59,-93.60,11z/data=!5m1!1e1"
    },
    {
        "city": "Cedar Rapids, IA", "lat": 41.98, "lon": -91.67, "station": "KCID",
        "map_link": "https://www.google.com/maps/@41.98,-91.67,11z/data=!5m1!1e1"
    }
]

headers = {'User-Agent': '(my-weather-app, contact@example.com)'}

def get_active_alerts(lat, lon):
    """Checks for active NWS alerts at specific coordinates[cite: 1]."""
    try:
        alert_url = f"https://api.weather.gov/alerts/active?point={lat},{lon}"
        resp = requests.get(alert_url, headers=headers).json()
        features = resp.get('features', [])
        
        if not features:
            return "None"
        
        alert_names = list(set([f['properties']['event'] for f in features]))
        return ", ".join(alert_names)
    except Exception as e:
        return f"Alert check failed ({str(e)})"

def get_current_temperature(station_id):
    """Fetches the latest actual thermometer reading from the weather station."""
    try:
        obs_url = f"https://api.weather.gov/stations/{station_id}/observations/latest"
        resp = requests.get(obs_url, headers=headers).json()
        temp_c = resp.get('properties', {}).get('temperature', {}).get('value')
        
        if temp_c is not None:
            # Convert Celsius to Fahrenheit and round it
            temp_f = round((temp_c * 9/5) + 32)
            return f"{temp_f}°F"
    except Exception:
        pass
    return "N/A"

def create_weather_file():
    filename = "Weather_Report.html"
    date_str = datetime.now().strftime("%A, %B %d, %Y")
    
    # HTML Header and basic styling
    report_content = f"""<!DOCTYPE html>
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
        .link-btn {{ display: inline-block; margin-top: 8px; padding: 6px 12px; background-color: #2980b9; color: white; text-decoration: none; border-radius: 4px; font-size: 0.9em; }}
        .link-btn:hover {{ background-color: #1a5276; }}
        .error {{ color: #e74c3c; }}
    </style>
</head>
<body>
<div class="container">
    <h1>Weather & Road Report</h1>
    <p><strong>Date:</strong> {date_str}</p>
    <hr style="border: 0; border-top: 1px solid #ddd; margin-bottom: 20px;">
"""

    print("Fetching weather, current temps, and alerts... please wait[cite: 1].")

    for loc in locations:
        try:
            # 1. Get the forecast text
            point_url = f"https://api.weather.gov/points/{loc['lat']},{loc['lon']}"
            point_resp = requests.get(point_url, headers=headers).json()
            forecast_url = point_resp['properties']['forecast']
            forecast_resp = requests.get(forecast_url, headers=headers).json()
            current_forecast = forecast_resp['properties']['periods'][0]
            
            # 2. Get the actual live current temperature from the station
            live_temp = get_current_temperature(loc['station'])

            # 3. Get active alerts
            active_alerts = get_active_alerts(loc['lat'], loc['lon'])
            
            # Alert styling logic
            alert_class = "alert-text" if active_alerts != "None" else ""

            # 4. Build HTML block for the city
            report_content += f"""
    <div class="city-block">
        <div class="city-name">{loc['city']}</div>
        <div><strong>Alerts:</strong> <span class="{alert_class}">{active_alerts}</span></div>
        <div><strong>Current Temp:</strong> {live_temp}</div>
        <div><strong>Forecast:</strong> {current_forecast['detailedForecast']}</div>
        <div style="margin-top: 10px;"><a href="{loc['map_link']}" target="_blank" style="color: #2980b9; font-weight: bold; text-decoration: underline; font-size: 1.05em;">🗺️ Click here for Live Traffic Map</a></div>
    </div>
"""
            time.sleep(0.7) 
        except Exception as e:
            print(f"Error processing {loc['city']}: {e}")
            report_content += f"""
    <div class="city-block">
        <div class="city-name">{loc['city']}</div>
        <div class="error">Error retrieving data for this location: {str(e)}</div>
    </div>
"""

    report_content += """
</div>
</body>
</html>
"""

    # Write the file securely with UTF-8 encoding
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report_content)
    
    print(f"Success! Report saved locally as '{filename}'.")
    
    try:
        os.startfile(filename)
    except AttributeError:
        print("Auto-open skipped (running in a non-Windows or server environment).")

if __name__ == "__main__":
    try:
        create_weather_file()
    except Exception as e:
        print(f"\nCRITICAL ERROR: The script failed to complete execution.")
        print(f"Error Details: {e}")
