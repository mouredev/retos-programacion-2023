'''
    Crea un juego interactivo por terminal en el que tendrás que adivinar 
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
 *   - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY'''

import random
import time

aciertos = 0
numero_pregunta = 1

while True:

    signo = random.choice(['+', '-', '*', '/'])


    if numero_pregunta <= 5:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
    elif numero_pregunta > 5 and numero_pregunta <= 10:
        a = random.randint(0, 99)
        b = random.randint(0, 9)
    elif numero_pregunta > 10 and numero_pregunta <= 15:
        a = random.randint(10, 99)
        b = random.randint(10, 99)
    elif numero_pregunta > 15 and numero_pregunta <= 20:
        a = random.randint(0, 999)
        b = random.randint(0, 99)

  
    pregunta = f'{a} {signo} {b} '    
    print(pregunta)
    inicio_tiempo = time.time()

    try:
     
        respuesta_usuario = input("Respuesta: ")
        resultado = eval(pregunta)     
        respuesta_usuario = int(respuesta_usuario)

        if respuesta_usuario == resultado:
            aciertos += 1
            print("¡Correcto!\n")
        else:
            print(f"Incorrecto. La respuesta correcta es: {resultado}\n")
            break

    except ValueError:
        print("Debes ingresar un número válido.\n")

   
    tiempo_transcurrido = time.time() - inicio_tiempo

    if tiempo_transcurrido > 3:
        print("¡Lo siento, fuera de tiempo... han pasado sus 3 segundos!\n")
        break

print(f"¡Has conseguido {aciertos} aciertos! ¡Suerte la próxima vez!\n")
