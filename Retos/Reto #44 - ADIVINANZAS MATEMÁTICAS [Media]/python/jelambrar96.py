#!/usr/bin/python3

"""
# Reto #44: Adivinanzas matemáticas
/*
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
 *   ...
 */
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

from pynput.keyboard import Key, KeyCode, Listener
from random import choice, randint
from time import time, sleep
from threading import Thread, Lock


LISTA_OPERACIONES = (
    ("+", lambda x,y: x + y),
    ("*", lambda x,y: x * y),
    ("-", lambda x,y: x - y),
    ("//", lambda x,y: x // y),
    ("%", lambda x,y: x % y),
)

NIVELES = [
    ((0, 9), (0, 9)),
    ((0, 99), (0, 9)),
    ((0, 99), (0, 99)),
    ((0, 999), (0,99)),
]

KEY_CODES = [
    KeyCode.from_char("0"),
    KeyCode.from_char("1"),
    KeyCode.from_char("2"),
    KeyCode.from_char("3"),
    KeyCode.from_char("4"),
    KeyCode.from_char("5"),
    KeyCode.from_char("6"),
    KeyCode.from_char("7"),
    KeyCode.from_char("8"),
    KeyCode.from_char("9"),
]

class JuegoMatematicas():

    def __init__(self, limite_segundos: int, vidas: int):
        self._seq = []
        self._code = None
        self._limite_segundos = limite_segundos
        self._contador_preguntas = 0
        self._vidas = vidas
        self._lock_sequence = Lock()
        self._lock_exit = Lock()
        self._exit_flag = False


    def _read_secuence(self):
        self._lock_sequence.acquire()
        temp_secuence = self._seq[:]
        self._lock_sequence.release()
        return temp_secuence

    def _write_secuence(self, nueva_secuencia):
        self._lock_sequence.acquire()
        self._seq[:] = nueva_secuencia
        self._lock_sequence.release()

    def _set_exit(self, flag):
        self._lock_exit.acquire()
        self._exit_flag = flag
        self._lock_exit.release()

    def _get_exit(self):
        self._lock_exit.acquire()
        flag = self._exit_flag 
        self._lock_exit.release()
        return flag

    def _check_key(self, key):
        # if key == Key.enter:
        #     self._write_secuence([])
        if key == Key.backspace:
            temp_secuence = self._read_secuence()
            temp_secuence.pop()
            self._write_secuence(temp_secuence)
        if key in KEY_CODES:
            temp_secuence = self._read_secuence()
            temp_secuence.append(KEY_CODES.index(key))
            self._write_secuence(temp_secuence)
        if key == KeyCode.from_char('q'):
            self._set_exit(True)
        # print(key)

    def start(self):
        self._code = Listener(self._check_key)
        self._code.start()
        game_thread = Thread(target=self._loop)
        game_thread.start()
        game_thread.join()
        self._code.stop()

    def _calular_nivel(numero_preguntas):
        return min((numero_preguntas + 1)//5, 3)

    def _time_info(t1, t2, limit_time):
        # print()
        # print(t1)
        # print(t2)
        # print(limit_time)
        rest_time = int((limit_time - (t2 - t1)) * 1e3)
        # print(rest_time)
        # print()
        milliseconds = rest_time % 1000
        rest_time //= 1000 
        seconds = rest_time % 60
        rest_time //= 60 
        minutes = rest_time % 60 
        return f"{minutes:02}:{seconds:02}.{milliseconds:03}"

    def exit(self):
        pass

    def _loop(self, ):


        time_question = time()
        while True:
            current_time = time()
            time_info = JuegoMatematicas._time_info(time_question, current_time, self._limite_segundos)
            print("EL JUEGO COMIENZA EN: ", time_info, "\r", end="")
            if (time_question + self._limite_segundos) <= current_time:
                print()
                break

        while self._vidas > 0 and self._get_exit() == False:

            operacion = choice(LISTA_OPERACIONES)
            nivel = JuegoMatematicas._calular_nivel(self._contador_preguntas)
            operador1 = randint(*NIVELES[nivel][0])
            operador2 = randint(*NIVELES[nivel][1]) 


            if operacion[0] in  ["//", "%"] and operador2 == 0:
                continue

            respuesta = operacion[1](operador1, operador2)
            if respuesta < 0:
                continue

            cadena_operacion = f"{operador1} {operacion[0]} {operador2} = "

            # print(cadena_operacion, respuesta)

            time_question = time()
            while True:
                current_time = time()
                time_info = JuegoMatematicas._time_info(time_question, current_time, self._limite_segundos)

                secuencia = self._read_secuence()
                str_secuencia = "".join([str(item) for item in secuencia])

                print("TIEMPO:", time_info, "\tVIDAS:", "+" * self._vidas, "\t", cadena_operacion,  str_secuencia, "\r", end="")
                if (time_question + self._limite_segundos) <= current_time:
                    self._vidas -= 1
                    break

                respuesta_secuencia = sum([ item * 10 ** i for i, item in enumerate(reversed(secuencia))], 0) if len(secuencia) > 0 else -1
                # respuesta_secuencia = int(str_secuencia)

                if respuesta_secuencia == respuesta:
                    self._contador_preguntas += 1
                    self._write_secuence([])
                    print()
                    print()
                    break

                sleep(0.001)

        print()
        input("game over. presione enteer para salir")




if __name__ == '__main__':
    jm = JuegoMatematicas(limite_segundos=3, vidas=3)
    jm.start()

