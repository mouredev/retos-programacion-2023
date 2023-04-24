# /*
#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
#  */


# Función para generar contraseñas
# Parámetros:
# - length: Longitud de la contraseña (entre 8 y 16)
# - upper: Booleano para indicar si se incluyen mayúsculas
# - numbers: Booleano para indicar si se incluyen números
# - symbols: Booleano para indicar si se incluyen símbolos

def generate_password(length, upper, numbers, symbols):
    import random
    import string

    if length < 8 or length > 16:
        return "La longitud debe estar entre 8 y 16"

    chars = string.ascii_lowercase
    if upper:
        chars += string.ascii_uppercase
    if numbers:
        chars += string.digits
    if symbols:
        chars += string.punctuation

    return "".join(random.choice(chars) for _ in range(length))


# Casos de prueba

print(generate_password(8, True, True, True))
print(generate_password(16, True, True, False))
print(generate_password(20, False, True, False))
print(generate_password(8, False, True, False))