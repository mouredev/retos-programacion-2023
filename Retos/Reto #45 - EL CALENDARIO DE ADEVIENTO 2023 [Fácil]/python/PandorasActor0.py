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

class Opciones:
    def __init__(self):
        self.Participantes = []

    def addparticipante(self,Nombre):
        if Nombre in self.Participantes:
            print("El participante ya esta concursando")
        else:
            self.Participantes.append(Nombre)
            print("Se agrego correctamente el participante {0}".format(Nombre))
    
    def eliminarParticipante(self,Nombre):
        if Nombre in self.Participantes:
            print("El participante {0} se elimino".format(Nombre))
            self.Participantes.remove(Nombre)
        else:
            print("El participante {0} No se encuentra registrado".format(Nombre))
    
    def mostrarParticipantes(self):
        if self.Participantes:
            print(self.Participantes)
        else:
            print("No tienes participantes registrados")

    def sorteo(self):
        if self.Participantes:
            ganador = random.choice(self.Participantes)
            print("El ganador es: {0}".format(ganador))
            self.Participantes.remove(ganador)
        else:
            print("No tiene participantes")

if __name__ == '__main__':
    opciones = Opciones()

    while True:
        print("\nmenu:")
        print("1. Agregar participante")
        print("2. Eliminar Participante")
        print("3. Mostrar Participantes")
        print("4. Realziar sorteo")
        print("5. Salir")

        opcion = input("Seleciona una opcion (1-5) : ")

        menu = {
            "1": lambda : opciones.addparticipante(input("Ingrese el Nombre del participante ")),
            "2": lambda : opciones.eliminarParticipante(input("Ingrese el Nombre del participante ")),
            "3": opciones.mostrarParticipantes,
            "4": opciones.sorteo,
            "5": lambda: print("¡Hasta Luego!") or exit(),
        }


        accion = menu.get(opcion, lambda: print("Opcion no valida."))

        accion()

        input("Presione Enter para continuar...")