

def comparar_cadenas(cadena1, cadena2):
    if len(cadena1) == len(cadena2):
        print("Las cadenas tienen la misma longitud")
        return True
    else:
        print("Las cadenas tienen diferentes longitudes")
        return False


def comparar_caracteres(cadena1, cadena2):
    ch = []
    for index, letter in enumerate(cadena2):
        if letter != cadena1[index]:
            ch.append(letter)
    return ch

# Test 1

# cadena1 = "Me llamo Juan Duque"
# cadena2 = "Me llame Juan Doque"


# Test 2
cadena1 = "Me llamo.Brais Moure"
cadena2 = "Me llamo brais moure"

comparar_cadenas(cadena1, cadena2)
diferentes_caracteres = comparar_caracteres(cadena1, cadena2)
print(f"Las cadenas no tienen los mismos caracteres {diferentes_caracteres}")
