"""
 Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 La función recibirá el mes y el año y retornará verdadero o falso.
 """
from datetime import datetime
#Función para saber si el año es bisiesto
def es_bisiesto(anyo):
    return anyo % 4 == 0 and (anyo % 100 != 0 or anyo % 400 == 0)
#Función principal
def reto12(mes, anyo):
    viernes_trece_si_no = False

    #Seleccionamos la cantidad de días según el mes introducido
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dias_mes = 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias_mes = 30
    elif mes == 2:
        if es_bisiesto(anyo):
            dias_mes = 29
        else:
            dias_mes = 28
    else:
        print ("Mes incorrecto")
        return
    
    #Para cada día formateamos la fecha y miramos el día de la semana
    for day in range(1, dias_mes+1):
        fecha_completa = f"{day:02d}-{mes:02d}-{anyo}"
        date = datetime.strptime(fecha_completa, "%d-%m-%Y")
        current_day = date.weekday()
        if current_day == 4 and day == 13:
            viernes_trece_si_no = True
    return viernes_trece_si_no
    
print(reto12(9, 2024))