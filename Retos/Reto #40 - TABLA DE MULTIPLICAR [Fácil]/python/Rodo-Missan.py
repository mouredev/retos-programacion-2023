def mostrarTabla(numero):
    print(f"\nTABLA DE MULTIPLICAR DEL {numero}")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")

while True:
    try:
        nro = int(input("Ingrese un número: "))
        mostrarTabla(nro)
        break
    except ValueError:
        print("ERROR: Debe ingresar un número entero")