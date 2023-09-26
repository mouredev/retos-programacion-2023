"""
    Reto #12: Viernes 13
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
     Publicación 20/03/23
     Realizado 21/03/23
"""

import calendar


def friday_13(month, year):
    if calendar.weekday(year, month, 13) == 4:
        return True
    else:
        return False


if __name__ == "__main__":
    print(friday_13(3, 108))
    print(friday_13(12, 2077))
    print(friday_13(10, 2023))
