"""
Crea una función que reciba dos cadenas de texto casi iguales,
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
"""


def search_infiltred(cadena_1=str, cadena_2=str):
    """Funcion para buscar el caracter infiltrado"""
    original = list(cadena_1)
    verificar = list(cadena_2)
    infiltrados = list()

    if len(original) == len(verificar):
        for i in range(1, len(original)):
            if original[i] != verificar[i]:
                infiltrados += verificar[i]
        return infiltrados
    else:
        return "La longitud entre ambas no es la misma!"


print(search_infiltred("Me llamo mouredev", "Me llemo mouredov"))
print(search_infiltred("Me llamo.Brais Moure", "Me llamo brais moure"))
print(search_infiltred("Juan", "Juan del Pueblo"))
