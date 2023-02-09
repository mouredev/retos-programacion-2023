import random
import string

# DEfinimos una funcion para establecer que caracteres deseamos en la contraseña

def longPassword():
    """Obtiene el numero de digitos de la contraseña"""
    long_password = int(input("Que longitud desea para la contraseña (8-16 caracteres): "))

    if long_password >= 8 and long_password <=16:
        return long_password
    else: 
        print("Solo son permitidas contraseñas entre 8 y 9 caracteres.")
        return int(longPassword())

def upperLower():
    """Verifica si la contraseña debe tener mayusculas"""
    upper_lower = input("Desea incluir mayusculas? (Y/N) ")
    if upper_lower == "y" or upper_lower == "Y":
        return True
    elif upper_lower == "n" or upper_lower == "N":
        return False
    else:
        print("Por favor, seleccione una opccion")
        return upperLower()

def numInclude():
    """Verifica si la contraseña debe tener numeros"""
    num_inc = input("Desea incluir numeros? (Y/N) ")
    if num_inc == "y" or num_inc == "Y":
        return True
    elif num_inc == "n" or num_inc == "N":
        return False
    else:
        print("Por favor, seleccione una opccion")
        return numInclude()

def simbInclude():
    """Verifica si la contraseña debe tener simbolos"""
    simb_inc = input("Desea incluir simbolos? (Y/N) ")
    if simb_inc == "y" or simb_inc == "Y":
        return True
    elif simb_inc == "n" or simb_inc == "N":
        return False
    else:
        print("Por favor, seleccione una opccion")
        return simbInclude()


def passwordGen(longitud, numeros, mayusculas, simbolos):
    """Genera una contraseña"""

    passwordChar = ""
    password = ""

    # Añade numeros
    if numeros:
        passwordChar += random.choice(string.digits)

    # Añade mayusculas
    if mayusculas:
        passwordChar +=  random.choice(string.ascii_uppercase)

    # Añade simbolos
    if simbolos:
        passwordChar += random.choice(string.punctuation)

    # Termina de completar la contraseña
    while len(passwordChar) < longitud:
        passwordChar += random.choice(string.ascii_lowercase)

    # Pone de manera aleatoria los caracteres añadidos
    for _ in range(longitud):
        password += " ".join(random.choice(passwordChar))   

    print("Su nueva contraseña es: " + password)


longitud = longPassword()
numeros = numInclude()
mayusculas = upperLower()
simbolos = simbInclude()

passwordGen(longitud, numeros, mayusculas, simbolos)
