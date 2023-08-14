'''
/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */

'''


def col_number(col):
    col = col.upper()
    col_num = 0
    for i in range(len(col)):
        col_num += (ord(col[i]) - 64) * (26 ** (len(col) - i - 1))
    return col_num

d = input("Introduce la columna: ")
print(col_number(d))