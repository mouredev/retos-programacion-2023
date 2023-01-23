""""
  Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
  Podrás configurar generar contraseñas con los siguientes parámetros:
  - Longitud: Entre 8 y 16.
  - Con o sin letras mayúsculas.
  - Con o sin números.
  - Con o sin símbolos.
  (Pudiendo combinar todos estos parámetros entre ellos)
"""

import string
import random
from string import punctuation


def generate_password(size: int, has_uppercases: bool, has_numbers: bool, has_symbols: bool) -> str:
    characters: list = []
    password: str = ""

    characters.append(list(string.ascii_letters)) if has_uppercases else characters.append(list(string.ascii_lowercase))

    if has_numbers:
        characters.append(list(range(0, 10)))

    if has_symbols:
        characters.append(list(punctuation))

    for _ in range(size):
        i: int = random.randint(0, len(characters)-1)
        j: int = random.randint(0, len(characters[i])-1)
        password += (str(characters[i][j]))

    return password


if __name__ == "__main__":
    length: int = 10
    include_uppercases: bool = True
    include_numbers: bool = True
    include_symbols: bool = True

    password_generated: str = generate_password(length, include_uppercases, include_numbers, include_symbols)

    print(f"Your new password: \n{password_generated}")
