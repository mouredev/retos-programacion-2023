# /*
#  * Crea una función que dibuje una espiral como la del ejemplo.
#  * - Únicamente se indica de forma dinámica el tamaño del lado.
#  * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
#  *
#  * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
#  * ════╗
#  * ╔══╗║
#  * ║╔╗║║
#  * ║╚═╝║
#  * ╚═══╝
#  */

def input_numero_entero(prompt=''):
    """ Verifica si es un entero positivo"""
    while True:
        try:
            n = int(input(prompt))
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print("Numero Invalido")
            prompt = "Por favor ingresa un numero entero: "
    return n

def imprimir_espiral(numero):
    rows = []
    for n in range(0,numero):
        rows.append("")
        rows[n]=["="]*numero
    mitad = int((numero/2) + (numero%2))
    print(mitad)
    for number in range(mitad,numero):
        rows[numero-number-1][number]="╗"
        rows[number][number]="╝"
        rows[number][numero-number-1]="╚"
    for col in reversed(range(mitad,numero)):
        for row in range(numero-col,col):
            rows[row][col]="║"
    for col in range(0,mitad):
        for row in range(col+1,numero-col-1):
            rows[row][col]="║"
    if numero % 2 == 0:
        mitad+=1
    else:
        rows[mitad-1][mitad-1]="╗"
    for number in range(mitad,numero):
        rows[numero-number][numero-number-1]="╔"
    for number in range(0,numero):
        print(''.join(rows[number]))

n = input_numero_entero("Ingresa el numero del tamaño del lado: ")
imprimir_espiral(int(n))