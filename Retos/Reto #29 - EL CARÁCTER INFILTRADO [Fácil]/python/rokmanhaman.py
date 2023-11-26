"""
Reto #29: EL CARÁCTER INFILTRADO
FÁCIL | Publicación: 17/07/23 | Resolución: 24/07/23
/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */
"""

def text_compare(text1, text2):

    lista = [text2[i] for i,j in enumerate(text2) if text1[i]!=text2[i]]


    return lista




#a = "Me llamo.Brais Moure"
a = "Me llamo mouredev"
#b = "Me llamo brais moure"
b = "Me llemo mouredov"

diff = text_compare(a,b)

print(diff)