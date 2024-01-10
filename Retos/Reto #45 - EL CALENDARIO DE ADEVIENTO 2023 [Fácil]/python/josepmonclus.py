'''
¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
24 días, 24 regalos sorpresa relacionados con desarrollo de software.
Desde el 1 al 24 de diciembre.
Crea un programa que simule el mecanismo de participación:
- Mediante la terminal, el programa te preguntará si quieres añadir y borrar
  participantes, mostrarlos, lanzar el sorteo o salir.
- Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
- Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
  (Y no lo duplicarás)
- Si seleccionas mostrar los participantes, se listarán todos.
- Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
  (Avisando de si lo has eliminado o el nombre no existe)
- Si seleccionas realizar el sorteo, elegirás una persona al azar 
  y se eliminará del listado.
- Si seleccionas salir, el programa finalizará.
'''
import random

def print_menu():
    print('')
    print('¿Que quieres hacer?')
    print('  1 - Añadir participante')
    print('  2 - Borrar participante')
    print('  3 - Listar participantes')
    print('  4 - Realizar sorteo')
    print('  5 - Salir')
    
    while True:
        opcion = input('Opcion seleccionada: ')
        
        if opcion not in ['1', '2', '3', '4', '5']:
            print('Opción incorrecta')
        else:
            return opcion

participantes = []

while True:
    opcion = print_menu()
    
    if opcion == '1':
        nuevo_participante = input('\nNombre del nuevo participante: ')
        if nuevo_participante not in participantes:
            participantes.append(nuevo_participante)
            print('Participante añadido correctamente')
        else:
            print('ERROR: Participante ya existe!')
    elif opcion == '2':
        participante_a_borrar = input('\nNombre del participante a borrar: ')
        if participante_a_borrar in participantes:
            participantes.remove(participante_a_borrar)
            print('Participante borraco correctamente')
        else:
            print('ERROR: participante no existe!')
    elif opcion == '3':
        print('\nLista de participantes:')
        for participante in participantes:
            print(f'  - {participante}')
    elif opcion == '4':
        ganador = random.choice(participantes)
        print(f'Usuario ganador: {ganador}')
        participantes.remove(ganador)
    elif opcion == '5':
        print('\nPrograma finalizado!')
        break