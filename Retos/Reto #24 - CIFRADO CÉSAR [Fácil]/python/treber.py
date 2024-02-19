# Reto #24: Cifrado César
#### Dificultad: Fácil | Publicación: 12/06/23 | Corrección: 19/06/23

## Enunciado

"""
/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */
"""
"""
Los símbolos no-alfabéticos como espacios y dígitos no cambian.
"""

import string

alfabeto = string.ascii_uppercase
posicion = int(input("Escriba un numero del 0 al 25: "))
alfabeto_coficado = alfabeto[posicion:] + alfabeto[:posicion]

def cifrado(texto):
    cifrado = ""
    for x in texto:
        if x not in alfabeto:
            cifrado = cifrado + x
        else:
            indice = alfabeto.index(x)
            cifrado = cifrado + alfabeto_coficado[indice]

    return cifrado


def descifrado(cifrado):
    descifrado = ""
    for x in cifrado:
        if x not in alfabeto_coficado:
            descifrado = descifrado + x
        else:
            indice = alfabeto_coficado.index(x)
            descifrado = descifrado + alfabeto[indice]

    return descifrado


texto = input("Escriba algo: ").upper()

cifrado = cifrado(texto)
print(f"El texto cifrado es: {cifrado}")

descifrado = descifrado(cifrado)
print(f"El texto descifrado es: {descifrado}")
