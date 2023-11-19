"""
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
"""


def main():
    try:
        inputNumber = int(input("Introduce un numero: "))

    except ValueError:
        print("ERROR: El valor introducido debe ser un número entero.")
        return
    


    for _ in range(1, 11):
        print(f"{inputNumber} x {_} = {inputNumber * _}")


if __name__ == "__main__":
    main()
