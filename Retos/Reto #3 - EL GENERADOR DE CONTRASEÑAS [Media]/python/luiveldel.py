# Created by luiveldel

# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
# - Longitud: Entre 8 y 16.
# - Con o sin letras mayúsculas.
# - Con o sin números.
# - Con o sin símbolos.
# (Pudiendo combinar todos estos parámetros entre ellos)

import random # generate random numbers
import string # provide a set of characters to choose

password_lengh: int = random.randint(8, 17)
characters: str = string.ascii_letters + string.digits + string.punctuation

password: str = "".join(random.choice(characters) for i in range(password_lengh))

print(password)