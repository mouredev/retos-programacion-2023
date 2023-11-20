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

from random import randint, getrandbits


def climate_change(initial_days: int, initial_temperature: float, inititial_risk_of_rain: float):
    days: int = initial_days
    next_temperature: float = initial_temperature
    next_risk_of_rain: float = inititial_risk_of_rain

    min_temperature: float = initial_temperature
    max_temperature: float = initial_temperature

    for day in range(days):
        temperature: float = next_temperature
        risk_of_rain: float = next_risk_of_rain

        print(f"Day {day + 1}, temperature: {temperature}, is raining: {risk_of_rain == 100} ")

        if risk_of_rain == 100:
            next_temperature -= 1

        if temperature < min_temperature:
            min_temperature = temperature

        if temperature > max_temperature:
            max_temperature = temperature

        increase_decrease_temperature_prob: int = randint(1, 100)
        
        if increase_decrease_temperature_prob >= 1 and increase_decrease_temperature_prob <= 10:
            increase_temperature: bool = bool(getrandbits(1))

            if increase_temperature:
                next_temperature += 2
            else:
                next_temperature -= 2

        if next_temperature > 25:
            next_risk_of_rain += 20
        elif next_temperature < 5:
            next_risk_of_rain -= 20

        if next_risk_of_rain < 0:
            next_risk_of_rain = 0
        elif next_risk_of_rain > 100:
            next_risk_of_rain = 100

    print(f"Min temperature: {min_temperature}º, max temperature: {max_temperature}º")


if __name__ == "__main__":
    days: int = int(input("Number of days: "))
    temperature: float = float(input("Initial number of temperature: "))
    risk_of_rain: float = float(input("Initial risk of rain: "))

    climate_change(days, temperature, risk_of_rain)