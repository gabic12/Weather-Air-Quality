import requests

API_KEY = "YOUR API KEY"
CITY_NAME = "Bucharest"

weather_api_parameters = {
    "key": API_KEY,
    "q": CITY_NAME,
    "aqi": "yes",
    "day_fields": "daily_chance_of_rain",
    "astro": "sunrise,sunset,moon_phase"
}

# API call
weather_response = requests.get(url="http://api.weatherapi.com/v1/forecast.json", params=weather_api_parameters)
weather_response.raise_for_status()
weather_data = weather_response.json()

# Weather variables
date = weather_data["current"]["last_updated"]
temp_c = weather_data["current"]["temp_c"]
condition = weather_data["current"]["condition"]["text"]
wind_kph = weather_data["current"]["wind_kph"]
cloud = weather_data["current"]["cloud"]
chance_of_rain = weather_data["forecast"]["forecastday"][0]["day"]["daily_chance_of_rain"]
uv = float(weather_data["current"]["uv"])
sunrise = weather_data["forecast"]["forecastday"][0]["astro"]["sunrise"]
sunset = weather_data["forecast"]["forecastday"][0]["astro"]["sunset"]
moon_phase = weather_data["forecast"]["forecastday"][0]["astro"]["moon_phase"]

# Air quality variables
co = weather_data["current"]["air_quality"]["co"]
no2 = weather_data["current"]["air_quality"]["no2"]
o3 = weather_data["current"]["air_quality"]["o3"]
so2 = weather_data["current"]["air_quality"]["so2"]
pm2_5 = weather_data["current"]["air_quality"]["pm2_5"]
pm10 = weather_data["current"]["air_quality"]["pm10"]
us_epa_index = int(weather_data["current"]["air_quality"]["us-epa-index"])

uv_risk = ""
aqi = ""

# Calculating UV risk
if uv < 3:
    uv_risk = "Low"
elif (uv >= 3) and (uv < 5):
    uv_risk = "Moderate"
elif (uv >= 5) and (uv < 7):
    uv_risk = "High"
else:
    uv_risk = "Very high"

# Calculating air quality
if us_epa_index == 1:
    aqi = "Good"
elif us_epa_index == 2:
    aqi = "Moderate"
elif us_epa_index == 3:
    aqi = "Unhealthy for sensitive groups"
elif us_epa_index == 4:
    aqi = "Unhealthy"
elif us_epa_index == 5:
    aqi = "Very unhealthy"
else:
    aqi = "Hazardous"

print(f"Sunrise: {sunrise}\nSunset: {sunset}\nMoon phase: {moon_phase}\n")
print(f"{CITY_NAME} at {date} was {condition}:\n- Temperature: {temp_c}°C\n- Wind speed: {wind_kph} km/h\n"
      f"- Cloud coverage: {cloud}%\n- Chance of rain: {chance_of_rain}%\n- UV index: {uv} ({uv_risk} risk of harm!)\n")
print(f"Air quality is {aqi}:\n- Carbon Monoxide: {co} μg/m3\n- Ozone: {o3} μg/m3\n- Nitrogen dioxide: {no2} μg/m3\n"
      f"- Sulphur dioxide: {so2} μg/m3\n- PM2.5: {pm2_5} μg/m3\n- PM10 {pm10} μg/m3")
