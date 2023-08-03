def escalera (n):
    if n < 0:
        n = n * -1
        texto = "|_"
        i = 0
        while i < n:
            print(texto)
            texto = "  " + texto
            i += 1
    elif n > 0:
        espacio = "  "
        character = "_|"
        print((espacio * (n + 1)) + "_")
        while n > 0:
            texto = (espacio * n) + character
            print(texto)
            n -= 1
    else:
        print("__")

while True:
    try:
        numero = int(input("N° de escaleras: "))
    except:
        print("ERROR: introduzca un numero")
    else:
        break

escalera(numero)
