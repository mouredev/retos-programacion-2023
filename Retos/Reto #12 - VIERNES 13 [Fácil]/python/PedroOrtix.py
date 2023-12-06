# /*
#  * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
#  * - La función recibirá el mes y el año y retornará verdadero o falso.
#  */

import datetime

def viernes13(month, year):
    return datetime.datetime(year, month, 13).weekday() == 4

print(viernes13(3, 2020)) # True