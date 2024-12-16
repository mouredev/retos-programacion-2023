# /*
#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
#  */

import random

def generar_contrasena(longitud, incluir_mayusculas, incluir_simbolos, incliur_numeros):
    letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
    letras_mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '0123456789'
    simbolos = '!@#$%^&*()_-+=<>?/[]{}|'

    caracteres = letras_minusculas

    if incluir_mayusculas == 'si':
        caracteres += letras_mayusculas    

    if incliur_numeros == 'si':
        caracteres += numeros

    if incluir_simbolos == 'si':
        caracteres += simbolos
    
    contrasena = []

    if incluir_mayusculas:
        contrasena.append(random.choice(letras_mayusculas))
    if incliur_numeros:
        contrasena.append(random.choice(numeros))
    if incluir_simbolos:
        contrasena.append(random.choice(simbolos))

    if not contrasena:
        raise ValueError('Debe incluir al menos un tipo de caracter para generar la contraseña')

    contrasena += [random.choice(caracteres) for _ in range(longitud)]

    random.shuffle(contrasena)

    return ''.join(contrasena)



def main():
    try:
        longitud = int(input("Introduce la longitud de la contraseña (entre 8 y 16): "))
        if longitud < 8 or longitud > 16:
            raise ValueError("La longitud debe estar entre 8 y 16.")

        incluir_mayusculas = input("¿Incluir mayúsculas? (si/no): ").strip().lower() == 'si'
        incluir_numeros = input("¿Incluir números? (si/no): ").strip().lower() == 'si'
        incluir_simbolos = input("¿Incluir símbolos? (si/no): ").strip().lower() == 'si'

        contrasena = generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)
        print(f"Contraseña generada: {contrasena}")
    except ValueError as e:
        print(f"Error: {e}")


main()


