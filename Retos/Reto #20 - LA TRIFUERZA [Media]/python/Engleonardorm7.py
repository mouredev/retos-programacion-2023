#  *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
#  *
#  * Crea un programa que dibuje una Trifuerza de "Zelda"
#  * formada por asteriscos.
#  * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
#  * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
#  *
#  * Ejemplo: Trifuerza 2
#  * 
#  *    *
#  *   ***
#  *  *   *
#  * *** ***
#  *

def dibujar_trifuerza(n):
    fila_mayor = 2 * n 

    for i in range(1, n + 1):
        text = "*" * (2 * i - 1)
        text = text.center(fila_mayor * 2)
        print(text)

    for i in range(1, n + 1):
        text = "*" * (2 * i - 1)
        text = text.center(fila_mayor)
        text = text * 2
        print(text)
dibujar_trifuerza(7)
