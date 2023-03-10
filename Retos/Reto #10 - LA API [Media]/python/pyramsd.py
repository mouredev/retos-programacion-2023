import requests
from datetime import datetime

# he creado un api key para este reto de OpenWeather
user_api = "3d182119ac77b2a38debc1aa430ea0e3"
location = input("Introduzca nombre de la ciudad: ")

complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}"

api_link = requests.get(complete_api_link)
api_data = api_link.json()


if api_data["cod"] == "404":
    print("Invalid city: {}, please  check your city name.".format(location))
else:
    # Variables para mostrar los datos de la api
    temp_city = ((api_data["main"]["temp"]) - 273.15)
    weather_desc = api_data["weather"][0]["description"]
    hmdt = api_data["main"]["humidity"]
    wind_spd = api_data["wind"]["speed"]
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("---------------------------------------------------------------")
    print("Estadísticas para - {} || {}".format(location.upper(), date_time))
    print("---------------------------------------------------------------")

    print("Temperatura actual      : {:.2f} °C".format(temp_city))
    print("Descripción del tiempo  :", weather_desc)
    print("Humedad actual          :", hmdt, "%")
    print("Velocidad del viento    :", wind_spd, "kmph")
