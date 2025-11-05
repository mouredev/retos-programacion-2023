"""
Los primeros dispositivos móviles tenían un teclado llamado T9
    con el que se podía escribir texto utilizando únicamente su
    teclado numérico (del 0 al 9).

Crea una función que transforme las pulsaciones del T9 a su
    representación con letras.
- Debes buscar cuál era su correspondencia original
- Cada bloque de pulsaciones va separado por un guión.
- Si un bloque tiene más de un número, debe ser siempre el mismo.
- Ejemplo:
    Entrada: 6-666-88-777-33-3-33-888
    Salida: MOUREDEV
"""

def keyboard_t9(code: str) -> str:
    """
    Decodifica una secuencia de pulsaciones del teclado T9 y devuelve
    su representación en texto.


    Reglas:
      * Cada bloque representa una letra.
      * Si un bloque tiene más de un dígito, todos deben ser iguales.
      * El dígito "0" representa un espacio.
      * La cantidad de repeticiones determina la letra seleccionada.

    Ejemplo:
        >>> keyboard_t9("6-666-88-777-33-3-33-888")
        'MOUREDEV'

    Args:
        code (str): Cadena con las pulsaciones separadas por guiones.

    Returns:
        str: Texto decodificado utilizando la correspondencia T9.

    Raises:
        TypeError: Si `code` no es una cadena de texto.
        ValueError: Si la cadena está vacía o algún bloque contiene
            más de un número diferente.
    """

    alphabet = {
        "2": ["A", "B", "C"],
        "3": ["D", "E", "F"],
        "4": ["G", "H", "I"],
        "5": ["J", "K", "L"],
        "6": ["M", "N", "O"],
        "7": ["P", "Q", "R", "S"],
        "8": ["T", "U", "V"],
        "9": ["W", "X", "Y", "Z"],
        "0": " "
    }

    if not isinstance(code, str):
        raise TypeError("Error. Ingrese los digitos separados por guiones.")
    if not code:
        raise ValueError("Error. Intentelo nuevamente.")

    pulsations = code.strip().split("-")
    if any( len(set(element)) > 1 for element in pulsations):
        raise ValueError("Error. Si son varias pulsaciones, solo pueden ser del mismo numero.")

    sentence = ""
    for element in pulsations:
        sentence += alphabet[element[0]][len(element) - 1]

    return sentence

if __name__ == "__main__":
    print(keyboard_t9("6-666-88-777-33-3-33-888"))
    print(keyboard_t9("44-666-555-2"))
    print(keyboard_t9("6-88-66-3-666"))
    print(keyboard_t9("44-666-555-2-0-6-88-66-3-666"))
