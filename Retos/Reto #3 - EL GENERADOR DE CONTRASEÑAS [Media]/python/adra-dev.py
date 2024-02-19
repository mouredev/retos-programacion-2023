"""
Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
Podrás configurar generar contraseñas con los siguientes parámetros:
- Longitud: Entre 8 y 16.
- Con o sin letras mayúsculas.
- Con o sin números.
- Con o sin símbolos.
(Pudiendo combinar todos estos parámetros entre ellos)
"""

import random
import string

def password_gen(length=8, upper=False, digits=False, symbols=False):
    """ Using https://www.ascii-code.com """

    characters = list(range(97, 123))

    if upper:
        characters += list(range(65, 91))

    if digits:
        characters += list(range(48, 58)) 

    if symbols:
        characters += list(range(33, 48)) +\
            list(range(58, 65)) + list(range(91, 97))
        
    password=""

    final_length = 8 if length < 8 else 16 if length > 16 else length

    while len(password) < final_length:
        password += chr(random.choice(characters))

    return password


print(password_gen())
print(password_gen(length=16))
print(password_gen(length=1))
print(password_gen(length=22))
print(password_gen(length=12, upper=True))
print(password_gen(length=12, upper=True, digits=True))
print(password_gen(length=12, upper=True, digits=True, symbols=True))
print(password_gen(length=12, upper=True, symbols=True))