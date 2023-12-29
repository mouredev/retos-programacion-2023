"""
/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
"""

import datetime

def viernes_trece(mes, anio):
        return True if datetime.date(int(anio), int(mes), 13).weekday() == 4 else False

mes = input("Introduce el mes: ")
anio = input("Introduce el año: ")
print(viernes_trece(mes, anio))
