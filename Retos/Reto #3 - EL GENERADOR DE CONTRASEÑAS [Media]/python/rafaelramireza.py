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

def generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos):
    caracteres = string.ascii_lowercase # Genera un string con todas las letras minúsculas
    if incluir_mayusculas: # Si se incluyen mayúsculas, se añaden al string
        caracteres += string.ascii_uppercase # Genera un string con todas las letras mayúsculas
    if incluir_numeros: # Si se incluyen números, se añaden al string
        caracteres += string.digits # Genera un string con todos los números
    if incluir_simbolos: # Si se incluyen símbolos, se añaden al string
        caracteres += string.punctuation # Genera un string con todos los símbolos

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud)) # Genera una contraseña aleatoria
    return contrasena # Devuelve la contraseña generada

def main():
    longitud = random.randint(8, 16) # Genera un número aleatorio entre 8 y 16
    incluir_mayusculas = random.choice([True, False]) # Genera un booleano aleatorio
    incluir_numeros = random.choice([True, False]) # Genera un booleano aleatorio
    incluir_simbolos = random.choice([True, False]) # Genera un booleano aleatorio

    contrasena = generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos) # Genera la contraseña
    print(f"Contraseña generada: {contrasena}")

if __name__ == "__main__": # Permite ejecutar este script directamente
    main() # Ejecuta la función main
