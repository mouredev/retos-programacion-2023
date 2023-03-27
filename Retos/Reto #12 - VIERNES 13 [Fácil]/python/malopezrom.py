# /*
# * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
# * - La función recibirá el mes y el año y retornará verdadero o falso.
# */

from datetime import date


# /**
# * Listado de meses del año en castellano antiguo
# */
MOUNTHS = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


# /**
# * Funcion que determina si un mes tiene un viernes 13 o no
# * @ param month Mes a evaluar
# * @ param year Año a evaluar
# * @ return true si el mes tiene un viernes 13, false en caso contrario
# */
def hasFriday13(mes, anio):
    #Tan fácil como obtener el dia de la semana que corresponde al dia 13 de un mes y año dados y si es Viernes.. voila!
    return date(anio, mes, 13).weekday() == 4


# /**
# * Funcion que imprime si un mes tiene un viernes 13 o no
# * @ param month Mes a evaluar
# * @ param year Año a evaluar
# */
def printResult(mes, anio):
    print("El mes de", MOUNTHS[mes-1], "del año", anio, "" if hasFriday13(mes, anio) else "NO", "tiene viernes 13:")


printResult(3, 2020)
printResult(10, 2017)
printResult(1, 1985)
