# /*
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
#  */

def print_triforce(rows: int):

    for row in range(0, rows):
        start_space = " " * (((2 * rows) - 1) - row)
        print_row = "*" * ((2 * (row + 1)) - 1)
        print(f"{start_space}{print_row}")

    for row in range(rows, rows * 2):
        current_row = row - rows
        start_space = " " * ((rows - current_row) - 1)
        middle_space = " " * ((2 * (rows - current_row)) - 1)
        print_row = "*" * ((2 * (current_row + 1)) - 1)
        print(f"{start_space}{print_row}{middle_space}{print_row}")

print_triforce(2)
print_triforce(5)