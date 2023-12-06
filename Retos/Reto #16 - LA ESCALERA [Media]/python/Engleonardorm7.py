def dibujar_escalera(numero):
    if numero > 0:
        for i in range(numero):
            print("  " * (numero - i - 1) + "_" +'|')
    elif numero < 0:
        for i in range(abs(numero)):
            print("  " * i + '|'+"_" )
    else:
        print("__")

dibujar_escalera(4)