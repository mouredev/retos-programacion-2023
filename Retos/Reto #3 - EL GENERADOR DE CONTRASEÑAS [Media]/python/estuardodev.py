'''
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
'''

import random

def main():
    print("------------------------------------------------------")
    print("--             Generador de Contraseñas             --")
    print("--              Hecho por @estuardodev              --")
    print("--                   -------------                  --")
    print("--        Antes debemos configurar unas cosas       --")
    print("------------------------------------------------------")

    longitud = int(input("\nIngresa la longitud de tu contraseña (Entre 8 y 16): "))
    if not (8 <= longitud <= 16):
        print("Ingresa valores válidos por favor.")
        exit()

    con_sin_mayusculas = pregunta("mayúsculas")
    con_sin_numeros = pregunta("números")
    con_sin_simbolos = pregunta("símbolos")

    password = generador_password(longitud, con_sin_mayusculas, con_sin_numeros, con_sin_simbolos)

    print("\nTu contraseña nueva es:", password, "\n\nNUNCA COMPARTAS TU CONTRASEÑA CON NADIE.")

def generador_password(longitud, mayusculas, numeros, simbolos):
    password = ""

    while len(password) < longitud:
        if mayusculas == 1:
            pilar = abecedario(True)
            password += pilar
        else:
            pilar = abecedario(False)
            password += pilar

        if numeros == 1:
            pilar = generar_numeros()
            password += pilar

        if simbolos == 1:
            pilar = caracteres()
            password += pilar

    return password

def pregunta(palabra):
    dato = int(input(f"\n¿Deseas {palabra}?\n[1] - SI\n[0] - NO\nRespuesta: "))
    if not (0 <= dato <= 1):
        print("Ingresa valores válidos por favor.")
        exit()

    return dato

def abecedario(mayuscula):
    ABC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    abc = "abcdefghijklmnñopqrstuvwxyz"

    if mayuscula:
        ABCabc = ABC + abc
        return random.choice(ABCabc)
    else:
        return random.choice(abc)

def generar_numeros():
    nums = "0123456789"
    return random.choice(nums)

def caracteres():
    caracteres = "!{}+¿°!#%$%/&(&()/?¡_.,.-{+}¿/*-+.@"
    return random.choice(caracteres)

if __name__ == "__main__":
    main()
