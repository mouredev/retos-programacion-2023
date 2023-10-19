
entero = int(input("Introduce un numero del 1 al 11 para hacer una tabla de multiplicar:  "))
if entero <= 11:
    for i in range(1 , 11):
        print(f"{entero} * {i} =  {entero*i} ")
        
else:
    print("El numero ingresado no esta en el rango del 1 al 11 o no es entero, vuelta a intentarlo")
    