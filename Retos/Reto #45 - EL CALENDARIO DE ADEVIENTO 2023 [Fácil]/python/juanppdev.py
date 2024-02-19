import random

participantes = []

def mostrar_participantes():
    print("Lista de participantes:")
    for participante in participantes:
        print(participante)
    print()

def agregar_participante():
    nombre = input("Introduce el nombre del participante: ")
    if nombre in participantes:
        print("Este participante ya existe.")
    else:
        participantes.append(nombre)
        print(f"{nombre} ha sido añadido correctamente.")

def eliminar_participante():
    nombre = input("Introduce el nombre del participante que deseas eliminar: ")
    if nombre in participantes:
        participantes.remove(nombre)
        print(f"{nombre} ha sido eliminado correctamente.")
    else:
        print("Este participante no existe en la lista.")

def realizar_sorteo():
    if participantes:
        ganador = random.choice(participantes)
        print(f"¡El ganador del sorteo es: {ganador}!")
        participantes.remove(ganador)
    else:
        print("No hay participantes para realizar el sorteo.")

def main():
    while True:
        print("1. Añadir participante")
        print("2. Mostrar participantes")
        print("3. Eliminar participante")
        print("4. Realizar sorteo")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            agregar_participante()
        elif opcion == "2":
            mostrar_participantes()
        elif opcion == "3":
            eliminar_participante()
        elif opcion == "4":
            realizar_sorteo()
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
