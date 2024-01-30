import random

participantes = []
options = ["1", "2", "3", "4", "5"]

while True:

    accion = input("Bienvenido al calendario de adviento. Escoge una acción a realizar: \n 1. Añadir participante \n 2. Mostrar participantes \n 3. Eliminar un participante \n 4. Realizar sorteo \n 5. Salir \n")

    while accion not in options:
        accion = input("Opción inválida. Intenta nuevamente. \n")

    if accion == "1":
        nombre = input("Ingresa el nombre del participante. \n")
        if nombre not in participantes:
            participantes.append(nombre)
        else:
            print("El participante ya existe. \n")

    elif accion == "2":
        if len(participantes) > 0:
            for participante in participantes:
                print(participante)
        else:
            print("Aún no hay participantes. \n")

    elif accion == "3":
        if len(participantes) > 0:
            nombre = input("Ingresa el nombre del participante a eliminar. \n")
            if nombre not in participantes:
                print("El participante no existe en la lista. \n")
            else:
                participantes.remove(nombre)
                print("El participante ha sido eliminado. \n")
        else:
            print("Aún no hay participantes. \n")
            
    elif accion == "4":
        if len(participantes) > 0:
            ganador = random.choice(participantes)
            print(f"El ganador de este sorteo es: {ganador} \n")
            participantes.remove(ganador)
        else:
            print("No hay participantes en la lista. \n")

    else:
        print("Adiós!")
        break