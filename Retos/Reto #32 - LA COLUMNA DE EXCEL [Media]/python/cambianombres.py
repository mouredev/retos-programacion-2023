#    Crea una función que calcule el número de la columna de una hoja de Excel teniendo en cuenta su nombre.
def excel_column(column: str) -> int:
    #   Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = 0

    try:
        for letter in column:
            number = (number * len(alphabet)) + (alphabet.index(letter) + 1)
    except:
        return 0

    return number

'''
    Ejemplos válidos: 
        A = 1, 
        Z = 26, 
        AA = 27, 
        CA = 79.
'''
print(excel_column("A"))
print(excel_column("Z"))
print(excel_column("AA"))
print(excel_column("CA"))

'''
    Mi aporte: Cualquier entrada no válida retorna un 0, dando a entender que la columna no existe.
    Ejemplos no válidos:
        2A = 0,
        2 = 0,
        "" = 0,
        " " = 0.
'''
print(excel_column("2A"))
print(excel_column(2))
print(excel_column(""))
print(excel_column(" "))