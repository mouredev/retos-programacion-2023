import time

def temporizador(numInicio, intervalo = 1):
    # Estos loops no finalizarán hasta que el usuario introduzca unos valores correctos
    while numInicio <= 0:
        numInicio = int(input("Error al introducir el número con el que comienza la cuenta.\n Debes introducir un número mayor a 0: "))
    while intervalo <= 0:
        intervalo = int(input("Error al introducir el intervalo de tiempo.\n Debes introducir un número mayor a 0: "))

    # Bucle hasta que el temporizador llegue a 0
    while numInicio > 0:
        print(numInicio)
        numInicio -= 1
        time.sleep(intervalo)

# Recolección de datos
try:
    numInicio = int(input("Introduce el número de inicio: "))
    intervalo = int(input("Introduce el intervalo del temporizador: "))
except ValueError:
    print("Error. Solo se puede escribir un número")
    
# Llamada a la función
temporizador(numInicio, intervalo)