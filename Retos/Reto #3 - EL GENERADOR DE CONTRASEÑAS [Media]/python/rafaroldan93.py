import string
import random

def loop(condition, text):
    value = 0
    while value not in condition:
        value = input(text)
        try:
            value = int(value)
        except:
            pass
    return value

print("Generador de contraseñas:")
lenght = loop(range(8, 17), "Introduce la longitud (entre 8 y 16 caracteres): ")
upper = loop(["s", "n"], "¿Deseas incluir letras mayúsculas? [s/n]: ")
numbers = loop(["s", "n"], "¿Deseas incluir números? [s/n]: ")
simbols = loop(["s", "n"], "¿Deseas incluir símbolos? [s/n]: ")

characters = string.ascii_lowercase
if upper == "s": characters += string.ascii_uppercase
if numbers == "s": characters += string.digits
if simbols == "s": characters += string.punctuation

password = ""
for _ in range(lenght):
    password += random.choice(characters)

print("Contraseña generada:", password)