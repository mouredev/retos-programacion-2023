"""
    /*
 * Crea una función que dibuje una espiral como la del ejemplo.
 * - Únicamente se indica de forma dinámica el tamaño del lado.
 * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
 *
 * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
 ════╗
 ╔══╗║
 ║╔╗║║
 ║╚═╝║
 ╚═══╝
"""
import math

def espiral(longitud: int):
    mitad = (math.ceil(longitud / 2))
    #* Primera mitad
    print('═' * (longitud-1) + '╗')
    for i in range(1, mitad):
        print('║' * (i-1) + '╔' + '═' * (longitud-i-i-1) + '╗' + '║' * (i))
    #* segunda mitad
    for i in range(mitad -2, -1 ,-1):
        print('║' * (i) + '╚' + '═' * (longitud -2 -2*i) + '╝' + '║' * (i))

if __name__ == '__main__':

    #longitud = int(input('¿Caul es la anchura? '))
    espiral(5)
    espiral(10)
    espiral(15)