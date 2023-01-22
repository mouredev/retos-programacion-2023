'''
 Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 Podrás configurar generar contraseñas con los siguientes parámetros:
 - Longitud: Entre 8 y 16.
 - Con o sin letras mayúsculas.
 - Con o sin números.
 - Con o sin símbolos.
 (Pudiendo combinar todos estos parámetros entre ellos)
'''

import string
import secrets

def generate_password(length = 8, case = True, number = True, symbol = True):
    password: str = ""
    options: int = 0
    
    if length < 8 or length > 16:
        print("La contraseña debe contener entre 8 y 16 caracteres")
    else:
        # Control de las opciones que se ejecutarán
        options += 1 if case else 0
        options += 1 if number else 0
        options += 1 if symbol else 0
        
        # En función del valor de las opciones se creará una password con mayúsculas, números o símbolos
        if options == 0:
            letter = string.ascii_letters.lower()
            
        if options == 1:
            letter = string.ascii_letters
            
        if options == 2:
            letter = string.ascii_letters +  string.digits
            
        if options == 3:
            letter = string.ascii_letters +  string.digits + string.punctuation
            
        # Generar contraseña
        password = ''.join(secrets.choice(letter) for i in range(length))
            
    return password

if __name__ == '__main__':

    print('Se generan los siguientes juegos de contraseñas con distintas configuraciones:\n')
    print(generate_password(16, True, True, True))
    print(generate_password(8, False, False, False))
    print(generate_password(10, False, False, False))
    print(generate_password(9, True, False, False))
    print(generate_password(20, True, True, True))
    print(generate_password())