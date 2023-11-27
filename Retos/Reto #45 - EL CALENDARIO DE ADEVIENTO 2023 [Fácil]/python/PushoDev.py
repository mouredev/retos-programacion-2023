# Reto #45: El calendario de aDEViento 2023
# Dificultad: Fácil | Publicación: 20/11/23 | Corrección: 27/11/23
#-----------------------------------------------------------------
# ENUNCIADO DEL EJERCICIO
#-----------------------------------------------------------------
# /*
#  * ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
#  * 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
#  * Desde el 1 al 24 de diciembre.
#  *
#  * Crea un programa que simule el mecanismo de participación:
#  * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
#  *   participantes, mostrarlos, lanzar el sorteo o salir.
#  * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
#  * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
#  *   (Y no lo duplicarás)
#  * - Si seleccionas mostrar los participantes, se listarán todos.
#  * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
#  *   (Avisando de si lo has eliminado o el nombre no existe)
#  * - Si seleccionas realizar el sorteo, elegirás una persona al azar 
#  *   y se eliminará del listado.
#  * - Si seleccionas salir, el programa finalizará.
#-----------------------------------------------------------------

import random


print ("Pushodev")
print ("https://github.com/PushoDev")

class CalendarioAdvento:
    def __init__(self):
        self.participantes = []

    def agregar_participante(self, nombre):
        if nombre in self.participantes:
            print(f"{nombre} ya está en la lista de participantes.")
        else:
            self.participantes.append(nombre)
            print(f"{nombre} ha sido añadido a la lista.")

    def mostrar_participantes(self):
        if not self.participantes:
            print("No hay participantes en la lista.")
        else:
            print("Lista de participantes:")
            for participante in self.participantes:
                print(participante)

    def eliminar_participante(self, nombre):
        if nombre in self.participantes:
            self.participantes.remove(nombre)
            print(f"{nombre} ha sido eliminado de la lista.")
        else:
            print(f"{nombre} no existe en la lista de participantes.")

    def realizar_sorteo(self):
        if not self.participantes:
            print("No hay participantes para realizar el sorteo.")
        else:
            participante_ganador = random.choice(self.participantes)
            print(f"¡El ganador del sorteo es: {participante_ganador}!")
            self.participantes.remove(participante_ganador)

# Función principal
def calendario_advento():
    calendario = CalendarioAdvento()

    while True:
        print("\n--- Calendario de aDEViento 2023 ---")
        print("1. Añadir participante")
        print("2. Mostrar participantes")
        print("3. Eliminar participante")
        print("4. Realizar sorteo")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            nombre_participante = input("Ingrese el nombre del participante: ")
            calendario.agregar_participante(nombre_participante)
        elif opcion == "2":
            calendario.mostrar_participantes()
        elif opcion == "3":
            nombre_participante = input("Ingrese el nombre del participante a eliminar: ")
            calendario.eliminar_participante(nombre_participante)
        elif opcion == "4":
            calendario.realizar_sorteo()
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

# Ejecutar el programa
calendario_advento()

print("Gracias por Participar......")