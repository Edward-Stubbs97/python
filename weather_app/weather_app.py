import requests
from datetime import datetime

api_key = ""

location = input("Where would you like to check? ").lower()

units = input("What metrics would you like to use, Imperial or Metric? ").lower()

url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units={units}"

weather_Data_Full = requests.get(url)

weather_Object = weather_Data_Full.json()

temp = weather_Object["main"] ["temp"]

description = weather_Object["weather"] [0] ["description"]

sun_Rise = weather_Object["sys"] ["sunrise"]
sun_Set = weather_Object["sys"] ["sunset"]
sun_Rise_Convert = datetime.fromtimestamp(sun_Rise)
sun_Set_Convert = datetime.fromtimestamp(sun_Set)

wind_speed_mps = weather_Object["wind"]["speed"]
wind_speed_mph = wind_speed_mps * 2.23694

timezone_offset = weather_Object["timezone"]
sun_Rise_Convert = datetime.utcfromtimestamp(sun_Rise + timezone_offset)
sun_Set_Convert = datetime.utcfromtimestamp(sun_Set + timezone_offset)
sun_Rise_Str = sun_Rise_Convert.strftime("%I:%M %p")
sun_Set_Str = sun_Set_Convert.strftime("%I:%M %p")

if units == "metric":
    result = "C"
else:
    result = "F"


# fix bug when imperial is chosen the wind speed changes to kmh but displays mph
print(f"The weather in {location.title()} is: {description.capitalize()}, The temperature is {temp}°{result}, the wind speed is {wind_speed_mph:.2f} MPH, sunrise is at {sun_Rise_Str} sunset is at {sun_Set_Str}.")







