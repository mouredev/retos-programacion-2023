"""
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
"""

import numpy as np

lista = ["a", "b", "c", 
         "d", "e", "f", 
         "g", "h", "i", 
         "j", "k", "l", 
         "m", "n", "o", 
         "p", "q", "r", 
         "s", "t", "u", 
         "v", "w", "x", 
         "y", "z", 
         "A", "B", "C", 
         "D", "E", "F", 
         "G", "H", "I", 
         "J", "K", "L", 
         "M", "N", "O", 
         "P", "Q", "R", 
         "S", "T", "U", 
         "V", "W", "X", 
         "Y", "Z",
         1, 2, 3, 
         4, 5, 6, 
         7, 8, 9, 
         0,
         "!", "$", "%", 
         "&", "/", "(", 
         ")", "=", "?", 
         "¿", "<", ">", 
         "Ç"]


def montar_clave():
    numero = np.random.randint(1, 75)
    return numero

longitud = int(input("Longitud de la clave: "))
contrasenya = ""


while len(contrasenya) <= (longitud-1):
    letra = str(lista[montar_clave()])
    contrasenya += letra
    
print(contrasenya)
