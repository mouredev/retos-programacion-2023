# Reto #43: Simulador de clima
#### Dificultad: Fácil | Publicación: 30/10/23 | Corrección: 13/11/23

## Enunciado


#
# Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
# de un lugar ficticio al pasar un número concreto de días según estas reglas:
# - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
# - Cada día que pasa:
#   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
#   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día
#     siguiente aumenta en un 20%.
#   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día
#     siguiente disminuya en un 20%.
#   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
# - La función recibe el número de días de la predicción y muestra la temperatura
#   y si llueve durante todos esos días.
# - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
#

import random

class WeatherSimulator:
    def __init__(self, initial_temperature, prediction_days):
        self.temperature = initial_temperature
        self.prob_rain = 30  # Probabilidad inicial de lluvia (se puede ajustar)
        self.max_temperature = float('-inf')  # Inicializar con un valor negativo
        self.min_temperature = self.temperature
        self.rainy_days = 0
        self.prediction_days = prediction_days

    def simulate_conditions(self):
        for day in range(1, self.prediction_days + 1):
            # Simular cambios en la temperatura
            temperature_change = random.choice([-2, 0, 2])
            
            # Ajustar la probabilidad de lluvia en función de la temperatura actual
            if self.temperature > 25:
                self.prob_rain += 20

            if self.temperature < 5:
                self.prob_rain -= 20

            # Simular lluvia
            is_rain = random.randint(0, 100) < self.prob_rain

            # Actualizar la temperatura
            self.temperature += temperature_change

            # Si llueve (100%), disminuir la temperatura en 1 grado
            if is_rain:
                temperature_change -= 1

            # Si llueve, incrementar el contador de días de lluvia
            if is_rain:
                self.rainy_days += 1

            # Actualizar la temperatura máxima y mínima con estructuras condicionales
            if self.temperature > self.max_temperature:
                self.max_temperature = self.temperature
            if self.temperature < self.min_temperature:
                self.min_temperature = self.temperature

            print(f"Dia {day}: Temperatura: {self.temperature}°C, Lluvia: {'Si' if is_rain else 'No'}")

        print(f"Temperatura máxima: {self.max_temperature}°C")
        print(f"Temperatura mínima: {self.min_temperature}°C")
        print(f"Dias con lluvia: {self.rainy_days}")

if __name__ == "__main__":
    initial_temp = float(input("Temperatura inicial (°C): "))
    prediction_days = int(input("Número de dias de predicción: "))

    simulator = WeatherSimulator(initial_temp, prediction_days)
    simulator.simulate_conditions()





