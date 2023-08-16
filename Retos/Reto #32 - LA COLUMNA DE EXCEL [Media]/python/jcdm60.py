# Reto #32: La Columna de Excel
#### Dificultad: Media | Publicación: 07/08/23 | Corrección: 14/08/23

## Enunciado


#
# Crea una función que calcule el número de la columna de una hoja de Excel
# teniendo en cuenta su nombre.
# - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
# - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
#

class ExcelColumn:
    def __init__(self, column_name):
        self.column_name = column_name

    def to_number(self):
        column_number = 0
        for char in self.column_name:
            column_number = column_number * 26 + ord(char) - ord('A') + 1
        return column_number

if __name__ == "__main__":
    column_A = ExcelColumn("A")
    print(column_A.to_number())  # Salida: 1
    column_Z = ExcelColumn("Z")
    print(column_Z.to_number())  # Salida: 26
    column_AA = ExcelColumn("AA")
    print(column_AA.to_number())  # Salida: 27
    column_CA = ExcelColumn("CA")
    print(column_CA.to_number())  # Salida: 79