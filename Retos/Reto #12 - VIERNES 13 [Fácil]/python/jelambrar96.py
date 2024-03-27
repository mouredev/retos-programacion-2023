#!/usr/bin/python3

"""
# Reto #12: Viernes 13
/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
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


import datetime


def check_friday_13(month: int, year: int):
    temp_datetime = datetime.datetime.strptime(f"{year}-{str(month).zfill(2)}-{13}", "%Y-%m-%d") 
    weekday = temp_datetime.weekday()
    return weekday == 4


if __name__ == '__main__':
    
    for y in range(2000, 2021):
        for m in range(1, 13):
            bandera = check_friday_13(month=m, year=y)
            cadena = "Es viernes 13" if bandera else "NO es viernes 13"
            print(f"{y}-{str(m).zfill(2)}-{13}:\t", cadena)

