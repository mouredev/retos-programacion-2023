import random

participantes = []

print("Calendario de aDEViento 2023")

while True:

    print("\n1. Añadir | 2. Eliminar | 3. Listar | 4. Sortear | 5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":

        nombre = input(
            "Introduce el nombre del participante que quieres añadir: ").lower()
        if nombre in participantes:
            print(f"El participante \"{nombre}\" ya existe.")
        else:
            participantes.append(nombre)
            print(f"Participante \"{nombre}\" añadido correctamente.")

    elif opcion == "2":

        nombre = input(
            "Introduce el nombre del participante que quieres eliminar: ").lower()
        if nombre in participantes:
            participantes.remove(nombre)
            print(f"Participante \"{nombre}\" eliminado correctamente.")
        else:
            print(f"El participante \"{nombre}\" no existe.")

    elif opcion == "3":

        print("Listado de participantes:")
        for participant in participantes:
            print(participant)

    elif opcion == "4":

        if participantes:
            nombre = random.choice(participantes)
            print(f"El ganador del sorteo es \"{nombre}\".")
            participantes.remove(nombre)
        else:
            print("No hay participantes para realizar el sorteo.")

    elif opcion == "5":

        print("Sorteo finalizado.")
        break

    else:
        print("Opción no válida. Selecciona otra opción.")