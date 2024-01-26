# Reto #12: Viernes 13
#### Dificultad: Fácil | Publicación: 20/03/23 | Corrección: 27/03/23

## Enunciado

"""
/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
"""

import datetime

# Recibir el mes y año indicado

day = 13

def friday_13():
    month = int(input("Ingresa el mes: "))
    anio = int(input("Ingresa el año: "))
    x = datetime.datetime(anio, month, day)
    value = x.strftime("%A")

    if value == "Friday":
        return True
    else:
        return False

print(friday_13())

