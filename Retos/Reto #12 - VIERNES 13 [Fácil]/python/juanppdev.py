import datetime

def es_viernes_13():
    mes = int(input("Ingrese el número del mes (1-12): "))
    año = int(input("Ingrese el año: "))

    fecha = datetime.datetime(año, mes, 13)
    return fecha.weekday() == 4

# Ejemplo de uso
if es_viernes_13():
    print("¡Hay un viernes 13 en el mes y año especificados!")
else:
    print("No hay un viernes 13 en el mes y año especificados.")
