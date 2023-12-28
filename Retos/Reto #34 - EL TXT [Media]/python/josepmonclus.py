'''
Crea un programa capaz de interactuar con un fichero TXT.
IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección. 
Únicamente el código.

- Si no existe, debe crear un fichero llamado "text.txt".
- Desde el programa debes ser capaz de introducir texto por consola y guardarlo
  en una nueva línea cada vez que se pulse el botón "Enter".
- Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
  a continuación o borrar su contenido y comenzar desde el principio.
- Si se selecciona continuar escribiendo, se tiene que mostrar por consola
  el texto que ya posee el fichero.  
'''

import os

file_name = 'text.txt'

overwrite = 'N'
exists = False

if os.path.exists(file_name):
    exists = True
    overwrite = input('El fichero ya existe, quieres sobreescribirlo (S/N)? ')
    overwrite = overwrite.upper()
    
if overwrite != 'S' and overwrite != 'N':
    print('Respuesta incorrecta.')
else:
    if exists and overwrite == 'N':
        with open(file_name, "r") as file:
            print(file.read())
    else:
        with open(file_name, "w") as file:
            file.write('')
    
    while True:
        with open(file_name, "a") as file:
            line = input('')
            if line == '':
                break
            
            file.write(line + '\n')

