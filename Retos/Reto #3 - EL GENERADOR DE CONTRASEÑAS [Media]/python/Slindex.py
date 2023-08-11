import random as rd
import string as sg

password = ''

long = int(input('Ingrese el número de caracteres deseado para su contraseña [8-16] '))
mayus = input('Desea incluir mayúsculas en su contraseña? [y/n] ')
numeros = input('Desea incluir números en su contraseña? [y/n] ')
simbolos = input('Desea incluir símbolos en su contraseña? [y/n] ')

for i in range(0,long):
    selector = []

    if mayus == 'y':
        randuc = rd.choice(sg.ascii_letters)
        selector.append(randuc)
    else:
        randlc = rd.choice(sg.ascii_lowercase)
        selector.append(randlc)
    if numeros == 'y':
        randn = rd.randint(0,9)
        selector.append(randn)
    if simbolos == 'y':
        randsy = rd.choice(sg.punctuation)
        selector.append(randsy)
    
    password = password+str(rd.choice(selector))

print(f'''
      
    Su contraseña es: {password}

    ''')