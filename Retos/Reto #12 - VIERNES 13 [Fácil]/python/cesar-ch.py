"""
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
"""
from datetime import datetime


def itsFridayThirteenth(month, year):
    return datetime(year, month, 13).weekday() == 4


print(itsFridayThirteenth(5, 2022))
print(itsFridayThirteenth(1, 2023))
