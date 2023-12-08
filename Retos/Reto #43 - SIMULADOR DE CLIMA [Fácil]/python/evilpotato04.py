# Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
# de un lugar ficticio al pasar un número concreto de días según estas reglas:
# - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
# - Cada día que pasa:
#   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
#   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día 
#     siguiente aumenta en un 20%.
#   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día 
#     siguiente disminuye en un 20%.
#   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
# - La función recibe el número de días de la predicción y muestra la temperatura
#   y si llueve durante todos esos días.
# - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.

import random

def weather_forecast(total_days, temperature, probability_of_rain):
    next_day = 0
    days_of_rain = 0
    max_temperature = temperature
    min_temperature = temperature

    print(" day | temperature (C°) | probability of rain (%)")
    print("--------------------------------------------------")
    while next_day < total_days:
        next_day += 1
        raining_today = " (raining day)" if probability_of_rain == 100 else ""
        days_of_rain = days_of_rain + 1 if probability_of_rain == 100 else days_of_rain
        max_temperature = temperature if max_temperature < temperature else max_temperature
        min_temperature = temperature if min_temperature > temperature else min_temperature

        print("  " 
            + str(next_day) + "  |        " 
            + str(temperature) + "        |        " 
            + str(probability_of_rain) + raining_today)
        
        if random.randint(1, 100) < 10:
            temperature = temperature - 2 if random.randint(1,2) == 1 else temperature + 2
        
        if temperature < 5:
            probability_of_rain -= 20
        if temperature > 25:
            probability_of_rain += 20

        if probability_of_rain < 0:
            probability_of_rain = 0
        if probability_of_rain > 100:
            probability_of_rain = 100
        if probability_of_rain == 100:
            temperature -= 1

    print("--------------------------------------------------")
    print("Total days of rain: " + str(days_of_rain))
    print("Maximum temperature: " + str(max_temperature))
    print("Minimum temperature: " + str(min_temperature)) 
    print("--------------------------------------------------")

total_days = int(input("Insert the number of days to weather forecast: "))
current_temperature = int(input("Insert the current temperature: "))
current_probability_of_rain = int(input("Insert the current probability of rain: "))

weather_forecast(total_days, current_temperature, current_probability_of_rain)