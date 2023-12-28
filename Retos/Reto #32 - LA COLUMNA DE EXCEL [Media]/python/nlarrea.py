"""
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
"""

from functools import reduce

# Array of ASCII values of the A-Z chars
ASCII_VALUES = [65 + idx for idx in range(26)]

def check_errors(column:str):
    """ Checks whether the value of the given column name is correct or not. """

    if type(column) != str: raise TypeError("You have to enter a String.")
    
    column = column.upper()
    
    if len(column) < 1: raise SyntaxError("You have to give at least one letter as column name.")

    ascii_codes = [ord(col) for col in column]
    if (any(code < ASCII_VALUES[0] for code in ascii_codes) or
        any(code > ASCII_VALUES[len(ASCII_VALUES) - 1] for code in ascii_codes)):
        raise IndexError("The given column name is out of range.")
    

def getColumnNumber(column:str) -> int:
    """ Receives a column name and returns its value. If the given column name
     is not correct, returns `-1`. """
    
    # Aux function

    def reduce_col_values(total:int, current:tuple) -> int:
        """ Reduce function: calculates the value of an iterable taking into
         account how many times the list of the `ASCII_VALUES` constant has
         been flipped and the end position. """

        curr_idx, curr_char = current
        curr_col_position = ASCII_VALUES.index(ord(curr_char)) + 1

        # len(ASCII_VALUES) ** idx = number of turns to the A-Z columns (starts at idx = 0)
        return total + ((len(ASCII_VALUES) ** curr_idx) * curr_col_position)


    # Checking errors
    
    try:
        check_errors(column)
    except Exception as error:
        print(error)
        return -1

    # Get column number

    column = column.upper()
    reversed_column_list = list(column)[::-1]

    return reduce(
        reduce_col_values,
        [(idx, char) for (idx, char) in enumerate(reversed_column_list)],
        0
    )


print(getColumnNumber('A'))      # 1
print(getColumnNumber('Z'))      # 26
print(getColumnNumber('AA'))     # 27
print(getColumnNumber('CA'))     # 79

# Checking errors
print(getColumnNumber(''))       # -1, prints: You have to give at least one letter as column name.
print(getColumnNumber(2))        # -1, prints: You have to enter a String.
print(getColumnNumber('_'))      # -1, prints: The given column name is out of range.