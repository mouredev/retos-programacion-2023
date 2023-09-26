""" * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)"""

import random

# Inicializamos las variables con los caracteres
char_minus = str('abcdefghijklmnñopqrstuvwxyz')
char_mayus = str(char_minus.upper())
char_nums = str('1234567890')
char_symbols = str('@!-.,?¡¿)((/&%')
pass_length = 0

#Mensaje de bienvenida
print('------------------------------------------------------------------')
print('Bienvenido al generador de claves!')
print('Por favor, seleccione los criterios para la generacion de la clave:')
print('------------------------------------------------------------------')

# Creamos la funcion para generar la contraseña segun los criterios
def password_generator():
    criterio = ''
    #Longitud
    while True:
        longitud = int(input('Indique la longitud de la contraseña (entre 8 y 16 caracteres): '))
        if longitud < 8 or longitud > 16:
            print('ERROR! Debe elegir un numero entre 8 y 16.')
        elif longitud >= 8 and longitud <= 16:
            pass_length = longitud
            break
    #Minusculas
    while True:
        minusculas = input('\nDesea que tenga minusculas? (Y/N): ')
        minusculas = minusculas.lower()
        if minusculas == 'y':
            criterio += char_minus
            break
        elif minusculas == 'n':
            break
        elif minusculas != 'y' or minusculas != 'n':
            print('ERROR! Debe elegir una de las dos opciones (Y/N).')
    #Mayusculas
    while True:
        mayusculas = input('\nDesea que tenga mayusculas? (Y/N): ')
        mayusculas = mayusculas.lower()
        if mayusculas == 'y':
            criterio += char_mayus
            break
        elif mayusculas == 'n':
            break
        elif mayusculas != 'y' or mayusculas != 'n':
            print('ERROR! Debe elegir una de las dos opciones (Y/N).')
    #Simbolos
    while True:
        simbolos = input('\nDesea que tenga simbolos? (Y/N): ')
        simbolos = simbolos.lower()
        if simbolos == 'y':
            criterio += char_symbols
            break
        elif simbolos == 'n':
            break
        elif simbolos != 'y' or simbolos != 'n':
            print('ERROR! Debe elegir una de las dos opciones (Y/N).')
    #Numeros
    while True:
        numeros = input('\nDesea que tenga numeros? (Y/N): ')
        numeros = numeros.lower()
        if numeros == 'y':
            criterio += char_nums
            break
        elif numeros == 'n':
            break
        elif numeros != 'y' or numeros != 'n':
            print('ERROR! Debe elegir una de las dos opciones (Y/N).')

    # Generador aleatorio de contraseñas segun criterios.
    for password in range(1):
        pass_sample = random.sample(criterio, pass_length)
        final_pass = ''.join(pass_sample)
        print(f'Su contraseña generada es la siguiente ==> {final_pass}')

password_generator()