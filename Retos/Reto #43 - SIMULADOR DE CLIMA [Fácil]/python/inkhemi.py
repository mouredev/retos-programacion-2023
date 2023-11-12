# /*
#  * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
#  * de un lugar ficticio al pasar un número concreto de días según estas reglas:
#  * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
#  * - Cada día que pasa:
#  *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
#  *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día
#  *     siguiente aumenta en un 20%.
#  *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día
#  *     siguiente disminuya en un 20%.
#  *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
#  * - La función recibe el número de días de la predicción y muestra la temperatura
#  *   y si llueve durante todos esos días.
#  * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
#  */

import random


def temperatureChange() -> bool:
    random_number = random.randint(0, 100)
    if random_number >= 0 and random_number <= 10:
        return True
    else:
        return False


def temperatureVariation() -> int:
    random_number = random.randint(0, 100)
    if random_number < 50:
        return 2
    elif random_number >= 50:
        return -2


def weatherSimulator(temperature: int, rainChance: int, days_prediction: int):
    rainy_days = 0
    max_temp = temperature
    min_temp = temperature
    is_raining = "no está lloviendo"

    for day in range(1, days_prediction + 1):
        if temperatureChange():
            temperature += temperatureVariation()

        # Si la temperatura supera el minimo o el máximo, esta los reemplaza
        if temperature < min_temp:
            min_temp = temperature
        elif temperature > max_temp:
            max_temp = temperature

        # Si la probabilidad de lluvia es del 100% se le suma un dia de lluvia y se le quita un grado al dia siguiente
        if rainChance == 100:
            rainy_days += 1
            temperature -= 1
            is_raining = "está lloviendo"
        else:
            is_raining = "no está lloviendo"

        print(f"Dia {day}, {is_raining}, temperatura: {temperature}")

        # Si la temperatura es mayor a 25 aumenta la probabilidad de lluvia en 20% del dia siguiente
        if temperature > 25:
            rainChance += 20
            if rainChance > 100:
                rainChance = 100

        # Si la temperatura es menor a 5 disminuye la probabilidad de lluvia en 20% del dia siguiente
        if temperature < 5:
            rainChance -= 20
            if rainChance < 0:
                rainChance = 0

    print(
        f"temperatura máxima: {max_temp}, temperatura mínima: {min_temp}, dias de lluvia: {rainy_days}")


while True:
    try:
        initial_temperature = int(
            input('Introduce la temperatura inicial (°C): '))
        initial_rainChance = int(
            input('Introduce la probabilidad de lluvia inicial: '))
        days_prediction = int(
            input("Introduce el número de días de predicción: "))
        weatherSimulator(initial_temperature,
                         initial_rainChance, days_prediction)
        break
    except:
        print("Valor invalido")
