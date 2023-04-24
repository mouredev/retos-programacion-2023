"""
 * Crea una función que sea capaz de detectar si existe un viernes 13
 * en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
"""
from datetime import datetime           #creo que vamos a necesitar esto para usar weekday()

def viernes_13(mes, ano):
    fecha = datetime(ano, mes, 13)
    if fecha.weekday() == 4:            #weekday() parte de 0=lunes,(...), 4=viernes, 5=sábado, 6=domingo
        return True                     #Si es 4 es TRUE y nos vamos.
    return False
    
#Pedimos Mes y año. 
#Habría que controlar que se metan bien los datos, pero hoy no me apetece.
#Me haces el favor de no meter cosas raras, vale?
mes = int(input("Que Mes (MM)?")[0:2])
ano = int(input("Que Año (AAAA)?")[0:4])

print(viernes_13(mes, ano))
