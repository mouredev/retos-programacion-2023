#
# Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
# - La función recibirá el mes y el año y retornará verdadero o falso.
#

import calendar
from datetime import datetime

mes_str = input("Introduce un mes: ")
anio_str = input("Introduce el año: ")

# Convertimos a números enteros

try:
    mes = int(mes_str)
    anio = int(anio_str)

    # Hay que validar la entrada
    if 1 <= mes <= 12:
        # Crear objeto del datetime(cada día se establece en 13 por defecto)
        fecha = datetime(year=anio, month=mes, day=13)
        print("Fecha introducida:", fecha.strftime("%B de %Y"))
        # Verificar si el día 13 es viernes o no lo es
        if fecha.weekday() == calendar.FRIDAY:
            print("Hay un viernes 13 en", fecha.strftime("%B de %Y"))
        else:
            print("No hay un viernes 13 en", fecha.strftime("%B de %Y"))
    else:
        print("Mes invalidado. Introduce un número entre 1 y 12")
except ValueError:
    print("Entrada inválidada. Hay que introducir números para el mes y el año")
