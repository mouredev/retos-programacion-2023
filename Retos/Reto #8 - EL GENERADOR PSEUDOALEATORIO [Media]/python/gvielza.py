import datetime
hora_actual=datetime.datetime.now()  ##obtengo la hora actual
print(hora_actual)

numero=hora_actual.microsecond 
print(numero%100)