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

'''
Utilizaremos la codificación ASCII extendido:
La mayoria de los simbolos se encuentran entre: [33:47]+[58:64]+[91:96]
Los números: [48:57]
Las letras mayúsculas: [65:90]+[209](Ñ)
Las letras minúsculas: [97:122]+[241](ñ)
'''

import random



def generador_contraseñas(longitud =16, mayusculas = True, numeros = True, simbolos = True):
    password = str()
    list_caracteres = list()
    
    list_caracteres = list(range(97, 123))   # Las letras minuscuals en ASCII se encuentran entre 97 y 122. range nos crea una lista de [97,123)
    list_caracteres.append(241)             # Agregamos la ñ.

    if mayusculas:
        list_caracteres += list(range(65,91))   # Concatenamos a la lista, los valores numéricos de ASCII coresponientes a las mayúsculas. 
        list_caracteres.append(209)
    if numeros:
        list_caracteres += list(range(48,58))
    if simbolos:
        list_caracteres += list(range(33, 48))
        list_caracteres += list(range(58,65))
        list_caracteres += list(range(91, 96))
    
         # Escogemos un valor entero aletorio relacionado con las posiciones de la lista list_caracteres, es decir, de 0 a len(list_caracteres)
    for i in range(longitud):
        password += chr(list_caracteres[random.randint(0, len(list_caracteres))])

    return password


new_password = generador_contraseñas()
print(new_password)
letras_minusculas = generador_contraseñas(longitud=10, mayusculas=False, numeros=False, simbolos=False)
print(letras_minusculas)
mayusculas = generador_contraseñas(longitud=10, mayusculas=True, numeros=False, simbolos=False)
print(mayusculas)
con_numeros = generador_contraseñas(longitud=10, mayusculas=True, numeros=True, simbolos=False)
print(con_numeros)