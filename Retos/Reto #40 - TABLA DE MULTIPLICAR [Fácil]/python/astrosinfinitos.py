#
# Crea un programa que sea capaz de solicitarte un número y se
# - Debe visualizarse qué operación se realiza y su resultado.
#   Ej: 1 x 1 = 1
#       1 x 2 = 2
#       1 x 3 = 3
#       ...
#


entrada_validada = False
numero_para_multiplicar = int(input("Introduce un número: "))

while (
    not entrada_validada
):  # Compruebo con el try except que efectivamente hemos introducido un número
    try:
        for i in range(1, 11):
            print(f"{numero_para_multiplicar} x {i} = {numero_para_multiplicar * i}")
            entrada_validada = True
    except ValueError:
        print("Por favor, introduce un número válido.")
