"""
Crea una función que calcule el número de la columna de una hoja de Excel
    teniendo en cuenta su nombre.
- Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
- Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
"""

def column_number(row: str) -> int:
    """
    Convierte una etiqueta de columna de Excel a su número entero correspondiente.

    Excel asigna letras a las columnas de forma secuencial con un sistema numérico
    posicional en base 26, donde:
        A = 1, B = 2, ..., Z = 26,
        AA = 27, AB = 28, ..., AZ = 52,
        BA = 53, y así sucesivamente.

    Ejemplos:
        >>> column_number("A")
        1
        >>> column_number("Z")
        26
        >>> column_number("AA")
        27
        >>> column_number("CA")
        79

    args:
        row (str): Cadena formada únicamente por letras (A-Z o a-z) que representa
                    el nombre de la columna en Excel.

    returns:
        int: El número de columna correspondiente.

    raises:
        ValueError: Si la cadena está vacía.
        TypeError: Si la cadena contiene caracteres no alfabéticos.

    """
    if not row:
        raise ValueError("Error. El valor de entrada no puede estar vacio.")
    if not row.isalpha():
        raise TypeError("Error. Solo se aceptan letras del abecedario.")

    row = row.upper()
    result = 0

    for char in row:
        result = result * 26 + (ord(char) - ord('A') + 1)

    return result


if __name__ == "__main__":
    print(column_number("A"))
    print(column_number("Z"))
    print(column_number("AA"))
    print(column_number("CA"))
    print(column_number("XFD"))
    print(column_number("ZZZZ"))
