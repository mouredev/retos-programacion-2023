"""
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
"""

from datetime import datetime

def isFridayThirteen(month, year):

    date = datetime(year, month, 13)
    return date.weekday() == 4


print(isFridayThirteen(1, 2023))        # True
print(isFridayThirteen(3, 2022))        # False
print(isFridayThirteen(3, 2020))        # True
print(isFridayThirteen(9, 2024))        # True