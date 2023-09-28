"""
```
/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */
```"""
column_values = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}


def get_column_id():
    return input("Id de la columna: ").strip().upper()


def transform_columnid_number(column_id):
    longitud_id = len(column_id)
    valor = 0
    for i in range(longitud_id):
        if column_id[i] in column_values:
            valor = column_values[column_id]

    return valor


def main():
    column_id = get_column_id()
    print(transform_columnid_number(column_id))


if __name__ == "__main__":
    main()
