
"""
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 """

def MultiplicationTable(n:int):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
    menu()

if __name__ == "__main__":
    
    def menu():
        chosen_element = input("\nElegir numero de tabla de multiplicar, X:Salir \n")
        
        if chosen_element.isnumeric() and int(chosen_element) <= 10:
            n = int(chosen_element)
            MultiplicationTable(n)

        elif chosen_element == "X" or chosen_element == "x":
            exit

        else:
            print("\nOpción no válida, vuelve a intentarlo")
            menu()
    menu()