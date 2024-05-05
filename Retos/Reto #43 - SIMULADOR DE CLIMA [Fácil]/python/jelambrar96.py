#!/usr/bin/python3

"""
/*
 * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
 * de un lugar ficticio al pasar un número concreto de días según estas reglas:
 * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
 * - Cada día que pasa:
 *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
 *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día 
 *     siguiente aumenta en un 20%.
 *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día 
 *     siguiente disminuye en un 20%.
 *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
 * - La función recibe el número de días de la predicción y muestra la temperatura
 *   y si llueve durante todos esos días.
 * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
"""

__author__ = "Jorge Lambraño - jelambrar96"
__copyright__ = "Copyright 2024, retos-programacion-2023"
__credits__ = ["Brais Moure - mouredev"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jorge Lambraño"
__email__ = "jelambrar@gmail.com"
__status__ = "Production"



import random


def simulador_clima(dias, temp_inicial, prob_lluvia_inicial):

    temperatura = temp_inicial
    probabilidad_lluvia = prob_lluvia_inicial
    temperatura_max = temp_inicial
    temperatura_min = temp_inicial
    dias_de_lluvia = 0

    bandera_lluvia = random.random() * 100 < probabilidad_lluvia
    str_llueve = "Si" if bandera_lluvia else "No"
    print(f"Día 0: Temp = {temperatura}°C, Prob. Lluvia = {probabilidad_lluvia}%, ¿Llueve? {str_llueve}")

    for dia in range(1, dias + 1):
        
        # Cambio de temperatura
        if random.random() < 0.1:
            cambio = 2 if random.random() < 0.5 else -2
            temperatura += cambio
        
        # Ajustes por temperatura alta o baja
        if temperatura > 25:
            probabilidad_lluvia *= 1.20
        elif temperatura < 5:
            probabilidad_lluvia *= 0.8

        probabilidad_lluvia = min(max(probabilidad_lluvia, 0), 100)  # Mantener en rango [0, 100]

        # Lluvia reduce la temperatura
        bandera_lluvia = random.random() * 100 < probabilidad_lluvia
        if bandera_lluvia:
            temperatura -= 1
            dias_de_lluvia += 1
        
        str_llueve = "Si" if bandera_lluvia else "No"

        # Registro de temperaturas máximas y mínimas
        temperatura_max = max(temperatura_max, temperatura)
        temperatura_min = min(temperatura_min, temperatura)

        print(f"Día {dia}: Temp = {temperatura}°C, Prob. Lluvia = {probabilidad_lluvia}%, ¿Llueve? {str_llueve}")

    print("\nTemperatura máxima: {}°C".format(temperatura_max))
    print("Temperatura mínima: {}°C".format(temperatura_min))
    print("Días de lluvia: {} de {} días".format(dias_de_lluvia, dias))


if __name__ == '__main__':
    
    print("Simulador de clima")
    temperatura = float(input("ingrese la tempratura incial en °C: "))
    probabilidad_lluvia = float(input("ingrese la probabilidad de lluvia (porcentaje de 0 a 100%): "))
    simulador_clima(12, temperatura, probabilidad_lluvia)
