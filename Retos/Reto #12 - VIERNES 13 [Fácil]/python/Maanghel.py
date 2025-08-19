"""
Crea una función que sea capaz de detectar si existe un viernes 13
en el mes y el año indicados.
- La función recibirá el mes y el año y retornará verdadero o falso.
"""

from datetime import date

def have_friday_13(year: int, month: int) -> bool:
    """Check if the 13th of a given month/year falls on a Friday.

    Args:
        year (int): Year to check.
        month (int): Month to check (1-12).

    Returns:
        bool: True if the 13th is Friday, False otherwise.

    Raises:
        TypeError: If arguments are not integers.
        ValueError: If month is not in 1-12.
    """
    if not isinstance(year, int) or not isinstance(month, int):
        raise TypeError("El año y el mes deben ser enteros.")
    if not 1 <= month <= 12:
        raise ValueError("El mes debe estar entre 1 y 12.")

    return date(year, month, 13).weekday() == 4


if __name__ == "__main__":
    print(have_friday_13(1900, 5)) # False
    print(have_friday_13(2023, 10)) # True
