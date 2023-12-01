# Reto #45: El calendario de aDEViento 2023
#### Dificultad: Fácil | Publicación: 20/11/23 | Corrección: 27/11/23

## Enunciado

#
# ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
# 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
# Desde el 1 al 24 de diciembre.
#
# Crea un programa que simule el mecanismo de participación:
# - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
#   participantes, mostrarlos, lanzar el sorteo o salir.
# - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
# - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
#   (Y no lo duplicarás)
# - Si seleccionas mostrar los participantes, se listarán todos.
# - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
#   (Avisando de si lo has eliminado o el nombre no existe)
# - Si seleccionas realizar el sorteo, elegirás una persona al azar 
#   y se eliminará del listado.
# - Si seleccionas salir, el programa finalizará.
#
import random

participantes = []

print("Hola bienvenido o bienvenida a Calendario de aDEViento 2023\n")

print("1.Añadir participante\n2.Borrar participante\n3.Mostrar participantes\n4.Lanzar sorteo\n5.Salir")


while True:
    opcion = input("Introduce un numero del 1 al 5: ")
    if opcion == "1":
        username = input("\nIntroduce el nombre de usuario del participante que quieres agregar: ")
        if len(username) > 0:
            username.lower()
            el_nombre_de_usuario_ya_existe = False
            for i in participantes:
                if username == i:
                    print(f"Error: {username} ya estaba previamente en la lista")
                    el_nombre_de_usuario_ya_existe = True
                    break
            if not el_nombre_de_usuario_ya_existe:
                participantes.append(username)
                print(f"El nombre de usuario {username} se a añadido sin errores")
        else:
            print("No introduciste un nombre de usuario, porfavor intente de nuevo")
    elif opcion == "2":
        username = input("\nIntroduce el nombre de usuario que deseas eliminar: ")
        username.lower()
        if len(username) > 0:
            if username in participantes:
                participantes.remove(username)
                print(f"Se ha eliminado {username} de la lista.")
            else:
                print(f"El usuario {username} no esta en la lista")
        else:
            print("No introduciste un nombre de usuario, porfavor intente de nuevo")
    elif opcion == "3":
        print("")
        for i in participantes:
            print(i)
    elif opcion == "4":
        if participantes:
            ganador = random.choice(participantes)
            print(f"¡¡El ganador es {ganador}!!")
        else:
            print("No hay participantes en el sorteo")
    elif opcion == "5":
        break
    else:
        print("Opcion invalida")
        
print("Has salido sin problemas")