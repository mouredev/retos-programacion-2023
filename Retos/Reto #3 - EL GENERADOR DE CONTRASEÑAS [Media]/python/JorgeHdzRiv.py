"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""

import string
import secrets

def generate():
    password = ''
    pwd_length = int(input('Digitos en su password entre 8 a 16: '))
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    
    alphabet = letters+digits+special_chars
    
    while pwd_length < 8 or pwd_length > 16:
        print('Longitud demasiado corta o larga')
        pwd_length = int(input('Digitos en su password entre 8 a 16: '))
        print()
    
    
    for i in range(pwd_length):
        password += ''.join(secrets.choice(alphabet))
    print('\nSu password generada es: ',password)
    
    
            
generate()
