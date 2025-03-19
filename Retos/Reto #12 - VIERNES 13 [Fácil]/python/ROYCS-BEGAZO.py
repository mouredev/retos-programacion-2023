import datetime
def viernes_13(mes, año):
    fecha = datetime.datetime(año, mes, 13)
    if fecha.strftime('%A') == 'Friday':
        return True
    return False
print(viernes_13(6,2025))