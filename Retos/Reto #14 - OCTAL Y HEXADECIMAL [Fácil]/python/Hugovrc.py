
def octal_y_hexadecimal(num):
    print(f"Numero Decimal = {num}")
    numero = num
    octal = 8
    num_octal = ""
    cociente = num / octal
    tablahexadecimal = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9,
                        10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}

    while cociente > 0:
        cociente = num / octal
        multi = octal * int(cociente)
        residuo = num - multi
        num_octal += str(residuo)
        num = int(cociente)
        
        
    print(f"Octal = {num_octal[::-1][1:]}")

    hexadecimal = 16
    num_hexa = []
    num_hexadecimal = ""
    cociente2 = numero / hexadecimal
    
    while cociente2 > 0:
        
        cociente2 = numero / hexadecimal
        residuo = numero % hexadecimal
        num_hexa.append(residuo)
        
        
        numero = int(cociente2)
    
    for n in num_hexa:
            
            if n in tablahexadecimal.keys():
                num_hexadecimal += str(tablahexadecimal[n])
    print(f"Hexadecimal = {num_hexadecimal[::-1]}")
   



octal_y_hexadecimal(1000)
octal_y_hexadecimal(345)
octal_y_hexadecimal(298)