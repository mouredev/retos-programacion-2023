"""
Crea una función que reciba dos cadenas de texto casi iguales,
    a excepción de uno o varios caracteres.
La función debe encontrarlos y retornarlos en formato lista/array.
- Ambas cadenas de texto deben ser iguales en longitud.
- Las cadenas de texto son iguales elemento a elemento.
- No se pueden utilizar operaciones propias del lenguaje
    que lo resuelvan directamente.

Ejemplos:
- Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
- Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
"""

def different_characters(text1: str, text2: str) -> list[str]:
    """
    Compara dos cadenas de texto con la misma longitud y retorna
    una lista con los caracteres que son distintos entre ambas.

    La comparación se realiza carácter a carácter y solo se guardan
    los caracteres diferentes que aparecen en la segunda cadena.

    Args:
        text1 (str): Primera cadena de texto a comparar.
        text2 (str): Segunda cadena de texto a comparar.

    Returns:
        list[str]: Lista con los caracteres distintos encontrados.

    Raises:
        TypeError: Si alguno de los argumentos no es una cadena.
        ValueError: Si las cadenas tienen longitudes diferentes o están vacías.
    """
    if not isinstance(text1, str) or not isinstance(text2, str):
        raise TypeError("Error. Se aceptan solo cadenas de texto como valores.")
    if len(text1) != len(text2):
        raise ValueError("Error. Las cadenas deben tener la misma cantidad de elementos.")
    if not text1 or not text2:
        raise ValueError("Error. Los textos no pueden estar vacios.")

    differences = []
    for char1, char2 in zip(text1, text2):
        if char1 != char2:
            differences.append(char2)

    return differences


if __name__ == "__main__":
    print(different_characters("Me llamo mouredev", "Me llemo mouredov"))
    print(different_characters("Me llamo.Brais Moure", "Me llamo brais moure"))
