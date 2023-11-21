"""
* Crea un juego interactivo por terminal en el que tendrás que adivinar 
 * el resultado de diferentes
 * operaciones matemáticas aleatorias (suma, resta, multiplicación 
 * o división de dos números enteros).
 * - Tendrás 3 segundos para responder correctamente.
 * - El juego finaliza si no se logra responder en ese tiempo.
 * - Al finalizar el juego debes mostrar cuántos cálculos has acertado.
 * - Cada 5 aciertos debes aumentar en uno el posible número de cifras 
 *   de la operación (cada vez en un operando):
 *   - Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
 *   - Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
 *   - Preguntas 11 a 15: XX operación YY
 *   - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
 """

import random
import time

nivel = 1

def establece_nivel():
    global nivel
    if nivel <= 5:
        x = 9
        y = 9
    elif nivel >5 and nivel <= 10:
        x = 99
        y = 9
    elif nivel > 10 and nivel <= 15:
        x = 99
        y = 99
    elif nivel > 15:
        x = 999
        y = 99

    return x, y

def sortea_operacion():
    operacion = random.choice(["+", "-", "*", "/"])

    return operacion

def sortea_numeros(x, y, operacion):
    operador_1 = random.randint(0, x)
    operador_2 = random.randint(0, y)
    if operacion == "/" and operador_2 == 0:
        operador_2 = random.randint(1, y)
    elif operacion == "/" and operador_2 > operador_1:
        operador_2 = random.randint(1, operador_1)
    pregunta = str(operador_1) + operacion + str(operador_2)

    return pregunta

def prepara_tablero():

    x, y = establece_nivel()

    operacion = sortea_operacion()

    pregunta = sortea_numeros(x, y, operacion)
    
    return pregunta

def a_jugar(pregunta, tiempo):
    global nivel
    calculo = eval(pregunta)
    ini_tiempo = time.time()
    resultado = int(input(f"Cual es el resultado de {pregunta} = "))
    fin_tiempo = time.time()

    if fin_tiempo - ini_tiempo > tiempo:
        print("\nHas perdido")
        print("Expiro el tiempo")
        return False
    elif resultado == round(calculo, 0):
        nivel += 1
        print(f"La respuesta es correcta, has pasado al nivel {nivel}\n")
        return True
    else:
        print("La respuesta es incorrecta, vuelve a intentarlo\n")
        return True

condicion = True
tiempo = 10
print("Vamos a jugar!!!")
print(f"Tienes {tiempo} segundos para responder cada operacion matematica.\n")
print(f"Estas en el nivel {nivel}")
print("*" * 25)

while condicion:
    pregunta = prepara_tablero()
    condicion = a_jugar(pregunta, tiempo)

print("*" * 25)
print("El juego se termino!!!")
print(f"Respondiste correctamente {nivel - 1} operaciones\n")
