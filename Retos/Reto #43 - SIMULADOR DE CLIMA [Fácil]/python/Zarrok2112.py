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

## Initial conditions
def getStartInputs():
    ## temperature input
    while True:
        try:
            initialTemperature = int(input('Introduce la temperatura inicial (ºC): '))
            if -50 <= initialTemperature <= 60:
                break
            else:
                print("La temperatura inicial debe estar entre -50 y 60.")
        except ValueError:
            print("La temperatura inicial debe ser un número entero.")
    ## rain chance input
    while True:
        try:
            initialRainChance = int(input('Introduce la probabilidad de lluvia inicial: '))
            if 0 <= initialRainChance <= 100:
                break
            else:
                print("La probabilidad de lluvia inicial debe estar entre 0 y 100.")
        except ValueError:
            print("La probabilidad de lluvia inicial debe ser un número entero.")
    ## days prediction input
    while True:
        try:
            days_prediction = int(input("Introduce el número de días de predicción: "))
            if days_prediction >= 0:
                break
            else:
                print("El número de días de predicción debe ser un número entero no negativo.")
        except ValueError:
            print("El número de días de predicción debe ser un número entero.")

    return initialTemperature, initialRainChance, days_prediction

## temperature change probability
def temperatureChange():
    rand = random.randint(0, 100)

    if rand >= 0 and rand <= 10:
        rand = random.choice([0, 1])
        if rand == 0:
            return 2
        return -2
    return False
    

def oracule_app():
    initialTemperature, initialRainChance, days_prediction = getStartInputs()

    rainyDays = 0

    temperature = initialTemperature
    rainChance = initialRainChance

    minTemperature = initialTemperature
    maxTemperature = initialTemperature
    

    for day in range(1, days_prediction + 1):
        temperatureChangeValue = temperatureChange()
        if temperatureChangeValue:
            temperature += temperatureChangeValue
        ## temperature change
        if temperature > 25:
            rainChance += 20        
        if temperature < 5:
            rainChance -= 20
        ##rain chances
        if rainChance >= 100:
            rainyDays += 1
            temperature -= 1
        ## temperature change in max and min
        if temperature > maxTemperature:
            maxTemperature = temperature
        if temperature < minTemperature:
            minTemperature = temperature
        

    print("\n")
    print("                      RESULTADOS                    ")
    print("----------------------------------------------------")
    print(f"Días de lluvia: {rainyDays}")
    print(f"Temperatura mínima: {minTemperature} ºC")
    print(f"Temperatura máxima: {maxTemperature} ºC")
    print("\n")



if __name__ == '__main__':
    oracule_app()
