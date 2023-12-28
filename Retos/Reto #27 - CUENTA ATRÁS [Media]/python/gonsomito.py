"""
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
"""
# Importamos la librería "time" para controlar las pausas de intervalos
import time

# la función "lapso" solicita al usuario el número desde el cual empezar a contar. Controlamos que solo salgan enteros positivos
def lapso():
    while True:
        cont_lapso = input("Cuenta atrás desde: ")
        if cont_lapso.isdigit():
            return int(cont_lapso)
        else:
            print("Vuleve a introducir desde que número empezar\n\n")

# la función "segundero" solicita al usuario el tiempo de espera entre cada número. Controlamos que solo salgan enteros positivos
def segundero():
    while True:
        cont_segundos = input("Tiempo de espera entre : ")
        if cont_segundos.isdigit():
            return int(cont_segundos)
        else:
            print("Vuleve a introducir tiempo de espera\n\n")

# la función "the_final_countdown" realiza la cuenta regresiva con los valores ingresados por el usuario.
def the_final_countdown(num_desde, num_seg):
    print("\n\n")
    while num_desde >= 0:
        print(num_desde)
        time.sleep(num_seg) 
        num_desde = num_desde - 1

the_final_countdown(lapso(), segundero())
