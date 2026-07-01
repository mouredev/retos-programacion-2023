"""```
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
```"""
import random
import string

def password_generate():
    password = []
    longitud = random.randrange(8, 16)

    for i in range(longitud):
        caracter = random.choice(string.ascii_letters)
        simbolos = "!@#$%^&*()_+-=[]{}|;:•🙊,.<>?~€¥"
        simbolos_aleatorio = random.choice(simbolos)
        numeros = str(random.randint(0,9))

        valor = random.choice([caracter, simbolos_aleatorio, numeros])
        password.append(valor)

    resultado = "".join(password)
    return resultado

print(password_generate())
        


