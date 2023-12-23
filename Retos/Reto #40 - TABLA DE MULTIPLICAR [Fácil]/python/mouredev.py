try:
    number = int(input("Introduce el número para generar su tabla de multiplicar: "))

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
        
except ValueError:
    print("Error: Introduce un número entero válido.")

