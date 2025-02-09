
# * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
#  * - La función recibirá el mes y el año y retornará verdadero o falso.


from datetime import datetime


def viernes_13(mes, año):
    return datetime(año, mes, 13).weekday() == 4


print(viernes_13(6, 2025)) # True
print(viernes_13(6, 2026)) # False


