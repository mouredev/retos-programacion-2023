# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número: "))

# Imprimir la tabla de multiplicar
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
