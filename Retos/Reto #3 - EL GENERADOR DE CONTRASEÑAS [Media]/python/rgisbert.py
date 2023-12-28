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


def create_password(length=10, upper=True, numbers=True, symbols=False):
    # Range allowed for password
    pass_range = {
        'MAX': 16,
        'MIN': 8,
    }

    # Character options
    opt_lower = "abcdefghijklmnopqrstuvwxyz"
    opt_number = "0123456789"
    opt_symbol = "~!@#$%^&*()_-+={[}]|:;<,>.?/"
    opt_upper = opt_lower.upper()

    # Set the right password length
    pass_length = length if pass_range['MIN'] <= length <= pass_range['MAX'] \
        else (pass_range['MIN'] if length < pass_range['MIN'] else pass_range['MAX'])

    # Options for final password
    valid_options = opt_lower + \
        (opt_number if numbers else "") + \
        (opt_symbol if symbols else "") + \
        (opt_upper if upper else "")

    # Discount 1 because randint takes the max value + 1 and could overflow the index
    length_opt = len(valid_options) - 1
    return "".join([valid_options[random.randint(0, length_opt)] for i in range(pass_length)])


if __name__ == "__main__":
    print(create_password(22))
    print(create_password(14))
    print(create_password(8, numbers=False, symbols=False))
    print(create_password(numbers=False, symbols=True))
