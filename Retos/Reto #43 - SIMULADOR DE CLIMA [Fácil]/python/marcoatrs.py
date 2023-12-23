import random
import signal
import sys

signal.signal(signal.SIGINT, lambda s, f: sys.exit(0))


def start_simulation(temp: float, rain_perc: float, days: int = 1) -> str:
    if (rain_perc > 100) or (rain_perc < 0):
        print("Porcentaje de lluvia invalido")
        return

    max_temp = temp
    min_temp = temp
    rain_days = 0
    summary = ""

    for day in range(days):

        rain = "Yes" if rain_perc == 100 else "No"
        summary += f"[Day {day + 1}] Temp: {temp}° | Rain: {rain}\n"
        max_temp = temp if max_temp < temp else max_temp
        min_temp = temp if min_temp > temp else min_temp
        if rain_perc == 100:
            rain_days += 1

        if temp > 25:
            rain_perc = min(100, rain_perc + 20)
        elif temp < 5:
            rain_perc = max(0, rain_perc - 20)

        if rain_perc == 100:
            temp -= 1

        num = random.random()
        if num <= 0.1:
            temp += 2
        elif 0.2 >= num > 0.1:
            temp -= 2

    summary += f"Max Temp: {max_temp}° | Min Temp: {min_temp}° | Rain {rain_days} days"
    return summary


print(start_simulation(28, 55, 50))
