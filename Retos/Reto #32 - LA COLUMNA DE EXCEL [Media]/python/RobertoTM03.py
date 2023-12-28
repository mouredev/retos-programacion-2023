# /*
#  * Crea una función que calcule el número de la columna de una hoja de Excel
#  * teniendo en cuenta su nombre.
#  * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
#  * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
#  */

def numero_columna(columna):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return sum([(alfabeto.index(columna[n]) + 1) * (26 ** (len(columna) - 1 - n)) for n in range(len(columna))])

print(numero_columna("CA"))
