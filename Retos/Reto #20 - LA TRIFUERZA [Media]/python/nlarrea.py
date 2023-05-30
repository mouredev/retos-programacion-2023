"""
 *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
 *
 * Crea un programa que dibuje una Trifuerza de "Zelda"
 * formada por asteriscos.
 * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
 * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 *
 * Ejemplo: Trifuerza 2
 * 
 *    *
 *   ***
 *  *   *
 * *** ***
 *
"""

def draw_triforce(rows):
    triforce = ''
    left_spaces = 2 * rows - 1

    for i in range(1, rows + 1):
        triforce += (" " * left_spaces) + ("*" * (2 * i - 1)) + "\n"
        left_spaces -= 1

    for i in range(1, rows + 1):
        triforce += ((" " * left_spaces) + ("*" * (2 * i - 1)) + (" " * (left_spaces + 1))) * 2
        triforce += "\n"
        left_spaces -= 1
        
    print(triforce)

draw_triforce(3)