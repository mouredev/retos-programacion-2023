import random

participants = []

while True:
    print("\nSeleccione una opción:")
    print("1. Añadir participante")
    print("2. Eliminar participante")
    print("3. Mostrar participantes")
    print("4. Realizar sorteo")
    print("5. Salir")

    option = input("Ingrese el número de la opción: ")

    if option == "5":
        break
    elif option == "1":
        name = input("Ingrese el nombre del participante: ")
        if name in participants:
            print("Este participante ya existe.")
        else:
            participants.append(name)
            print(f"{name} ha sido añadido.")
    elif option == "2":
        name = input("Ingrese el nombre del participante: ")
        if name not in participants:
            print("El participante no existe.")
        else:
            participants.remove(name)
            print(f"{name} ha sido eliminado.")
    elif option == "3":
        if not participants:
            print("No hay participantes.")
        else:
            print("Participantes:")
            for index, name in enumerate(participants):
                print(f"{index + 1}. {name}")
    elif option == "4":
        if not participants:
            print("No hay participantes para realizar el sorteo.")
        else:
            winner = random.choice(participants)
            print(f"El ganador es {winner}")
            participants.remove(winner)
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
