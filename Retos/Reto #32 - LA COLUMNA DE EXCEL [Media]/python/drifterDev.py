def columna_excel(cadena: str) -> int:
    letras = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    respuesta = 0
    n = len(cadena)
    potencia = n - 1
    for i in range(n):
        if potencia == 0:
            respuesta += letras.index(cadena[i])
        else:
            respuesta += ((26) ** potencia) * letras.index(cadena[i])
        potencia -= 1
    return respuesta


if __name__ == "__main__":
    print(columna_excel("A"))
    print(columna_excel("AA"))
    print(columna_excel("CA"))
    print(columna_excel("Z"))
    print(columna_excel("AAA"))
    print(columna_excel("AZZ"))
