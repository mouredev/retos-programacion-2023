from random import choice
from string import ascii_letters
from string import ascii_lowercase
from string import digits
from string import punctuation

def set_values():
    print("Indique la cantidad de caracteres (debe estar entre 8 y 16):")
    length = int(input())
    print("¿Desea que su contraseña incluya mayúsculas?\n[1]Sí\n[0]No\n")
    mayus = int(input())
    print("¿Desea que su contraseña incluya números?\n[1]Sí\n[0]No\n")
    numbers = int(input())
    print("¿Desea que su contraseña incluya símbolos?\n[1]Sí\n[0]No\n")
    symbols = int(input())
    print("\n")
    values = [length, mayus, numbers, symbols]
    return values

def gen_password(length: int, mayus: bool = True, numbers: bool = True, symbols: bool = True):
    
    if length < 8 or length > 16:
        print("La contraseña debe ser de 8 a 16 caracteres\n")
        values = set_values()
        gen_password(values[0], values[1], values[2], values[3])
    
    password = ""
    letters = ascii_letters
    minus_letters = ascii_lowercase
    num = digits
    sym = punctuation

    if mayus == True:
        generator = letters  
    else:
        generator = minus_letters

    if numbers == True:
        generator = generator + num
    
    if symbols == True:
        generator = generator + sym
    
    for i in range(length):
            password = password + choice(generator)
    print("Su contraseña es: [ " + password + " ]")
    return password

values = set_values()
gen_password(values[0], values[1], values[2], values[3])
