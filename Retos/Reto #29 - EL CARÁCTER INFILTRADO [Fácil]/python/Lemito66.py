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

def find_difference(string_one: str , string_two: str) -> list:
    difference = []
    if len(string_one) != len(string_two):
        return "Ambas cadenas de texto deben ser iguales en longitud."
    
    for word in range(len(string_one)):
        if string_one[word] != string_two[word]:
            difference.append(string_two[word])
    return difference

print(find_difference("Me llamo mouredev", "Me llemo mouredov"))
print(find_difference("Me llamo.Brais Moure", "Me llamo brais moure"))

print(find_difference('abc', 'abc'))
print(find_difference('abc', 'abcd'))
print(find_difference('a!b@c#', 'a!b@d#'))