from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice


def generate_password(length=16, uppers=False, numbers=False, symbols=False):
    enabled_symbols = ascii_lowercase
    password = ""
    
    if not length in range(8, 17):
        return "[Error] longitud no valida"

    if uppers:
        enabled_symbols += ascii_uppercase

    if numbers:
        enabled_symbols += digits

    if symbols:
        enabled_symbols += punctuation

    while True:
        password = ""
        is_valid = True

        for _ in range(length):
            password += choice(enabled_symbols)

        if not any(symbol.islower() for symbol in password):
            is_valid = False

        if uppers:
            if not any(symbol.isupper() for symbol in password):
                is_valid = False

        if numbers:
            if not any(symbol.isdigit() for symbol in password):
                is_valid = False

        if symbols:
            if not any(symbol in password for symbol in punctuation):
                is_valid = False

        if is_valid:
            break
        
    return password


print(generate_password(12, True, True, True))
