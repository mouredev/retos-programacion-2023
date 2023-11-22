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

class ParticipantManager:
    def __init__(self):
        self.participants = {}

    def add_participant(self, name):
        if name in self.participants:
            print(f"El participante '{name}' ya existe.")
        else:
            self.participants[name] = True
            print(f"El participante '{name}' ha sido añadido.")

    def show_participants(self):
        if self.participants:
            print("Lista de participantes:")
            for participant in self.participants:
                print(participant)
        else:
            print("No hay participantes registrados.")

    def remove_participant(self, name):
        if name in self.participants:
            del self.participants[name]
            print(f"El participante '{name}' ha sido eliminado.")
        else:
            print(f"El participante '{name}' no existe en la lista.")

    def draw(self):
        if self.participants:
            selected_participant = random.choice(list(self.participants.keys()))
            print(f"El participante sorteado es:  {selected_participant}")
            del self.participants[selected_participant]
        else:
            print("No hay participantes para realizar el sorteo.")

def main():
    manager = ParticipantManager()

    while True:
        print("\nQué acción deseas realizar?")
        print("1. Añadir participante")
        print("2. Mostrar participantes")
        print("3. Eliminar participante")
        print("4. Realizar sorteo")
        print("5. Salir")
        
        option = input("Ingresa tu selección ")
        
        if option == '1':
            name = input("Ingresa el nombre del participante: ")
            manager.add_participant(name)
        elif option == '2':
            manager.show_participants()
        elif option == '3':
            name = input("Ingresa el nombre del participante a eliminar: ")
            manager.remove_participant(name)
        elif option == '4':
            manager.draw()
        elif option == '5':
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.")

if __name__ == "__main__":
    main()

