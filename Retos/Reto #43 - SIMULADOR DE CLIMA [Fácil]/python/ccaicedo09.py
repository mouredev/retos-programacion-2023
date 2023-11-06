""" * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
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
 * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover."""

import random
import os

class SimuladorClima():

    def __init__(self, temperatura, probabilidad_lluvia, dias_prediccion):
        self.temperatura = temperatura
        self.probabilidad_lluvia = probabilidad_lluvia
        self.dias_de_lluvia = 0
        self.temperatura_min = temperatura
        self.temperatura_max = temperatura
        self.dias_prediccion = dias_prediccion
    
    def simulador(self):
        for dia in range(1, self.dias_prediccion + 1):
            
            # Considerar: 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
            cambio_temperatura = 0
            lluvia = False

            if 10 > random.randint(1, 100):
                if random.randint(0,1) == 0:
                    cambio_temperatura -= 2
                else:
                    cambio_temperatura += 2
            
            #Simular lluvia de acuerdo a la probabilidad dada---------------------

            #La probabilidad de lluvia tiene que estar en términos de porcentaje
            if self.probabilidad_lluvia>100:
                self.probabilidad_lluvia = 100
            elif self.probabilidad_lluvia < 0:
                self.probabilidad_lluvia = 0
            
            if self.probabilidad_lluvia >= random.randint(1,100):
                lluvia = True
                cambio_temperatura -= 1 # -> Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
                self.dias_de_lluvia += 1

            #Validar probabilidad de lluvia al día siguiente

            if self.temperatura > 25: #Si la temperatura supera los 25 grados, la probabilidad de lluvia al día siguiente aumenta en un 20%.
                self.probabilidad_lluvia += 20
            
            if self.temperatura < 5: #Si la temperatura baja de 5 grados, la probabilidad de lluvia al día siguiente disminuye en un 20%.
                self.probabilidad_lluvia -= 20 
            
            #Determinar cambios en temperatura mínima y máxima

            if self.temperatura < self.temperatura_min:
                self.temperatura_min = self.temperatura
            
            if self.temperatura > self.temperatura_max:
                self.temperatura_max = self.temperatura

            print(f"Día: {dia} | Temperatura: {self.temperatura}°C | Lloverá: {'Sí' if lluvia else 'No'}")

            #Aplicar el cambio de temperatura a la temperatura del día siguiente

            self.temperatura += cambio_temperatura

        print(f"\nTemperatura mínima: {self.temperatura_min}°C\n"
            f"Temperatura máxima: {self.temperatura_max}°C\n"
            f"Días de lluvia: {self.dias_de_lluvia}")


if __name__ == "__main__":
    os.system("cls")
    temperatura = float(input("Ingrese la temperatura inicial (°C): "))
    probabilidad_lluvia = int(input("Ingrese la probabilidad de lluvia inicial (%): "))
    dias_prediccion = int(input("Ingrese los días para la predicción: "))
    print("")

    simulador = SimuladorClima(temperatura, probabilidad_lluvia, dias_prediccion)
    simulador.simulador()
