"""
Crea una función que reciba un número decimal y lo trasforme a Octal
    y Hexadecimal.
- No está permitido usar funciones propias del lenguaje de programación que
    realicen esas operaciones directamente.
"""

def _validate_data(decimal: int) -> None:
    """
    Validate the input data for conversion.

    Ensures the value is a positive integer greater than zero.
    Raises an appropriate exception if the input is invalid.

    Args:
        decimal (int): The number to validate.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is zero or a negative integer.
    """
    if not isinstance(decimal, int):
        raise TypeError("Solo se admiten enteros positivos como datos.")
    if not decimal:
        raise ValueError("tiene que ingresar un valor positivo.")
    if decimal < 0:
        raise ValueError("Solo se admiten enteros positivos como datos.")

def _to_base(decimal: int, base: int) -> str:
    """
    Convert a decimal integer into a string representation in the specified base.

    This function uses successive integer division and remainders to transform
    a decimal number into another base (e.g., binary, octal, hexadecimal).
    It supports bases up to 16, using digits 0/9 and letters A/F for values >= 10.

    Args:
        decimal (int): The number in decimal format to be converted.
        base (int): The target base (e.g., 2 for binary, 8 for octal, 16 for hex).

    Returns:
        str: The string representation of the number in the target base.
    """
    symbols = "0123456789ABCDEF"
    digits = []

    if decimal == 0:
        return "0"

    while decimal > 0:
        remainder = decimal % base
        digits.append(symbols[remainder])
        decimal //= base

    return ''.join(reversed(digits))

def to_octal_and_hex(decimal: int) -> str:
    """
    Convert a decimal number into its Octal and Hexadecimal string representations.

    This function internally calls `to_base` with base 8 (Octal) and base 16 (Hexadecimal).
    It avoids using Python's built-in conversion functions such as `oct()` or `hex()`.

    Args:
        decimal (int): The number in decimal format to be converted.

    Returns:
        str: A descriptive message containing the decimal number and its octal
            and hexadecimal equivalents.
    """
    try:
        _validate_data(decimal)
    except (ValueError, TypeError) as e:
        return f"Error: {e}"

    octal = _to_base(decimal, 8)
    hexa = _to_base(decimal, 16)

    return f"El número {decimal} en octal es {octal} y en hexadecimal es {hexa}"


if __name__ == "__main__":
    print(to_octal_and_hex(1))
    print(to_octal_and_hex(255))
    print(to_octal_and_hex(-1))
