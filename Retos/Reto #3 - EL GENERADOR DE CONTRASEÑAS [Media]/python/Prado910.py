# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
# - Longitud: Entre 8 y 16.
# - Con o sin letras mayúsculas.
# - Con o sin números.
# - Con o sin símbolos.
# (Pudiendo combinar todos estos parámetros entre ellos)

import random

def generarContraseña(longitud=8, mayusculas=False, numeros=False, simbolos=False):
    caracteres = list(range(97, 123))
    contraseña = ""
    
    if mayusculas:
        caracteres += list(range(65, 91))
    if numeros:
        caracteres += list(range(48, 58))
    if simbolos:
        caracteres = list(range(33, 127))
    
    for i in range(longitud):
        contraseña += chr(random.choice(caracteres))
    
    return contraseña

print(generarContraseña())
print(generarContraseña(mayusculas=True))
print(generarContraseña(numeros=True))
print(generarContraseña(longitud=15,  simbolos=True, mayusculas=True))
