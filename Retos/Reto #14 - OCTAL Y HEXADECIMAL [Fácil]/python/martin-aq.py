def dec_to_oct_hex(decimal: int):
    """Está función convierte decimal a octal y hexadecimal"""

    # Octal
    aux_decimal = decimal    
    octal = ""
    
    while aux_decimal > 0:
        octal = str(aux_decimal % 8) + octal
        aux_decimal //= 8
    
    # El condicional octal se puede reemplazar por una expresion ternaria
    if octal == "":
        octal = 0
    else:
        octal
    
    print(f"El numero {decimal} en octal es {octal}")
    
    # Hexadecimal
    hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5:'5', 6: '6', 7: '7', 8: '8',
                9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    aux_decimal = decimal
    hexa = ""
    
    while aux_decimal > 0:
        hexa = hex_dict[aux_decimal % 16] + hexa
        aux_decimal //= 16
    
    # El condicional hexa se puede reemplazar por una expresion ternaria
    if hexa == "": 
        hexa = 0
    else:
        hexa
    
    print(f"El numero {decimal} en hexadecimal es {hexa}")

dec_to_oct_hex(100)
dec_to_oct_hex(31)
dec_to_oct_hex(256)
dec_to_oct_hex(3022)
dec_to_oct_hex(298)
dec_to_oct_hex(15)