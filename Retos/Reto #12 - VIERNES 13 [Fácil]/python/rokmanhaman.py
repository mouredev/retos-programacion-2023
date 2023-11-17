"""
Reto #12: VIERNES 13
FÁCIL | Publicación: 20/03/23 | Resolución: 27/03/23
/*
 * Crea una función que sea capaz de detectar si existe un viernes 13
 * en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
"""
from datetime import datetime

def det_v13(year, month):
    fecha_especifica = datetime(year, month, 13)
    dia_de_la_semana = fecha_especifica.weekday()



    return True if fecha_especifica.weekday() == 4 else False

#2023 month 1 ==> True
#2023 month 10 ==> True
indicado = det_v13(2023, 11)
print(indicado)