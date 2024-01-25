"""
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
"""


def print_table(table: list) -> None:
    for row in table:
        print(row)


def multiplication_table(number: int) -> None:
    # Check if data is correct
    if type(number) != int:
        return "The given data must be a integer!"
    elif number < 0:
        return "The given number must be positive!"
    
    # Get table
    times = 10
    table = [f"{number} x {num} = {number * num}" for num in range(1, times + 1)]

    print_table(table)
    

multiplication_table(7)