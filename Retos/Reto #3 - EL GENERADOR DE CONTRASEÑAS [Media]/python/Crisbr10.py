'''*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 *'''
 
from random import *
from sys import stdout as st

st.reconfigure(encoding ='utf-8')

upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", "\"", "<", ">", ",", ".", "?", "/", "|", "\\", "`", "~"]

pass_long = int(input('Indique la longitud de su contraseña (8-16)\n:'))
if 8 > pass_long > 16:
    print('Longitud incorrecta debe tener 8 - 16 caracteres')
    exit 

password_complexity = {
    'upper_letters' : False,
    'numbers' : False,
    'symbols' : False,
    'lower_letters': True

}

print('Desea incluir letras mayúsculas?\n1. Sí\n2. No')
with_upper_letters = int(input(':'))

if with_upper_letters not in {1,2}:
    print('Selección incorrecta')
if with_upper_letters == 1:
    password_complexity["upper_letters"] = True
    
print('Desea incluir números?\n1. Sí\n2. No')
with_numbers = int(input(':'))

if with_numbers not in {1,2}:
    print('Selección incorrecta')
if with_numbers == 1:
    password_complexity["numbers"] = True
    
print('Desea incluir simbolos?\n1. Sí\n2. No')
with_symbols = int(input(':'))

if with_symbols not in {1,2}:
    print('Selección incorrecta')
if with_symbols == 1:
    password_complexity["symbols"] = True
   
password = ""

for i in range(pass_long):
    next_char = choice(list(password_complexity.keys()))
    next_char_value = ""
    
    if password_complexity[next_char] == True:
        match next_char:
            case 'upper_letters':
                next_char_value = choice(upper_letters)
            case 'symbols':
                next_char_value = choice(symbols)
            case 'numbers':
                next_char_value = str(randint(0, 9))
            case _:
                next_char_value = choice(upper_letters).lower()
    else:
        next_char_value = choice(upper_letters).lower()
        
    password += next_char_value

print(password)