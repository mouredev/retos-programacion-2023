#
#Crea un programa que sea capaz de solicitarte un número y se
#encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
#- Debe visualizarse qué operación se realiza y su resultado.
#  Ej: 1 x 1 = 1
#      1 x 2 = 2
#      1 x 3 = 3
#      ...
#

def show_mult_table(number: int):

    print("")

    for index in range(1,11):
        print(str(number) + " x " + str(index) + " = " + str(number * index))

def request_number() -> int:

    while True:
        try:
            number = int(input("Enter an integer to know its multiplication table: "))
            break
        except ValueError:
            print("Only integer numbers are allowed!!")

    return number

n: int = request_number()
show_mult_table(n)
