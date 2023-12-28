'''
 * ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
 * 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
 * Desde el 1 al 24 de diciembre.
 *
 * Crea un programa que simule el mecanismo de participación:
 * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
 *   participantes, mostrarlos, lanzar el sorteo o salir.
 * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
 * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
 *   (Y no lo duplicarás)
 * - Si seleccionas mostrar los participantes, se listarán todos.
 * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
 *   (Avisando de si lo has eliminado o el nombre no existe)
 * - Si seleccionas realizar el sorteo, elegirás una persona al azar 
 *   y se eliminará del listado.
 * - Si seleccionas salir, el programa finalizará.'''
from random import choice
class Sorteo:
    def __init__(self):
        self.participantes=[]
        self.participantes_premiados=[]
        self.premios=[]
    def menu(self):
        return '''
    1- Añadir participate
    2- Mostrar los participantes
    3- Eliminar
    4- Relalizar Sorteo
    5- Salir
    '''
    def incluir(self):
        self.name=input('Introduce el nombre del participante: ')
        if self.name in self.participantes:
            return f'{self.name} ya está incluido en la lista de participantes'
        else:
            self.participantes.append(self.name)
    def mostrar(self):
        for i in self.participantes:
            print(i)
    def eliminar(self):
        self.name=input('Introduce el nombre del participante a eliminar: ')
        if self.name in self.participantes:
            self.participantes.remove(self.name)
            return f'{self.name} ha sido eliminado de la lista de participantes'
        else:
            return f'{self.name} no se encuentra en la lista de participantes.'
    def sorteo(self):
        premiado=choice(self.participantes)
        if premiado in self.participantes_premiados:
            self.sorteo()
        else:
            self.participantes_premiados.append(premiado)
            return f' El participante premiado ha sido {premiado}'
    


s=Sorteo()

if __name__ == "__main__":
    while True:
        print(s.menu())
        opc=int(input('Introduce un opción: '))
        if opc == 1:
            print(s.incluir())
        elif opc == 2:
            s.mostrar()
        elif opc ==3:
            print(s.eliminar())
        elif opc == 4:
            print(s.sorteo())
        elif opc == 5:
            break
        else:
            print('Ha intruducido un valor erróneo.')

        

