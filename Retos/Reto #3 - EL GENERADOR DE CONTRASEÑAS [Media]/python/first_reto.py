### Reto 1 ##

from secrets import choice
from string import ascii_letters, ascii_uppercase, digits, punctuation

def GeneracionContraseña():
    caracteres = ascii_letters + ascii_uppercase + digits + punctuation
    longitud = 8 or 16
    contraseña= "".join(choice(caracteres) for caracter in range (longitud))
    return (f"Tu contraseña generada aleatoriamente es: {contraseña}")

print(GeneracionContraseña())
