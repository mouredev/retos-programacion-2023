"""
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
"""

from datetime import datetime

def Friday_13th(month: int, year: int):
    date = datetime(year, month, 13)
    
    return True if date.isoweekday() == 5 else False #.isoweekday() no toma lunes como 0; más cómodo

print(Friday_13th(9, 2023))
print(Friday_13th(10, 2023))
