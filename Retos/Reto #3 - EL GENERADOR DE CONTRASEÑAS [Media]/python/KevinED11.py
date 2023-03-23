from string import ascii_lowercase, ascii_uppercase, punctuation, digits
from random import choice

# por defecto genera una contraseña con una longitud de 10 caracteres y con todos los parámetros


def pass_gen(length: int = 10, all_params: bool = True, upper: bool = False, lower: bool = False,  numbers: bool = False, simbols: bool = False) -> str:

    characters = ""

    char_all = ascii_lowercase + ascii_uppercase + punctuation + digits

    if length not in list(range(8, 17)):
        return 'porfavor vuelve a intentarlo, debes colocar un rango entre 8 y 16 caracteres.'

    if all_params:
        characters += char_all
    elif upper:
        characters += ascii_uppercase
    elif numbers:
        characters += digits
    elif simbols:
        characters += punctuation

    contraseña = "".join(choice(characters) for i in range(length))

    return f'su nueva contraseña generada es: {contraseña}'


print(pass_gen())
