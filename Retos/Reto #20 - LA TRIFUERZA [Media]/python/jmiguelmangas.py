"""/*
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
 */"""
def get_number():
    try:
        return int(input("Numero de Filas de los Triangulos: "))
    except ValueError:
        print("El valor introducido no es un entero")
def triforce_constructor(number):
    max_side = (number*2)-1
    min_side = number - 1
    character_brick = "*"
    rows_triangle = number
    width_max = (max_side * 2) + min_side
    print_triforce(max_side,min_side,character_brick,width_max,rows_triangle)
    
def print_triforce(max_side,min_side,character_brick,width_max,rows_triangle):
    row_actual = 1
    spaces = width_max - row_actual
    
    space_character = " "
    for i in range(rows_triangle):
        spaces = width_max - row_actual
        print(f"{space_character*int(spaces/2)}{row_actual*character_brick}{space_character*int(spaces/2)}")
        row_actual += 2
    
    row_actual = 1
    spaces_lateral = int(spaces/2) - 1
    spaces_middle = max_side
    for i in range(rows_triangle):
        
        print(f"{space_character*spaces_lateral}{row_actual*character_brick}{space_character*spaces_middle}{row_actual*character_brick}{space_character*spaces_lateral}")
        row_actual += 2
        spaces_lateral -= 1
        spaces_middle -= 2
def main():
    number = get_number()
    triforce_constructor(number)
    
if __name__ == "__main__":
    main()