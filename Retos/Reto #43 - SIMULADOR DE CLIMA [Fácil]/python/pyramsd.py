import random


def weather_simulator(temperature: int, rain: int, days: int):

    rainy_days = 0
    min_temp = temperature
    max_temp = temperature

    for day in range(1, days + 1):

        print(f"Día {day}: {temperature} grados y {rain}% de probabilidad de lluvia")

        if rain == 100:
            rainy_days += 1

        if temperature < min_temp:
            min_temp = temperature

        if temperature > max_temp:
            max_temp = temperature

        if random.randint(1, 10) == 1:
            temperature += 2 if random.randint(1, 2) == 1 else -2

        if temperature > 25:
            rain += 20
            if rain > 100:
                rain = 100

        elif temperature < 5:
            rain -= 20
            if rain < 0:
                rain = 0

        if rain == 100:
            temperature -= 1

    print(f"Días lluviosos: {rainy_days}")
    print(f"Temperatura mínima: {min_temp}")
    print(f"Temperatura máxima: {max_temp}")


weather_simulator(24, 100, 365)