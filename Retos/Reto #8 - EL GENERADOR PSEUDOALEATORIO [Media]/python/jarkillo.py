'''/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */'''

from time import sleep
import datetime
import math


def pseudoaleatorio(digitos=2, contador=1, velocidad=0.2):
    '''Genera {contador} números pseudoaleatorios de {digitos} dígitos .
    Params: digitos: Número de dígitos del número pseudoaleatorio.
            contador: Número de números pseudoaleatorios a generar.'''

    for n in range(contador):
        current_time = datetime.datetime.now().timestamp()
        seconds = datetime.datetime.now().second
        minute = datetime.datetime.now().minute
        hour = datetime.datetime.now().hour
        day = datetime.datetime.now().day
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year
        microsecond = datetime.datetime.now().microsecond

        op1 = current_time * minute / 100 * hour / \
            15 * day / 30 * month / 12 * year / 100 - seconds

        op2 = op1 + datetime.datetime.now().second * 100000 / 1000 * minute / 100 * \
            day / 1000 * month * microsecond / 100 * year / \
            1000 / datetime.datetime.now().microsecond

        for n in range(datetime.datetime.now().second):
            op1 = op1 + n - op2 + datetime.datetime.now().microsecond * 100
            op3 = op1 + op2 - datetime.datetime.now().microsecond * 100
            op4 = op3 * 123478912 / \
                datetime.datetime.now().microsecond * math.pi
            op4 = int(op4*10*digitos)

        print(int(str(op4)[-digitos:]))
        sleep(velocidad)


contador = input('¿Cuantos números pseudoaleatorios quieres generar? ')
digitos = input('¿De cuantos dígitos quieres que sean? ')
velocidad = input(
    '¿A que velocidad quieres que se generen? (Recomendado: 0.5 - 1) ')

pseudoaleatorio(int(digitos), int(contador), float(velocidad))
