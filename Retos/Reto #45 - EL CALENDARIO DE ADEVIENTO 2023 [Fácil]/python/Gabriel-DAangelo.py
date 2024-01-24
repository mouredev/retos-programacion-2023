#reto 45
#25/nov/23
#Autor: Gabriel D'Angelo
print()

#Crear una lista vacía para almacenar participantes
participantes =[]
import random

print("        "  ,  "+  Menú   +")
print('''
+============================+
| 1) Añadir participante     |
| 2) Borrar participante     |
| 3) Mostrar Participante    |
| 4) Lanzar sorteo           |
| 5) Salir                   |
+============================+
'''
    )

while True:
    print()
    respuesta = int(input("Seleciona una opción para comenzar -> "))
    print()

    if respuesta == 1:
        nombre=input("Escribe el nombre del nuevo participante -> ").lower()
        if nombre not in participantes:
            participantes.append(nombre)
            print("Haz añadido a ","-> ",nombre," <-", "a los participantes")
        else:
            print("-> ",nombre," <-", "Ya existe")
            break
    
    elif respuesta == 2:
        nombre=input("Escribe el nombre del participante que deseas borrar -> ").lower()
        if nombre in participantes:
            participantes.remove(nombre)
            print("Haz eliminado a ","-> ",nombre," <-", "de los participantes")
        else:
            print("-> ",nombre," <-", "No es un participante")           
    
    elif respuesta == 3:
        print("+==== Lista de Participantes ====+")
        print(participantes)
    
    elif respuesta == 4:
        if len(participantes) > 0:
            ganador=random.choices(participantes)
            print("-> ",ganador," <-", "¡Que suerte! haz sido seleccionado ")
            participantes.remove(ganador)
        else:
            print("No hay participantes para el sorteo")
    
    elif respuesta == 5:
        print("+==== Gracias por participar en el sorteo +====")
        break
    
    else:
        print("Elige una opción válida")
