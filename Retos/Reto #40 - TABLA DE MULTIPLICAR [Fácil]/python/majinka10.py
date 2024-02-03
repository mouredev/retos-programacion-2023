def tablaDeMultiplicar(number: int):
    for i in range(1, 11):
        print(f"{number} x {i} = {i*int(number)}")

tablaDeMultiplicar(input("Ingresa un número\n"))