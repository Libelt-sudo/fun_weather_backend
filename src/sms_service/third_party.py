import os
import requests



def get_weather():

    geo_res = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={"London"}&limit={1}&appid={os.getenv("WEATHER_API_KEY")}")
    geo_json = geo_res.json()

    geo_lon = geo_json[0]["lon"]
    geo_lat = geo_json[0]["lat"]

    weather_res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={geo_lat}&lon={geo_lon}&units={"metric"}&appid={os.getenv("WEATHER_API_KEY")}")
    weather_json = weather_res.json()

    temp = round(weather_json["main"]["temp"])
    feels_like_temp = round(weather_json["main"]["feels_like"])

    return {"temp": temp, "feels_like": feels_like_temp}


def get_joke():
    funny_res = requests.get("https://official-joke-api.appspot.com/jokes/general/random")
    funny_json = funny_res.json()

    funny_joke = f"{funny_json[0]["setup"]} {funny_json[0]["punchline"]}"

    return funny_joke
