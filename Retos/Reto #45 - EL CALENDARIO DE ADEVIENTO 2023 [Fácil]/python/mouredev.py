import random

participants = []

print("Calendario de aDEViento 2023")

while True:

    print("\n1. Añadir | 2. Eliminar | 3. Listar | 4. Sortear | 5. Salir")

    option = input("Selecciona una opción: ")

    if option == "1":

        name = input(
            "Introduce el nombre del participante que quieres añadir: ").lower()
        if name in participants:
            print(f"El participante \"{name}\" ya existe.")
        else:
            participants.append(name)
            print(f"Participante \"{name}\" añadido correctamente.")

    elif option == "2":

        name = input(
            "Introduce el nombre del participante que quieres eliminar: ").lower()
        if name in participants:
            participants.remove(name)
            print(f"Participante \"{name}\" eliminado correctamente.")
        else:
            print(f"El participante \"{name}\" no existe.")

    elif option == "3":

        print("Listado de participantes:")
        for participant in participants:
            print(participant)

    elif option == "4":

        if participants:
            name = random.choice(participants)
            print(f"El ganador del sorteo es \"{name}\".")
            participants.remove(name)
        else:
            print("No hay participantes para realizar el sorteo.")

    elif option == "5":

        print("Sorteo finalizado.")
        break

    else:
        print("Opción no válida. Selecciona otra opción.")
