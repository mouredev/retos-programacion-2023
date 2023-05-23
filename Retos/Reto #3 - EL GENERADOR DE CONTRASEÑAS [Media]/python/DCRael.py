from random import *

def generador_contraseña():
    
    #caracteres usados
    numbers = '1234567890'
    alphabet = 'abcdefghijklmnopqrsuvtñwzx'
    symbols = '@#$_&-+/*!?%<>¿¡'
    #longitud y contraseña
    longitud = randint(8,16)
    contraseña = ''

    #generador de contraseña
    for i in range(longitud):
        contraseña += choice(numbers + alphabet + alphabet.upper() + symbols)
    return contraseña

print(generador_contraseña())