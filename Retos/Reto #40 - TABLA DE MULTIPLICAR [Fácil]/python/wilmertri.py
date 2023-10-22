def multiplication_table(n: int) -> None:
    for i in range(1, 11):
        print(f"{n} x {i} = {i*n}")

number = int(input("Ingrese un número para imprimir su tabla de multiplicar: "))
multiplication_table(number)