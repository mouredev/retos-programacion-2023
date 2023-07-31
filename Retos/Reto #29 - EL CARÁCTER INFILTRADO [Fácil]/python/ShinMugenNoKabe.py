# Crea una función que reciba dos cadenas de texto casi iguales,
# a excepción de uno o varios caracteres. 
# La función debe encontrarlos y retornarlos en formato lista/array.
# - Ambas cadenas de texto deben ser iguales en longitud.
# - Las cadenas de texto son iguales elemento a elemento.
# - No se pueden utilizar operaciones propias del lenguaje
#   que lo resuelvan directamente.
# 
# Ejemplos:
# - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
# - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]

def find_differences(text1: str, text2: str) -> list[str]:
    if text1 is None or text2 is None:
        raise ValueError("Introduce un texto válido")
    elif len(text1) != len(text2):
        raise ValueError("Las cadenas de texto deben tener el mismo número de carácteres")
    
    return [char2 for char1, char2 in zip(text1, text2) if char1 != char2]


if __name__ == "__main__":
    diff1 = find_differences("Me llamo mouredev", "Me llemo mouredov")
    assert diff1 == ["e", "o"]
    print(diff1)

    diff2 = find_differences("Me llamo.Brais Moure", "Me llamo brais moure")
    assert diff2 == [" ", "b", "m"]
    print(diff2)

    text1 = input("Introduce la primera cadena de carácteres: ")
    text2 = input("Introduce la segunda cadena de carácteres: ")
    print(find_differences(text1, text2))