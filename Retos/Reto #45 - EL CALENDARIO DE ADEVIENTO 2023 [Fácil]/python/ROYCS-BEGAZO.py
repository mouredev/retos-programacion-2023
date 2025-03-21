import random
import time

participantes = []

def agregar(nombre : str):
    if nombre in participantes:
        print(f'el participante ya se encuentra registrado')
    else:
        participantes.append(nombre)
        print(f'participante {nombre} agregado correctamente')

def seleccionar():
    ganador = random.choice(participantes)
    participantes.remove(ganador)
    print(ganador)

def listar():
    for index ,participante in enumerate(participantes,1):
        print(f'{index}°{participante}')



while True:
    print(f'BIENVENIDO AL SORTEO DE SUSCRPTORES')
    print(f'ingrese una opcion para continuar')
    print(f'1)Agregar participante\n2) Mostrar participantes\n3)Empezar sorteo\n4)Salir')
    opcion =input('ingrese su opcion: ')
    match opcion:
        case '1':
            nombre = input('ingrese el nombre del participante ')
            agregar(nombre)
        case '2':
            listar()
            enter = input('presiones [ENTER] para continuar')
        case '3':
            if len(participantes) < 2:
                print('no hay suficientes participantes activos, porfavor ingrese participantes')
            else:
                seleccionar()
                enter = input('presiones [ENTER] para continuar')
        case '4':
            print('saliendo del programa')
            break
        case _:
            print('ingrese una opcion valida')
            enter = input('presiones [ENTER] para continuar')

