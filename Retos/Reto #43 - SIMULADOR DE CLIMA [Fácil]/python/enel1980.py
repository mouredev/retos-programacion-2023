# /*
#  * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
#  * de un lugar ficticio al pasar un número concreto de días según estas reglas:
#  * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
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

# Mi solución
import random

def meteorologo()->list:
    final = [["D, T, P"]]
    temp = int(input("Ingrese temperatura inicial: "))
    prob_lluvia = int(input("Ingrese probabilidad de lluvia inicial: "))
    dias = int(input("¿Cuántos días vamos a estimar: "))
    for i in range(1, dias + 1):
        if prob_lluvia == 100:
            temp -= 1
        if random.randint(0,100) < 10:
            temp += 2
        if random.randint(0,100) > 90:
            temp -= 2
        if temp > 25:
            prob_lluvia += 20
            if prob_lluvia > 99:
                prob_lluvia = 100
        elif temp < 5:
            prob_lluvia -= 20      
            if prob_lluvia < 1:
                prob_lluvia = 0 

        print(f"La temperatura el dia {i} es: {temp} Celsius")
        print(f"La probabilidad de lluvia el dia {i} es: {prob_lluvia} %")
        final.append([f"{i}", f"{temp}" , f"{prob_lluvia}"]) # Por algún motivo no le gustaba el cambio de type
    return final
final = meteorologo()
for i in range(len(final)):
    print(final[i])