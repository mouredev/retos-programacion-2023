# Crea un juego interactivo por terminal en el que tendrás que adivinar 
# el resultado de diferentes
# operaciones matemáticas aleatorias (suma, resta, multiplicación 
# o división de dos números enteros).
# - Tendrás 3 segundos para responder correctamente.
# - El juego finaliza si no se logra responder en ese tiempo.
# - Al finalizar el juego debes mostrar cuántos cálculos has acertado.
# - Cada 5 aciertos debes aumentar en uno el posible número de cifras 
#   de la operación (cada vez en un operando):
#   - Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
#   - Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
#   - Preguntas 11 a 15: XX operación YY
#   - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
#   ...

import random
from multiprocessing import TimeoutError
from multiprocessing.pool import ThreadPool

def timeout(seconds):
    def decorator(function):
        def wrapper(*args, **kwargs):
            pool = ThreadPool(processes=1)
            result = pool.apply_async(function, args=args, kwds=kwargs)
            try:
                return result.get(timeout=seconds)
            except TimeoutError as e:
                return e
        return wrapper
    return decorator

def seleccionar_operacion_matematica():
    rand = random.randint(1, 4)
    operacion = ""
    if rand == 1:
        operacion = "+"
    elif rand == 2:
        operacion = "-"
    elif rand == 3:
        operacion = "*"
    elif rand == 4:
        operacion = "/"
    else:
        operacion = ""
    return operacion

def generar_calculo_aleatorio(nivel_de_dificultad):
    valor1 = 0
    valor2 = 0

    if nivel_de_dificultad == 1:
        valor1 = int(random.randint(0,9))
        valor2 = int(random.randint(0,9))
    elif nivel_de_dificultad == 2:
        valor1 = int(random.randint(0,99))
        valor2 = int(random.randint(0,9))
    elif nivel_de_dificultad == 3:
        valor1 = int(random.randint(0,99))
        valor2 = int(random.randint(0,99))
    elif nivel_de_dificultad == 4:
        valor1 = int(random.randint(0,999))
        valor2 = int(random.randint(0,99))
    elif nivel_de_dificultad == 5:
        valor1 = int(random.randint(0,999))
        valor2 = int(random.randint(0,999))
    elif nivel_de_dificultad == 6:
        valor1 = int(random.randint(0,9999))
        valor2 = int(random.randint(0,999))
    elif nivel_de_dificultad == 7:
        valor1 = int(random.randint(0,9999))
        valor2 = int(random.randint(0,9999))
    elif nivel_de_dificultad == 8:
        valor1 = int(random.randint(0,99999))
        valor2 = int(random.randint(0,9999))
    elif nivel_de_dificultad == 9:
        valor1 = int(random.randint(0,99999))
        valor2 = int(random.randint(0,99999))
    elif nivel_de_dificultad == 10:
        valor1 = int(random.randint(0,999999))
        valor2 = int(random.randint(0,99999))
    else:
        print("Eres un genio de las matemáticas!\nMejor estudia algo de literatura!")
        valor1 = -1
        valor2 = -1

    operacion = seleccionar_operacion_matematica()

    if operacion == "/" and valor2 == 0:
        valor2 = 1

    return [valor1, operacion, valor2]

def calcular_respuesta_correcta(valor1, operacion, valor2):
    resultado = 0
    if operacion == "+":
        resultado = valor1 + valor2
    elif operacion == "-":
        resultado = valor1 - valor2
    elif operacion == "*":
        resultado = valor1 * valor2
    elif operacion == "/":
        resultado = valor1 / valor2
    else:
        print("Operación invalida")
    return resultado

@timeout(3)
def leer_respuesta_del_jugador(calculo):
    return float(input(str(calculo[0]) + " " + calculo[1] + " " + str(calculo[2]) + " = "))

def empiezar_juego_nuevo():
    fin_del_juego = False
    respuestas_correctas = 49
    nivel_de_dificultad = 10

    while fin_del_juego == False:
        calculo = generar_calculo_aleatorio(nivel_de_dificultad)
        
        if calculo[0] < 0:
            print("Fin del juego! :D\nTu puntuación: " + str(respuestas_correctas) + " respuestas correctas")
            break
        
        respuesta_del_jugador = leer_respuesta_del_jugador(calculo)
        
        if isinstance(respuesta_del_jugador, TimeoutError):
            fin_del_juego = True
            print("\nFin del juego! :(\nTu puntuación: " + str(respuestas_correctas) + " respuestas correctas")
            break
        
        respuesta_correcta = calcular_respuesta_correcta(calculo[0], calculo[1], calculo[2])
        
        if respuesta_del_jugador == respuesta_correcta:
            respuestas_correctas += 1
            if respuestas_correctas >= (nivel_de_dificultad * 5):
                nivel_de_dificultad += 1
        else:
            fin_del_juego = True
            print("Fin del juego! :(\nTu puntuación: " + str(respuestas_correctas) + " respuestas correctas")
            
empiezar_juego_nuevo()

