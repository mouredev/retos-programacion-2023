'''/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */'''

import random


def generar_contrasena(N):
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S',
                  'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's',
                  't', 'u', 'v', 'w', 'x', 'y', 'z']
    simbolos = ['!', '#', '$', '&', '/',
                '(', ')', '=', '?', '¿', '¡', '}', '{', '[', ']', '*', '+', '-', '_', '.']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(N):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = ''.join(contrasena)
    return contrasena


print('Bienvenido al generador de contraseñas')
N = input('¿De cuantos caracteres quieres la contraseña? (Recomendado entre 8 y 16)')
try:
    N = int(N)
    generar_contrasena = generar_contrasena(N)
    print('\nTu nueva contraseña es: ' + generar_contrasena)

except:
    print('Debes introducir un número')
    exit()
