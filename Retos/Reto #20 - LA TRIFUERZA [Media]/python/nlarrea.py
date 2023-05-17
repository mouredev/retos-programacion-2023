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
    total_rows = 2 * rows
    first_spaces = 2 * rows - 1
    triforce = ''

    for i in range(1, total_rows + 1):
        if i == 1:
            triforce += f"{' ' * first_spaces}*\n"
            first_spaces -= 1
        elif i % 2 == 0:
            triforce += f"{' ' * first_spaces}" + '*** ' * int(i / 2) + '\n'
            first_spaces -= 1
        elif i % 2 != 0:
            triforce += f"{' ' * first_spaces}" + ('*' + ' ' * (3)) * int((i + 1) / 2) + '\n'
            first_spaces -= 1
    print(triforce)

draw_triforce(2)