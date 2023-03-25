# Reto #12: Viernes 13
#### Dificultad: Fácil | Publicación: 20/03/23 | Corrección: 27/03/23

## Enunciado

#
# Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
# - La función recibirá el mes y el año y retornará verdadero o falso.
#

import datetime


def is_friday_13(month, year):

    # Creamos un objeto datetime para el 13 del month y año indicados
    date = datetime.date(year, month, 13)

    # Comprobamos si es viernes (el número 4 representa el día viernes)
    if date.weekday() == 4:
        return True
    else:
        return False


if __name__ == "__main__":
    month = int(input("Ingresa el mes (número del 1 al 12): "))
    year = int(input("Ingresa el año (número de 4 dígitos): "))
    print(is_friday_13(month, (year)))
