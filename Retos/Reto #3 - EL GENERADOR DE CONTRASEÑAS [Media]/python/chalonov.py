# Reto #3: Generador de contraseñas

import string
import random

def password_generator(size, letters, number, symbol):
    '''
    size = [8-16]
    letters = ["lower", "upper", "any"]
    number = [0,1]
    symbol = [True, False]
    '''
    if size >= 8 and size <= 16:
        if letters == "lower":
            alphabet = list(string.ascii_lowercase) 
        elif letters == "upper":
            alphabet = list(string.ascii_uppercase)
        elif letters == "any":
            alphabet = list(string.ascii_letters)
        
        if number == 0:
            numbers = list()
        elif number == 1:
            numbers = list(string.digits)

        if symbol == True:
            symbols = list(string.punctuation)
        elif symbol == False:
            symbols = list()
        
        password = ''.join(random.sample((alphabet + numbers + symbols), size))        

        print("Password: ", password)
    else:
        print("ERROR: Ingrese un tamaño de contraseña entre 8-16 caracteres")

password_generator(16, "lower", 1, True)   # Password:  ~?rf9&*6l0.t${b`
password_generator(8, "upper", 0, False)   # Password:  KVLAUXTS
password_generator(12, "lower", 0, True)   # Password:  phs?_%~+(<x"
password_generator(14, "upper", 1, False)  # Password:  R0YB8U2TDV5CIZ
password_generator(9, "any", 1, False)     # Password:  xATOriu05
password_generator(17, "upper", 1, False)  # ERROR: Ingrese un tamaño de contraseña entre 8-16 caracteres

