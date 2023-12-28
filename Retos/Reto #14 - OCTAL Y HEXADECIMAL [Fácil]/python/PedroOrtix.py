diccionario_hexa = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
                'F': 15, 'G': 16}

def decimal_hexa(numero: int) -> str:
    hexa = ''
    while numero > 0:
        if numero % 16 > 9:
            hexa = list(diccionario_hexa.keys())[list(diccionario_hexa.values()).index(numero % 16)] + hexa
        else:
            hexa = str(numero % 16) + hexa
        numero = numero // 16
    return hexa

def decimal_octa(numero: int) -> str:
    octa = ''
    while numero > 0:
        octa = str(numero % 8) + octa
        numero = numero // 8
    return octa

def main():
    numero = int(input("Ingrese un número: "))
    print(f"Octal: {decimal_octa(numero)}")
    print(f"Hexadecimal: {decimal_hexa(numero)}")

if __name__ == '__main__':
    main()