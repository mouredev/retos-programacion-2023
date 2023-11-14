"""
Comentarios:
- El enunciado no exige aplicar mínimos o máximos a temperatura o probabilidad de lluvia.
  Por sentido común, he forzado la probabilidad de lluvia a ester entre (0%, 100%),
  y la temperatura a estar entre dos valores configurables ((-20, +50) por defecto).
- El enunciado parece implicar que sólo llueve cuando la probabilidad es de 100%,
  no que llueva según la probabilidad de lluvia.
- El enunciado no aclara si cuando llueve la probabilidad de lluvia al día
  siguiente se modifica.
- El enunciado no aclara si el 10% de probabilidad de que la temperatura suba o baje
  de un día a otro se reparte igualmente entre subir o bajar. He supuesto que sí,
  con lo cual habría un 5% de subir, un 5% de bajar y un 90% de mantenerse.
- El enunciado no menciona unidades para la temperatura, así que no se han usado.
"""
import random
import sys
from typing import Tuple


MIN_TEMPERATURE = -20
MAX_TEMPERATURE = 50
TEMPERATURE_THRESHOLD_INCREASE_RAIN = 25  # above this temp, rain prob increases next day
TEMPERATURE_THRESHOLD_DECREASE_RAIN = 5  # below this temp, rain prob decreases next day
RAIN_PROBABILITY_DELTA = 20  # percent prob increase/decrease if temp above/below thresholds
TEMPERATURE_DELTA_IF_RAIN = 1  # decrease in next-day temp if it rains today
PROBABILITY_TEMPERATURE_DELTA = 10  # probability that temperature changes wrt previous temp


def validated_input() -> Tuple[int, float, float]:
    """
    Get input simulation days and initial rain probability from the arguments
    passed in the script call.

    Args:
        None.

    Returns:
        Tuple: (simulation days, initial temperature, initial rain probability).
    """
    try:
        days = int(sys.argv[1])
    except (IndexError, ValueError):
        raise ValueError("You must pass a valid amount of days as first argument.")

    if days <= 1:
        raise ValueError(f"Simulation does not make sense for fewer than 2 days (you entered {days})")

    try:
        temperature = float(sys.argv[2])
    except (IndexError, ValueError):
        raise ValueError("You must pass a valid temperature as second argument.")

    if not (MIN_TEMPERATURE <= temperature <= MAX_TEMPERATURE):
        raise ValueError(f"Temperature must be between {MIN_TEMPERATURE} and {MAX_TEMPERATURE}")

    try:
        rain_prob = float(sys.argv[3])
    except (IndexError, ValueError):
        raise ValueError("You must pass a valid rain probability as third argument.")

    if not (0 <= rain_prob <= 100):
        raise ValueError("Rain probability must be between 0 and 100")

    return days, temperature, rain_prob


def new_random_temperature(temperature: float) -> float:
    """
    Given an initial temperature, return today's new temperature.
    The rules are:
    - (100 - PROBABILITY_TEMPERATURE_DELTA) probability of temperature staying the same.
    - PROBABILITY_TEMPERATURE_DELTA probability of temperature going up or down:
        - 50% probability of going up by 2 degrees
        - 50% probability of going down by 2 degrees
    """
    if random.random() <= (1. - PROBABILITY_TEMPERATURE_DELTA/100.):
        return temperature

    if random.random() <= 0.5:
        return temperature + 2

    return temperature - 2


def main(days: int, temperature: float, rain_prob: float) -> None:
    """
    Run the simulation.
    """
    min_temperature, max_temperature, rain_days = None, None, 0
    for day in range(days):
        it_rained = False
        temperature = new_random_temperature(temperature)

        if rain_prob >= 100:
            rain_prob = 100
            it_rained = True
        elif rain_prob <= 0:
            rain_prob = 0

        if min_temperature is None or temperature < min_temperature:
            min_temperature = temperature

        if max_temperature is None or temperature > max_temperature:
            max_temperature = temperature

        print(f"Day {day}: {temperature} degrees, {'it rained' if it_rained else 'it did not rain'}")

        if temperature > TEMPERATURE_THRESHOLD_INCREASE_RAIN:
            rain_prob += RAIN_PROBABILITY_DELTA
        elif temperature < TEMPERATURE_THRESHOLD_DECREASE_RAIN:
            rain_prob -= RAIN_PROBABILITY_DELTA

        if it_rained:
            temperature -= TEMPERATURE_DELTA_IF_RAIN
            rain_days += 1

        if temperature > MAX_TEMPERATURE:
            temperature = MAX_TEMPERATURE
        elif temperature < MIN_TEMPERATURE:
            temperature = MIN_TEMPERATURE

    print(f"\nSummary:\n  Max T: {max_temperature}\n  Min T: {min_temperature}\n  Rain days: {rain_days}")


if __name__ == "__main__":
    simulation_days, initial_temperature, initial_rain_prob = validated_input()
    main(days=simulation_days, temperature=initial_temperature, rain_prob=initial_rain_prob)
