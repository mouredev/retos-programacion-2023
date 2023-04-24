import random
import string

longitud = int(input('Ingresa la cantidad de caracteres entre 8 y 16: '))

num = input('Quieres que incluya números[y/n]: ')
if num == 'y':
    num = True
elif num == 'n':
    num = False
else:
    print('Parámetro no válido.')

may = input('Quieres que incluya mayúsculas[y/n]: ')
if may == 'y':
    may = True
elif may == 'n':
    may = False
else:
    print('Parámetro no válido.')

sim = input('Quieres que incluya símbolos[y/n]: ')
if sim == 'y':
    sim = True
elif sim == 'n':
    sim = False
else:
    print('Parámetro no válido.')

def password_generator(longitud, numeros, mayusculas, minusculas, simbolos):
    if longitud >=8 and longitud <=16:
            char_list = []
            if numeros:
                char_list += list(string.digits)
            if mayusculas:
                char_list += list(string.ascii_uppercase)
            if minusculas:
                char_list += list(string.ascii_lowercase)
            if simbolos:
                char_list += list(string.punctuation)
            password = "".join(random.choices(char_list, k=longitud))
            return password

    else:
        print('[-] Error, debes ingresar una cantidad entre 8 y 16 ')

password = password_generator(longitud=longitud,numeros=num, mayusculas=may, minusculas=True, simbolos=sim)
print(password)
