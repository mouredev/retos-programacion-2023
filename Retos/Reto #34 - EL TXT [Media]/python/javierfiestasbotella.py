'''
/*
 * Crea un programa capaz de interactuar con un fichero TXT.
 * IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección. 
 * Únicamente el código.
 * 
 * - Si no existe, debe crear un fichero llamado "text.txt".
 * - Desde el programa debes ser capaz de introducir texto por consola y guardarlo
 *   en una nueva línea cada vez que se pulse el botón "Enter".
 * - Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
 *   a continuación o borrar su contenido y comenzar desde el principio.
 * - Si se selecciona continuar escribiendo, se tiene que mostrar por consola
 *   el texto que ya posee el fichero.  
 */'''
import os

nombre_fichero = 'text.txt'

try:
    with open(nombre_fichero, 'r'):
        print(f'El archivo {nombre_fichero} ya existe.')
except FileNotFoundError:
    with open(nombre_fichero, 'w') as file:
        file.write('')
    print(f"El archivo {nombre_fichero} ha sido creado.")

menu = '''1- Continuar escribiendo.
2- Borrar y comenzar a escribir.
3- Salir'''

while True:
    print(menu)
    opcion = int(input('Introduce una opción del menú: '))
    
    if opcion == 1:
        with open(nombre_fichero, 'r') as fichero:
            contenido_fichero = fichero.read()
            print(contenido_fichero)
        
        nuevo_contenido = input('Introduce texto: ')
        with open(nombre_fichero, 'a') as fichero:
            fichero.write(nuevo_contenido + '\n')  # Agregar el contenido y un salto de línea

    elif opcion == 2:
        nuevo_contenido = input('Introduce texto: ')
        with open(nombre_fichero, 'w') as fichero:
            fichero.write(nuevo_contenido + '\n')  # Agregar el contenido y un salto de línea

    elif opcion == 3:
        print('Muchas gracias por utilizar el programa.')
        break

    else:
        print('Introduce una opción válida del menú.')
