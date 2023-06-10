'''
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
 '''

import random
import string

def generaPassword(longitud, mayusculas=True, numeros=True, simbolos=True):
    caracteres = string.ascii_lowercase
    if mayusculas:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation
    
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

# Pedir al usuario que configure los parámetros
longitud = int(input("Longitud de la contraseña (entre 8 y 16): "))
mayusculas = input("Incluir letras mayúsculas (S/N): ").lower() == "s"
numeros = input("Incluir números (S/N): ").lower() == "s"
simbolos = input("Incluir símbolos (S/N): ").lower() == "s"

# Validar la longitud de la contraseña
if longitud < 8 or longitud > 16:
    print("Longitud inválida. La longitud debe estar entre 8 y 16.")
else:
    # Generar la contraseña
    contrasena = generaPassword(longitud, mayusculas, numeros, simbolos)
    print("Contraseña generada:", contrasena)
