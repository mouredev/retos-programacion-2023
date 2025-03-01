import random

def weather_simulator(temperature: int, rain: int, days: int):
    max_temperature = temperature
    min_temperature = temperature
    rainy_days = 0
    for day in range(1,days+1):
        print(f'dia {day}: temperatura: {temperature} probabilidad de lluvia {rain}%')
        if temperature < min_temperature:
            min_temperature = temperature

        if temperature > max_temperature:
            max_temperature = temperature

        if random.randint(1, 10) == 1:
            temperature += 2 if random.randint(1, 2) == 1 else -2
        if temperature > 25:
            rain += 20
            if rain >= 100:
                rain = 100
        elif temperature < 5:
            rain -= 20
            if rain < 0:
                rain = 0
        if rain == 100:
            temperature -= 1
            rainy_days += 1
    print(f"Días lluviosos: {rainy_days}")
    print(f"Temperatura mínima: {min_temperature}")
    print(f"Temperatura máxima: {max_temperature}")

weather_simulator(24, 100, 365)