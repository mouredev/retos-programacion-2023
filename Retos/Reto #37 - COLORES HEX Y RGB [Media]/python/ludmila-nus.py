# importamos modulos
from termcolor import colored

def conversor_RGB(r,g,b):
    """ funcion que convierte el color en formato RGB a formato Hexadecimal"""
    
    r_hex = hex(r)
    g_hex = hex(g)
    b_hex = hex(b)

    # eliminar el prefijo "0x" de la cadena hexadecimal
    hexadec = [r_hex, g_hex, b_hex]
    for i in range(len(hexadec)):
        hexadec[i] = hexadec[i].lstrip("0x")

    # concatena todos los valores de la lista para que salgan sin espacios
    hex_concatenado = ''.join(hexadec)
   
   # imprime el resultado
    print(colored(f'El color en formato Hexadecimal es: #{hex_concatenado}', 'yellow'))
    print()


def conversor_hex(valores_lista):
    """ funcion que convierte el color en formato Hexadecimal a RGB """
    
    # Convierte los valores hexadecimales a enteros
    # se proporciona 16 como segundo valor para indicar que la cadena esta en base 16 ( hexadecimal)
    r1 = int(valores_lista[0], 16)
    r2 = int(valores_lista[1], 16)
    g1 = int(valores_lista[2], 16)
    g2 = int(valores_lista[3], 16)
    b1 = int(valores_lista[4], 16)
    b2 = int(valores_lista[5], 16)

    # Multiplicamos por 16 los primeros números de cada par de dígitos y le sumamos el segundo par
    r = r1 * 16 + r2
    g = g1 * 16 + g2
    b = b1 * 16 + b2
    
    # Asegurarse de que los valores estén en el rango correcto (0-255)
    r = min(max(r, 0), 255)
    g = min(max(g, 0), 255)
    b = min(max(b, 0), 255)
   
    RGB = [r, g, b]

    # imprime el resultado
    print(colored(f'El color en formato RGB es: {RGB}', 'yellow'))
    print()

   
def inicio():
    print('Bienvenido al conversor de colores')
    continuar = True
    while continuar:
        accion = input('¿Que desea realizar? seleccione una opcion \n 1-convertir de RGB a Hexadecimal \n 2-Convertir de Hexadecimal a RGB  \n 3-Salir del conversor \n opcion: ')
        
        if accion == '1':
            # Se solicita al usuario ingresar el valor del color en R-G-B.
            valor_r= int(input('Ingrese el valor del color en R: '))
            valor_g= int(input('Ingrese el valor del color en G: '))
            valor_b= int(input('Ingrese el valor del color en B: '))
            # llama a la funcion para convertir el valor de RGB a Hex
            conversor_RGB(valor_r, valor_g, valor_b)
    
        if accion == '2':
            # Se solicita al usuario ingresar el valor del color en formato hexadecimal.
            valores = input('Ingrese el valor del color en formato hexadecimal: (ej:FF0000) #')

            # Se crea una lista para almacenar los valores en distintas posiciones.
            valores_lista = []
            
            # Se agrega cada carácter del valor hexadecimal a la lista.
            for n in valores:
                valores_lista.append(n)
            
            # se llama a la funcion para convertir de valor Hex a RGB
            conversor_hex(valores_lista)
    
        if accion == '3':
            # se cierra el conversor
            print(colored('Gracias por utilizar nuestro conversor. ¡Hasta la proxima!','magenta'))
            continuar = False

# se inicia el script
inicio()