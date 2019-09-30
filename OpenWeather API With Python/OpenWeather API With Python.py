
import requests, json 
import math
api_key = "YOUR_API"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "YOUR_LOCATION"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()


if x["cod"] != "404":
    y = x["main"]
    current_temperature = math.floor(y["temp"] - 273)
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    print(" Temperature  = " +
          str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n humidity (in percentage) = " +
          str(current_humidiy) +
          "\n description = " +
          str(weather_description))

else:
    print(" City Not Found ")
