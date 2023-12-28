"""/*
 * Crea una función que reciba un número decimal y lo tranforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */"""

def get_number():
    return input("Numero Decimal: ")

def transform_oct_hex(numero):
    oct = trans_oct(numero)
    hex = trans_hex(numero)
    return (oct,hex)

def trans_oct(numero):
    lista_restos = []
    numero = int(numero)
    octal = ""
    while numero != 0:
        division = (int(numero/8))
        resto = numero%8

        lista_restos.append(resto)
        numero = division

    for i in range(len(lista_restos)):
        numero_invertir = len(lista_restos)-i
        if numero_invertir >= 0:
            octal = octal + str(lista_restos[numero_invertir-1])
    return int(octal)
                
def trans_hex(numero):
    lista_restos = []
    numero = int(numero)
    hex = ""
    while numero != 0:
        division = (int(numero/16))
        resto = str(numero%16)
        match(resto):
            case "10":
                lista_restos.append("a")
            case "11": 
                lista_restos.append("b")
            case "12":
                lista_restos.append("c")
            case "13":
                lista_restos.append("d")
            case "14":
                lista_restos.append("e")
            case "15":
                lista_restos.append("f")
            case _:
                lista_restos.append(resto)
        numero = division
    for i in range(len(lista_restos)):
        numero_invertir = len(lista_restos)-i
        if numero_invertir >= 0:
            hex = hex + str(lista_restos[numero_invertir-1])
    return hex
    
def main():
    
    numero = get_number()
    oct,hex = transform_oct_hex(numero)
    print(f"El numero {numero} transformado en Octal es: {oct}, y transformado en Hexadecimal es: {hex}")
    
if __name__ == "__main__":
    main()