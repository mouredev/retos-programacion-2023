def print_tabla():
    num_solicitado = input("Dame un número:  ")
    num_solicitado = int(num_solicitado)
    print('\nTabla del número ' + str(num_solicitado) + '\n')
    for i in range(0,10):
        resultado = num_solicitado * i
        print(str(num_solicitado) + " x " + str(i) + " = " + str(resultado))


print_tabla()