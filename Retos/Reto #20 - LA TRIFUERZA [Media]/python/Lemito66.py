'''
/*
 *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
 *
 * Crea un programa que dibuje una Trifuerza de "Zelda"
 * formada por asteriscos.
 * - Debes indicarle el número de number_of_triangles de los triángulos con un entero positivo (number_of_triangles).
 * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 *
 * Ejemplo: Trifuerza 2
 * 
 *    *
 *   ***  
 *  *   *
 * *** ***
 *
 */
'''


def triforce(number_of_triangles: int):

    output = []
    for row in range(1, number_of_triangles+1):
        output.append(' '*(number_of_triangles*2-row) + '*'*(2 * row-1))

    for row in range(1, number_of_triangles+1):
        output.append(' '*(number_of_triangles-row) + '*'*(2 * row-1) + ' ' *
                      (number_of_triangles-row) + ' '*(number_of_triangles-row+1) + '*'*(2 * row-1))
    return output


for i in triforce(2):
    print(i)
