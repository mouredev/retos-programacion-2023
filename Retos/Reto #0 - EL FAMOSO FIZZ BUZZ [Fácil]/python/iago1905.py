for i in range(1,101):
    salida = ""
    if (i % 3 == 0) :
        salida += "fizz"
    if (i % 5 == 0) :
        salida += "buzz"
    print(salida) if salida else print(i)