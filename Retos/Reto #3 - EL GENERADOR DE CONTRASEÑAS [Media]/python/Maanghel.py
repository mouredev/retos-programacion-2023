"""
Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
Podrás configurar generar contraseñas con los siguientes parámetros:
- Longitud: Entre 8 y 16.
- Con o sin letras mayúsculas.
- Con o sin números.
- Con o sin símbolos.
(Pudiendo combinar todos estos parámetros entre ellos)
"""

import secrets
import string

def validate_data(length: int) -> None:
    """
    Validates the password length.

    Args:
        length (int): Desired password length.

    Raises:
        TypeError: If length is not an integer.
        ValueError: If length is not between 8 and 16.
    """
    if not isinstance(length, int):
        raise TypeError("Solo se aceptan enteros para definir la longitud.")
    if length < 8 or length > 16:
        raise ValueError("La contraseña debe tener un minimo de 8 caracteres y un maximo de 16.")

def password_generator(length: int, *, upper: bool=False, numbers: bool=False, symbols: bool=False) -> str:
    """
    Generates a secure random password based on user preferences.

    Args:
        length (int): Length of the password (8-16).
        upper (bool): Include uppercase letters.
        numbers (bool): Include digits.
        symbols (bool): Include special characters.

    Returns:
        str: Securely generated password.
    """
    validate_data(length)
    character_pools = [string.ascii_lowercase]
    if upper:
        character_pools.append(string.ascii_uppercase)
    if numbers:
        character_pools.append(string.digits)
    if symbols:
        character_pools.append(string.punctuation)

    all_characters = "".join(character_pools)
    password_chars = [secrets.choice(pool) for pool in character_pools]

    while len(password_chars) < length:
        password_chars.append(secrets.choice(all_characters))

    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


if __name__ == "__main__":
    print(password_generator(9, upper=True, numbers=True, symbols=True))
