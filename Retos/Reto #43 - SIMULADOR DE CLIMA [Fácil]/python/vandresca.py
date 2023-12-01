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
 *     siguiente disminuya en un 20%.
 *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
 * - La función recibe el número de días de la predicción y muestra la temperatura
 *   y si llueve durante todos esos días.
 * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
 */
 """

import random

def getInitialClimaticConditions():
    init_temp = int(input("Introduce la temperatura inicial: "))
    init_pRain = int(input("Introduce el porcentaje de lluvia: "))
    return init_temp, init_pRain 

def isTemperatureChange():
    rand = random.randint(0, 100)
    if rand >= 0 and rand <= 10:
        return True
    return False

def is2GradeIncrease():
    rand = random.randint(0, 1)
    if rand == 0:
        return True
    return False

def calculateClimaticConditions(days_prediction):
    init_temp, init_pRain = getInitialClimaticConditions()
    temp_max = init_temp
    temp_min = init_temp
    daysOfRain = 0

    for _ in range(days_prediction):
        if isTemperatureChange():
            if is2GradeIncrease():
                init_temp += 2
            else:
                init_temp -= 2
        if init_temp > 25:
            init_pRain += 20
        if init_temp < 5:
            init_pRain -= 20

        if init_pRain >= 100:
            init_temp -= 1
            daysOfRain +=1
        
        if init_temp > temp_max:
            temp_max = init_temp
        if init_temp < temp_min:
            temp_min = init_temp

    if init_pRain >= 100:
        isRaining = "Sí"
    else:
        isRaining = "No" 

    print("Temperatura: "+ str(init_temp))
    print("Llueve: "+ isRaining)
    print("Temperatura máxima: "+ str(temp_max))
    print("Temperatura mínima: "+ str(temp_min))
    print("Días de lluvia: "+ str(daysOfRain))



days_prediction = int(input("Introduce el número de días de predicción: "))
calculateClimaticConditions(days_prediction)

