"""
Crea una función que reciba una expresión matemática (String)
    y compruebe si es correcta. Retornará true o false.
- Para que una expresión matemática sea correcta debe poseer
    un número, una operación y otro número separados por espacios.
Tantos números y operaciones como queramos.
- Números positivos, negativos, enteros o decimales.
- Operaciones soportadas: + - * / %

Ejemplos:
"5 + 6 / 7 - 4" -> true
"5 a 6" -> false
"""

def is_number(number: str) -> bool:
    """
    Verifica si la cadena es un numero.

    Args:
        number (str): Cadena que se validara como numero.

    Returns:
        bool: True si es un numero, False en caso contrario.
    """
    if number.count("+") + number.count("-") > 1:
        return False
    if number.startswith(("+", "-")):
        number = number[1:]
    if number.count(".") > 1:
        return False
    return number.replace(".", "").isdigit()

def is_mathematical_expression(expression: str) -> bool:
    """
    Verifica si una cadena representa una expresión matemática válida.

    Para que la expresión se considere correcta debe cumplir:
        - Estar compuesta por números y operadores separados por espacios.
        - Alternar correctamente entre número y operador.
        - Permitir números enteros, decimales, positivos y negativos.
        - Permitir los operadores: +, -, *, /, %
        - Tener al menos un patrón número-operador-número.
        - No terminar con un operador.

    Args:
        expression (str): Cadena que representa la expresión matemática a validar.

    Returns:
        bool: True si la expresión es válida, False en caso contrario.

    Raises:
        TypeError: Si el argumento proporcionado no es una cadena.
        ValueError: Si la cadena proporcionada está vacía o solo contiene espacios.
    """
    if not isinstance(expression, str):
        raise TypeError("Error. Solo se aceptan cadenas de texto como valor.")
    if not expression:
        raise ValueError("Error. La expresion no puede estar vacia")

    data = expression.strip().split()

    if len(data) < 3 or len(data) % 2 == 0:
        return False

    expecting_number = True
    for value in data:
        if expecting_number:
            if not is_number(value):
                return False
        else:
            if value not in ["+", "-", "*", "/", "%"]:
                return False
        expecting_number = not expecting_number

    return not expecting_number


if __name__ == "__main__":
    print(is_mathematical_expression("5 + 6 / 7 - 4"))
    print(is_mathematical_expression("5 a 6"))
    print(is_mathematical_expression("3 + 5"))
    print(is_mathematical_expression("3 a 5"))
    print(is_mathematical_expression("-3 + 5"))
    print(is_mathematical_expression("- 3 + 5"))
    print(is_mathematical_expression("-3 a 5"))
    print(is_mathematical_expression("-3+5"))
    print(is_mathematical_expression("3 + 5 - 1 / 4 % 8"))
