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

class CalendarioAdvento:
    def __init__(self):
        self.participantes = []

    def agregar_participante(self, nombre):
        if nombre in self.participantes:
            print(f"{nombre} ya está en la lista.")
        else:
            self.participantes.append(nombre)
            print(f"{nombre} ha sido añadido.")

    def mostrar_participantes(self):
        print("Lista de participantes:")
        for participante in self.participantes:
            print(participante)

    def eliminar_participante(self, nombre):
        if nombre in self.participantes:
            self.participantes.remove(nombre)
            print(f"{nombre} ha sido eliminado.")
        else:
            print(f"{nombre} no se encuentra en la lista.")

    def realizar_sorteo(self):
        if not self.participantes:
            print("No hay participantes para realizar el sorteo.")
        else:
            ganador = random.choice(self.participantes)
            print(f"¡El ganador es: {ganador}!")
            self.participantes.remove(ganador)

if __name__ == "__main__":
    calendario = CalendarioAdvento()

    while True:
        print("\n--- Calendario de aDEViento ---")
        print("1. Añadir participante")
        print("2. Mostrar participantes")
        print("3. Eliminar participante")
        print("4. Realizar sorteo")
        print("5. Salir")

        try:
            opcion = int(input("Selecciona una opción (1-5): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if opcion == 1:
            nombre_participante = input("Introduce el nombre del participante: ")
            calendario.agregar_participante(nombre_participante)

        elif opcion == 2:
            calendario.mostrar_participantes()

        elif opcion == 3:
            nombre_participante = input("Introduce el nombre del participante a eliminar: ")
            calendario.eliminar_participante(nombre_participante)

        elif opcion == 4:
            calendario.realizar_sorteo()

        elif opcion == 5:
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")
