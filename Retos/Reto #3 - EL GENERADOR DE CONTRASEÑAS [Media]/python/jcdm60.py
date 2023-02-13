#
# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
# - Longitud: Entre 8 y 16.
# - Con o sin letras mayúsculas.
# - Con o sin números.
# - Con o sin símbolos.
# (Pudiendo combinar todos estos parámetros entre ellos)
#

import random
from string import ascii_letters, digits, punctuation


def password(length, lower=False, upper=False, digit=False, symbol=False):
    characters = ""
    if lower:
        characters += ascii_letters[:26]
    if upper:
        characters += ascii_letters[26:]
    if digit:
        characters += digits
    if symbol:
        characters += punctuation
    if not 8 <= length <= 16:
        return "La longitud tiene que ser entre 8 y 16 caracteres"

    password = []

    while len(password) < length:
        if lower:
            password.append(random.choice(ascii_letters[:26]))
        if upper:
            password.append(random.choice(ascii_letters[26:]))
        if digit:
            password.append(random.choice(digits))
        if symbol:
            password.append(random.choice(punctuation))
        if not any([lower, upper, digit, symbol]):
            password.append(random.choice(characters))

    random.shuffle(password)
    return "".join(password)


if __name__ == "__main__":
    print(password(8, True, True, True))