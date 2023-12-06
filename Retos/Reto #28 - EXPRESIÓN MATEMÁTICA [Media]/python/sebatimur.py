num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese otro número: "))
operacion = input("Ingrese la operación que desea realizar (+, -, * o /): ")

if operacion == '+':
    resultado = num1 + num2
    print("El resultado de la suma de", num1, "+", num2, "es:", resultado)
elif operacion == '-':
    resultado = num1 - num2
    print("El resultado de la resta de", num1, "-", num2, "es:", resultado)
elif operacion == '*':
    resultado = num1 * num2
    print("El resultado de la multiplicación de", num1, "*", num2, "es:", resultado)
elif operacion == '/':
    if num2 == 0:
        print("No se puede dividir por 0")
    else:
        resultado = num1 / num2
        print("El resultado de la división de", num1, "/", num2, "es:", resultado)
else:
    print("Operador inválido")