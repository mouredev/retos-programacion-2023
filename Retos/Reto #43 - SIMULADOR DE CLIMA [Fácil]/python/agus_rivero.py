"""
 * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
 * de un lugar ficticio al pasar un número concreto de días según estas reglas:
 * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
 * - Cada día que pasa:
 *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
 *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día 
 *     siguiente aumenta en un 20%.
 *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día 
 *     siguiente disminuya en un 20%.
 *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
 * - La función recibe el número de días de la predicción y muestra la temperatura
 *   y si llueve durante todos esos días.
 * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
"""
import random


class ClimateConditionsSimulator:
    def __init__(self, initial_temp: int, initial_rain_prob: float):
        self.temp = initial_temp
        self.rain_prob = initial_rain_prob
        self.rainy_days = []
        self.max_temp = initial_temp
        self.min_temp = initial_temp

    def get_climate_conditions_on_day_n(self, day_n: int) -> dict:
        for day in range(day_n):
            next_day_temp = self.get_augmented_temp()
            next_day_rain_prob = self.rain_prob

            if self.temp > 25:
                next_day_rain_prob += 0.2
            elif self.temp < 5:
                next_day_rain_prob -= 0.2
            if self.rain_prob == 1:
                self.rainy_days.append(day)
                next_day_temp -= 1
            if next_day_temp > self.max_temp:
                self.max_temp = next_day_temp
            elif next_day_temp < self.min_temp:
                self.min_temp = next_day_temp

            self.temp = next_day_temp
            self.rain_prob = next_day_rain_prob

    def get_augmented_temp(self):
        prob = random.randint(0, 100)
        augment_or_reduce = random.randint(0, 1)
        if augment_or_reduce == 0 and prob <= 10:
            return self.temp + 2
        elif augment_or_reduce == 1 and prob <= 10:
            return self.temp - 2
        else:
            return self.temp

    def get_results(self):
        return {
            "max_temperature": self.max_temp,
            "min_temperature": self.min_temp,
            "rainy_days": self.rainy_days,
            "rainy_days_count": len(self.rainy_days),
            "day_n_temp": self.temp,
        }


if __name__ == "__main__":
    simulator = ClimateConditionsSimulator(40, 1)
    simulator.get_climate_conditions_on_day_n(10000)
    print(simulator.get_results())
