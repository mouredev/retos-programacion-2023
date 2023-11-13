"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""
import random

def password_generator(length=8, capital = False, numbers = False, symbols = False): #Establecemos los valores predeterminados de los parametros
    
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers_ = "0123456789"
    symbols_ = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
    password = ""
    password_chars = []
    correct_length = 8
    
    if length < 8:
        correct_length = 8
    elif length > 16:
        correct_length = 16
    else:
        correct_length = length

    if capital:
        letters = letters.upper()
        password_chars += letters
    else:
        password_chars += letters
        
    if numbers:
        password_chars += numbers_
        
    if symbols:
        password_chars += symbols_
    
    password = "".join(random.choices(password_chars, k=correct_length))
            
    return password      
    
print(password_generator(length = 12, capital = True, numbers = True, symbols = True))
