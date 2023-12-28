'Reto #3: EL GENERADOR DE CONTRASEÑAS'
'''
Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
Podrás configurar generar contraseñas con los siguientes parámetros:

- Longitud: Entre 8 y 16.
- Con o sin letras mayúsculas.
- Con o sin números.
- Con o sin símbolos.
(Pudiendo combinar todos estos parámetros entre ellos)
'''
import random

def generate_password():
    
    numbers = '1234567890'
    alphabet = 'abcdefghijklmnopqrsuvtñwzx'
    symbols = '@#$_&-+/*!?%<>¿¡'
    
    password = ''
    
    i=0
    while i <= random.randrange(8, 17):
        password += random.choice(numbers + alphabet + alphabet.upper() + symbols)
        i += 1
    
    return password

print(generate_password())