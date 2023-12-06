import random

__letters_lower = "abcdefghijklmnopqrstuvwxyz"
__letters_upper = "ABCDEFGHYJKLMNOPQRSTUVWXYZ"
__numbers = "1234567890"
__symbols = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

def PasswordGenerator(length: int, uppercase: bool = False, numbers: bool = False, symbols: bool = False) -> str:
    if not isinstance(length, int):
        return "La longitud tiene que ser de tipo int."

    if length < 8:
        return "La longitud no puede ser inferior a 8"

    if length > 16:
        return "La longitud no puede ser mayor de 16"

    if not isinstance(uppercase, bool) or not isinstance(numbers, bool) or not isinstance(symbols, bool):
        return "Error en el tipo de datos introducido, parámetros 2, 3 ó 4."

    characters = __letters_lower

    if uppercase:
        characters += __letters_upper

    if numbers:
        characters += __numbers

    if symbols:
        characters += __symbols

    password = ""

    while len(password) < length:
        password += characters[random.randint(0, len(characters) - 1)]

    return password

print(PasswordGenerator(5, False, False, False))
print(PasswordGenerator("5", False, False, False))
print(PasswordGenerator(18, False, False, False))
print(PasswordGenerator(15, "False", False, False))
print(PasswordGenerator(15, True, False, False))
print(PasswordGenerator(9, True, True, True))

password_length = int(input("Longitud de la contraseña:"))
password_upper = bool(input("¿Contraseña con letras mayúsculas? (True/False):"))
password_numbers = bool(input("¿Contraseña con números? (True/False):"))
password_symbols = bool(input("¿Contraseña con símbolos? (True/False):"))

print(PasswordGenerator(password_length, password_upper, password_numbers, password_symbols))