# Crea una función que sea capaz de detectar si existe un viernes 13
# en el mes y el año indicados.
# - La función recibirá el mes y el año y retornará verdadero o falso.
from datetime import date

def viernesTrece(anio:int, mes:int):
    semana = date(anio,mes,13).weekday()
    return True if semana == 4 else False

print(viernesTrece(2023, 10))
print(viernesTrece(2023, 3))
