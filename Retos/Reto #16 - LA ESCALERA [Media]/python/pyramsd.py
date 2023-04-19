def escalera(num):
    if num > 0:
        i = 0
        inicio = (num * 2) + 1
        while i < inicio:
            posicion = f"{{:>{inicio-i}s}}"
            if i == 0: print(f"{posicion}".format('_'))
            else:
                print(f"{posicion}".format('_|'))
                i += 1

            i += 1

    elif num < 0:
        i = 1
        termino = (abs(num) * 2) + 1
        while i <=  termino:
            posicion = f"{{:>{i}s}}"
            if i == 1: print(f"{posicion}".format('_'))
            else:
                print(f"{posicion}".format('|_'))

            i += 2
    else:
        print("__")

num = int(input("Numero de escalones: "))

escalera(num)
