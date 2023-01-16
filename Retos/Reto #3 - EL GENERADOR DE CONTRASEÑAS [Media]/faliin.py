
 #  Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 #  Podrás configurar generar contraseñas con los siguientes parámetros:
 #  Longitud: Entre 8 y 16.
 #  Con o sin letras mayúsculas.
 #  Con o sin números.
 #  Con o sin símbolos.
 # (Pudiendo combinar todos estos parámetros entre ellos)
 


import random
import string

def generate_password(length=8, use_upper=True, use_numbers=True, use_symbols=True):
    char_set = ""
    if use_upper:
        char_set += string.ascii_uppercase
    if use_numbers:
        char_set += string.digits
    if use_symbols:
        char_set += string.punctuation

    return ''.join(random.sample(char_set, length))

# Usage example
print(generate_password(length=12, use_upper=True, use_numbers=True, use_symbols=True))
