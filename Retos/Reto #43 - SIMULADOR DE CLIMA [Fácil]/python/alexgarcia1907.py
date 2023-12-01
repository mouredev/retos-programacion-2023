# /*
#  * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
#  * de un lugar ficticio al pasar un número concreto de días según estas reglas:
#  * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario. ----
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

def getInitialConditions():
    try:
        initialTemperature = int(input('Introduce la temperatura inicial (ºC): '))
        initialRainChance = int(input('Introduce la probabilidad de lluvia inicial: '))
        days_prediction = int(input("Introduce el número de días de predicción: "))

        return initialTemperature, initialRainChance, days_prediction
    except (ValueError):
        print("Introduce valores correctos.")
        getInitialConditions()

def temperatureChange():
    rand = random.randint(0, 100)

    if rand >= 0 and rand <= 10:
        return True
    return False

def temperatureIncrease2Grades():
    rand = random.choice([0, 1])
    if rand == 0:
        return True
    return False

def printResults(rainyDays, minTemperature, maxTemperature):
    print("\n")
    print("                      RESULTADOS                    ")
    print("----------------------------------------------------")
    print(f"Días de lluvia: {rainyDays}")
    print(f"Temperatura mínima: {minTemperature} ºC")
    print(f"Temperatura máxima: {maxTemperature} ºC")

def calculatePredictions():
    initialTemperature, initialRainChance, days_prediction = getInitialConditions()

    rainyDays = 0
    maxTemperature = initialTemperature
    minTemperature = initialTemperature

    for day in range(1, days_prediction + 1):
        
        # 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
        if temperatureChange():
            if temperatureIncrease2Grades():
                initialTemperature += 2
            else: initialTemperature -= 2


        # Si la temperatura supera los 25 grados, la probabilidad de lluvia al día siguiente aumenta en un 20%.
        if initialTemperature > 25: initialRainChance += 20
        
        # Si la temperatura baja de 5 grados, la probabilidad de lluvia al día siguiente disminuya en un 20%.
        if initialTemperature < 5: initialRainChance -= 20

        # Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
        if initialRainChance >= 100:
            initialTemperature -= 1
            rainyDays += 1

        if initialTemperature < minTemperature: minTemperature = initialTemperature
        if initialTemperature > maxTemperature: maxTemperature = initialTemperature

    
    return printResults(rainyDays, minTemperature, maxTemperature)

if __name__ == '__main__':
    calculatePredictions()
