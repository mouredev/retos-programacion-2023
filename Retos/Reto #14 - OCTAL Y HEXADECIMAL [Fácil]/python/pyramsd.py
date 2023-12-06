def decimal_a_hexadecimal_octal(numero):

    conversion_hexa = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    digitos_hex = []
    digitos_oct = []
    num_para_hex = numero
    num_para_oct = numero
    
    while num_para_hex != 0:

        resto_hex = num_para_hex % 16
        # Si el resto es mayor a 9, usar la conversión a letra correspondiente
        if resto_hex > 9:
            resto_hex = conversion_hexa[resto_hex]
        digitos_hex.append(resto_hex)
        num_para_hex //= 16
    con_hexa = ''.join(str(d) for d in digitos_hex[::-1])
    print(f"Forma hexadecimal: {con_hexa}")


    while num_para_oct != 0:
        resto_oct = num_para_oct % 8
        digitos_oct.append(resto_oct)
        num_para_oct //= 8
    con_octa = ''.join(str(d) for d in digitos_oct[::-1])
    print(f"Forma octal: {con_octa}")
    
numero_decimal = int(input("Ingrese un número decimal: "))

decimal_a_hexadecimal_octal(numero_decimal)
