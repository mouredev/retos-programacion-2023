"""
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
 """


def infiltrated_character(string_1, string_2):
    different_characters = []
    if len(string_1) != len(string_2):
        return "Las cadenas de texto no son del mismo tamaño"
    else:
        for i in range(len(string_1)):
            character_1 = string_1[i]
            character_2 = string_2[i]
            if character_1 == character_2:
                continue
            else:
                different_characters.append(character_2)
    return different_characters

print(infiltrated_character("Me llamo.Brais Moure", "Me llamo brais moure"))

 