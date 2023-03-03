# Reto #3: EL GENERADOR DE CONTRASEÑAS
#### Dificultad: Media | Publicación: 16/01/23 | Corrección: 23/01/23

## Enunciado

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

longitud = 9
mayusculas = True
numeros = False
simbolos = True
simbolosPermitidos = [34,35,36,37,38,39,40,41,42,43,44,45,46,47,
                      57,58,59,60,61,62,63,64,91,92,93,93,95,96,123,
                      124,125,126]

def genLetra(conMayuscula):
    numeroASCII = 0
    if conMayuscula:
        return random.randint(65, 90) #ASCII Mayusculas
    else:
        return random.randint(97, 122) #ASCII Minuscula
    return 

def genNum():
    return  random.randint(48, 57) #ASCII Mayusculas

def genSimbolo():
    selector =  random.randint(0, len(simbolosPermitidos)) #ASCII Mayusculas
    return chr(simbolosPermitidos[selector])

condiciones = mayusculas + numeros + simbolos

if longitud > 7 and longitud < 17:
    passGenerada = ""
    control = 0
    while control < longitud:
        seleccion = random.randint(0, 4)
        if seleccion == 0:
            passGenerada = passGenerada + chr(genLetra(False))
            control += 1
        elif seleccion == 1 and mayusculas:
            passGenerada = passGenerada + chr(genLetra(True))
            control += 1
        elif seleccion == 2 and numeros:
            passGenerada = passGenerada + str(genNum())
            control += 1
        elif seleccion == 3 and simbolos:
            passGenerada = passGenerada + genSimbolo()
            control += 1
        #seleccionar de manera aleatoria una de las funciones

print(passGenerada)




