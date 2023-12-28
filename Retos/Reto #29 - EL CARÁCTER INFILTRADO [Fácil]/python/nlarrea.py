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


def infiltrated_characters(text_one:str, text_two:str) -> list:
    """ Function that receives two texts of the same length and returns the 
     different characters of the second one. """
    
    if len(text_one) != len(text_two):
        print("Both texts must be equal in length!")
        return []

    infiltrated_chars = [char for index, char in enumerate(text_two)
                         if char != text_one[index]]

    if len(infiltrated_chars) == 0:
        print("Both texts are the same!")

    return infiltrated_chars


print(infiltrated_characters("Me llamo mouredev", "Me llemo mouredov"))           # ['e', 'o']
print(infiltrated_characters("Me llamo.Brais Moure", "Me llamo brais moure"))     # [' ', 'b', 'm']
print(infiltrated_characters("Me llamoBrais Moure", "Me llamo brais moure"))      # [] -> prints: Both texts must be equal in length!
print(infiltrated_characters("Me llamo Brais Moure", "Me llamo Brais Moure"))     # [] -> prints: Both texts are the same!