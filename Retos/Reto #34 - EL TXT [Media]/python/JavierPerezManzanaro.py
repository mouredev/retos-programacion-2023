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
 */

'''


import os

FICHERO = '#34 Fichero TXT.txt'

def crear_fichero_o_reescribir(contenido_anterior):
    """Función que crea el TXT o re escribe el contenido (añandiendo el contenido anterior mas el nuevo)

    Args:
        contenido_anterior (_type_): Contenido del TXT anterior
    """
    with open(FICHERO, 'w', encoding='utf-8') as archivo:
        print('Ve escribiendo el contendio por lineas, si quieres salir escribe "salir": ')
        contenido_acumulado = anadimos_lineas()
        contenido_acumulado = contenido_anterior + contenido_acumulado
        archivo.writelines(contenido_acumulado)


def fichero_existente():
    """Función que pregunta que hacer si el fichero existe: Sobre escribimos o continuamos con la edición
    """
    archivo_str = ''
    sobreescribir = input('¿Quieres sobreescribir el archivo (s/n)? ')
    if sobreescribir == 's':
        crear_fichero_o_reescribir('')
    else:
        with open(FICHERO, 'r', encoding='utf-8') as archivo:
            numero_linea = 1
            print()
            print('El conenido del archivo es:')
            for linea in archivo:
                numero_linea +=1
                if linea != '\n':
                    print(f'Línea: {numero_linea}| {linea[:-2]}')
                    archivo_str = archivo_str + linea
                else:
                    pass
        crear_fichero_o_reescribir(archivo_str)


def anadimos_lineas()-> str:
    """Añadimos contenido al archivo TXT

    Returns:
        contenido_acumulado: str: todo el contenido del archivo TXT
    """
    contenido_acumulado = ''
    linea = 0
    paso = True
    while paso:
        linea +=1
        contenido = input(f'Línea {linea}| ')
        if contenido == 'salir':
            paso = False
        else:
            paso = True
            contenido_acumulado = contenido_acumulado + contenido + '\n'
    #print(contenido_acumulado)
    return contenido_acumulado



if __name__ == '__main__':
    print('-'*20)
    print()
    if os.path.isfile(FICHERO):
        print(f'El fichero: "{FICHERO}" existe')
        print()
        fichero_existente()
    else:
        print(f'El fichero: "{FICHERO}" NO existe')
        print()
        crear_fichero_o_reescribir('')



#