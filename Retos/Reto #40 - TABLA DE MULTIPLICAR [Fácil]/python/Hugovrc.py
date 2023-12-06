numero = int(input("Ingresa un numero del que desees generar su tabla: "))
    
for num in range(1, 11):
    resultado = numero * num

    print(f"{numero} X {num} = {resultado}")