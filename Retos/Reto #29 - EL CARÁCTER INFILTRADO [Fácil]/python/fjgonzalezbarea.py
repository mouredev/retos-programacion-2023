"""
 Crea una función que reciba dos cadenas de texto casi iguales, a excepción de uno o varios caracteres.
 La función debe encontrarlos y retornarlos en formato lista/array.
 - Ambas cadenas de texto deben ser iguales en longitud.
 - Las cadenas de texto son iguales elemento a elemento.
 - No se pueden utilizar operaciones propias del lenguaje
   que lo resuelvan directamente.

 Ejemplos:
 - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]

 Ejecutar tests:
 python -m fjgonzalezbarea "test"

 Ejecutar función con argumentos
 python -m fjgonzalezbarea "Me llamo mouredev" "Me llemo mouredov"
"""
import sys


def find_differences(str1, str2):
    return [str2[index] for index in range(len(str1)) if str1[index] != str2[index]]


def main(str1, str2):
    if len(str1) != len(str2):
        raise ValueError(f"Strings must have same length, however first string length is {len(str1)} and second string length is {len(str2)}")

    differences_list = find_differences(str1, str2)
    print(f"The list of different characters is: {differences_list}")

# Better in a separate file, but to accomplish rules for Pull Request :-)
def test_find_difference():
    str1 = "Me llamo mouredev"
    str2 = "Me llemo mouredov"
    difference = find_differences(str1, str2)
    assert difference == ["e", "o"]

    str3 = "Me llamo.Brais Moure"
    str4 = "Me llamo brais moure"
    difference_2 = find_differences(str3, str4)
    assert difference_2 == [" ", "b", "m"]
    print("Tests successfully executed!")


if __name__ == "__main__":
    if sys.argv[1] == "test":
        test_find_difference()
    elif len(sys.argv[1:]) == 2:
        main(sys.argv[1], sys.argv[2])
    else:
        raise ValueError("Unexpected arguments.")
