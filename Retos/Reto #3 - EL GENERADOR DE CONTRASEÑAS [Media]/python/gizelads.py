""" Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
Podrás configurar generar contraseñas con los siguientes parámetros:
- Longitud: Entre 8 y 16.
- Con o sin letras mayúsculas.
- Con o sin números.
- Con o sin símbolos.
(Pudiendo combinar todos estos parámetros entre ellos) """
 

import random

def generar_contrasena(lon, may, min, num, sim):
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '^', '&', '$', '#', '"']
  
    if may == 'y' and min == 'y' and num == 'y' and sim == 'n':
        caracteres = mayusculas + minusculas + numeros
    elif may == 'y' and min == 'y' and num == 'n' and sim == 'y':
        caracteres = mayusculas + minusculas + simbolos
    elif may == 'y' and min == 'y' and num == 'n' and sim == 'n':
        caracteres = mayusculas + minusculas
    elif may == 'y' and min == 'n' and num == 'y' and sim == 'y':
        caracteres = mayusculas + numeros + simbolos
    elif may == 'y' and min == 'n' and num == 'y' and sim == 'n':
        caracteres = mayusculas + numeros
    elif may == 'y' and min == 'n' and num == 'n' and sim == 'y':
        caracteres = mayusculas + simbolos
    elif may == 'y' and min == 'n' and num == 'n' and sim == 'n':
        caracteres = mayusculas
    elif may == 'n' and min == 'y' and num == 'y' and sim == 'y':
        caracteres = minusculas + numeros + simbolos
    elif may == 'n' and min == 'y' and num == 'y' and sim == 'n':
        caracteres = minusculas + numeros
    elif may == 'n' and min == 'y' and num == 'n' and sim == 'y':
        caracteres = minusculas + simbolos
    elif may == 'n' and min == 'y' and num == 'n' and sim == 'n':
        caracteres = minusculas
    elif may == 'n' and min == 'n' and num == 'y' and sim == 'y':
        caracteres = numeros + simbolos
    elif may == 'n' and min == 'n' and num == 'y' and sim == 'n':
        caracteres = numeros
    elif may == 'n' and min == 'n' and num == 'n' and sim == 'y':
        caracteres = simbolos
    else:
        caracteres = mayusculas + minusculas + numeros + simbolos

    contrasena = []

    for i in range(lon):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    
    contrasena = ''.join(contrasena)
    return contrasena


def run():
    print('Bienvenido al generador de contraseñas, elige los siguientes parametros: ')
    lon = int(input('Longitud [8 - 16]: '))
    may = input('Mayusculas [y/n]: ')
    min = input('Minusculas [y/n]: ')
    num = input('Numeros [y/n]: ')
    sim = input('Simbolos [y/n]: ')

    if lon < 8 or lon > 16:
        print('Error: contraseña fuera de rango.')
    elif (may == 'y' or may == 'n') and (min == 'y' or min == 'n') and (num == 'y' or num == 'n') and (sim == 'y' or sim == 'n'):
        nueva_contrasena = generar_contrasena(lon, may, min, num, sim)
        print('Tu nueva contrasena es:', nueva_contrasena)
    else:
        print('Error: opcion invalida.')


if __name__ == '__main__':
    run()