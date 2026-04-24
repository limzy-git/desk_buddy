import requests, json

AREA = "Clementi"

def get_air_temp():    
    r = requests.get("https://api-open.data.gov.sg/v2/real-time/api/air-temperature")
    data = r.json()
    
    stations = data["data"]["stations"]
    readings = data["data"]["readings"][0]["data"]

    station_id = ""
    value = ""

    for station in stations:
        if AREA in station["name"]:
            station_id = station["id"]
            break

    for no in readings:
        if no["stationId"] == station_id:
            value = no["value"]
    return value

def get_forecast_2h():    
    r = requests.get("https://api-open.data.gov.sg/v2/real-time/api/two-hr-forecast")
    data = r.json()

    nowcasts = data["data"]["items"][0]["forecasts"]

    nowcast_value = ""

    for nowcast in nowcasts:
        area = nowcast["area"]
        forecast = nowcast["forecast"]

        if area == AREA:
            nowcast_value = forecast
    return nowcast_value

def get_3d_forecasts():
    r = requests.get("https://api-open.data.gov.sg/v2/real-time/api/four-day-outlook")
    data = r.json()
    days_data = data["data"]["records"][0]["forecasts"]
    three_day_forecasts = []

    for day in days_data[:3]:
        output = {}
        output["date"] = day["timestamp"][:10]
        output["day"] = day["day"]
        output["forecast"] = day["forecast"]["summary"]
        output["temperature"] = {
            "min" : day["temperature"]["low"], 
            "max" : day["temperature"]["high"]
        }
        output["Humidity"] = {
            "min" : day["relativeHumidity"]["low"], 
            "max" : day["relativeHumidity"]["high"]
        }
        output["Wind"] = {
            "min" : day["wind"]["speed"]["low"], 
            "max" : day["wind"]["speed"]["high"] 
        }

        three_day_forecasts.append(output)
    return three_day_forecasts

def get_relative_humidity():
    r = requests.get("https://api-open.data.gov.sg/v2/real-time/api/relative-humidity")
    data = r.json()

    stations = data["data"]["stations"]
    readings = data["data"]["readings"][0]["data"]

    station_id = ""
    humidity = ""

    for station in stations:
        if AREA in station["name"]:
            station_id = station["id"]
            break

    for reading in readings:
        if reading["stationId"] == station_id:
            humidity = reading["value"]
    return humidity

def get_wind_speed():
    r = requests.get("https://api-open.data.gov.sg/v2/real-time/api/wind-speed")
    data = r.json()

    stations = data["data"]["stations"]
    readings = data["data"]["readings"][0]["data"]

    station_id = ""
    wind_speed = ""

    for station in stations:
        if AREA in station["name"]:
            station_id = station["id"]
            break

    for reading in readings:
        if reading["stationId"] == station_id:
            wind_speed = reading["value"]
    return wind_speed

def is_rain_warning(condition):
    keywords = ["shower", "thunder", "drizzle", "rain"]
    condition_lower = condition.lower()
    
    for word in keywords:
        if word in condition_lower:
            return True
        
    return False

def get_weather():
    temperature = get_air_temp()
    condition = get_forecast_2h()
    forecast = get_3d_forecasts()
    humidity = get_relative_humidity()
    wind_speed = get_wind_speed()
    rain_warning = is_rain_warning(condition)
    return {
        "temperature" : temperature,
        "condition" : condition,
        "humidity" : humidity,
        "wind_speed" : wind_speed,
        "rain_warning" : rain_warning,
        "forecast" : forecast
    }
