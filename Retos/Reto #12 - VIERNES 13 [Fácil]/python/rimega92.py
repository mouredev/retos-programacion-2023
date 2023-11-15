from datetime import datetime

def existe_viernes_13(mes, anio):
    # Crear un objeto de fecha para el 13 del mes y año dados
    fecha_13 = datetime(anio, mes, 13)

    # Verificar si el día de la semana es viernes (código 4 en la librería datetime)
    return fecha_13.weekday() == 4

mes_ejemplo = 10  # Octubre
anio_ejemplo = 2023
resultado = existe_viernes_13(mes_ejemplo, anio_ejemplo)

if resultado:
    print(f'¡Sí existe un viernes 13 en {mes_ejemplo}/{anio_ejemplo}!')
else:
    print(f'No hay un viernes 13 en {mes_ejemplo}/{anio_ejemplo}.')