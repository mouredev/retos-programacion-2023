"""
/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */
"""

def print_table(number: int) -> None:
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


def main():
    number = input("Enter a number: ")

    try:
        number = int(number)

        while number < 0 or number > 10:
            number = input("Enter a number between (0 and 10): ")
            number = int(number)
        
        print_table(number)
    except Exception as e:
            print(f"Error: + {str(e)})")

if __name__ == "__main__":
    main()
