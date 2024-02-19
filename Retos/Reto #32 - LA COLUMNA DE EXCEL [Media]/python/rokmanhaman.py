"""
Reto #32: LA COLUMNA DE EXCEL
MEDIA | Publicación: 07/08/23 | Resolución: 14/08/23
/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */
"""

def ExcelColumn(column):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i,j in enumerate(letters[:26]):
        for x, y in enumerate(letters[:26]):
            letters.append(j + y)

    return letters.index(column) +1 



col = 'CA'
out = ExcelColumn(col)
print(f"\n\nEl número de la columna {col} es el: {out}\n\n")

