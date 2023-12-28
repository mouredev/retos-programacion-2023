"""
* Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
* - La función recibirá el mes y el año y retornará verdadero o falso.
"""
from datetime import date


def viernes_13(año: int, mes: int) -> bool:
    return date(year=año,
                month=mes,
                day=13).weekday() == 4


print(viernes_13(año=2022, mes=5))


def dia_viernes_13(año: int, mes: int) -> bool:

    dia: bool = lambda año, mes: date(year=año,
                                      month=mes,
                                      day=13).weekday() == 4

    return dia(año, mes)


print(dia_viernes_13(año=2012, mes=1))


"""
viernes_13 = lambda año, mes: date(year=año, month=mes, day=13).weekday() == 4

print(viernes_13(año=2022, mes=5))
    
"""
