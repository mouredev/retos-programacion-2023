import random
import string


def generar_clave(longitud=8, mayusculas=False, numeros=False, especiales=False):

    if longitud < 8 or longitud > 16:
        return "El numero de caracteres esta fuera del rango"

    caracteres = string.ascii_lowercase

    if mayusculas:
        caracteres += string.ascii_uppercase

    if numeros:
        caracteres += string.digits

    if especiales:
        caracteres += string.punctuation

    return "".join(random.choice(caracteres) for i in range(longitud))


print(generar_clave(8, False, True, True))
print(generar_clave(15, True, True, True))
print(generar_clave(10, False, False, True))
print(generar_clave(3, False, True, True))
print(generar_clave(28, False, True, True))
