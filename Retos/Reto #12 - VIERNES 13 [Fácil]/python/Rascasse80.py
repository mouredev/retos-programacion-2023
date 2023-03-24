"""
 Crea una función que sea capaz de detectar si existe un viernes 13
 en el mes y el año indicados.
 - La función recibirá el mes y el año y retornará verdadero o falso.
 """

import datetime


def viernes13(año, mes):

    fecha = datetime.date(año, mes, 13)

    if fecha.weekday()==4:
        return True
    else:
        return False
    
print(viernes13(2023, 10))