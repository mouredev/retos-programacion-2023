"""
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
 */
"""

def calcular_puntos(palabra: str) -> int:
    """ Calcula el valor de un string pasado como la suma del valor de cada letra a=1 z=26
    
        Params:
            palabra str: string cuyo valor hay que calcular

        result:
            puntos int: suma de el valor de cada letra de la palabraa

        ej:
        'abc' = 1 + 2 + 3 = 6
    
    
    """
    letras = {'a':1, 'á':1, 'b':2, 'c':3, 'd':4, 'e':5, 'é':5, 'f':6, 'g':7, 'h':8, 'i':9, 'í':9, 'j':10,
              'k':11, 'l':12, 'm':13, 'n':14, 'ñ':15, 'o':16, 'ó':16, 'p':17, 'q':18, 'r':19, 's':20,
              't':21,'u':22, 'ú':22, 'ü':22, 'v':23, 'w':24, 'x':25, 'y':26, 'z':27 }

    try:
        resultado = sum([letras[x] for x in palabra])
    except KeyError as e:
        print(f' El caracter {e} no pertenece as abecedario español...')
        resultado = 0
    
    return resultado



if __name__ == '__main__':   
    
    puntuacion = 0

    while True:  

        palabra = input(""" 
    Teclee la palabra
(presione ENTER para salir)

---> """)
        
        if palabra == '': break
        if not palabra.isalpha():
            print(" Sólo se permiten letras de la 'a' a la 'z', vuelva a intentar...")
        else:
            puntuacion = calcular_puntos(palabra.lower())

            if puntuacion == 100:
                print('Enhorabuena, ha ganado!!!')
                break
            else:
                print(f'La puntuacion {puntuacion} de su palabra no es 100, vuelva a intentar')
