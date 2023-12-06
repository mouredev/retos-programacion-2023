import calendar

def is_viernes_13(mes, anio):
    
    # Retorna el día de la semana (0 es lunes) para year (1970–…), month (1–12), day (1–31)
    # y se guarda en la variable dia, 0 es lunes, martes es 1, miercoles es 3 y asi con todos los dias de la semana
    dia = calendar.weekday(anio, mes, 13)
    #print(dia)
    if dia == 4:
        return True
    
    return False
    
print(is_viernes_13(1, 2023))
print(is_viernes_13(12, 2022))
print(is_viernes_13(11, 2022))
print(is_viernes_13(10,2023))