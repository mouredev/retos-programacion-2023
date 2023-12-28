




def conv_int_hex(valor = 0):
    entero = int(valor)
    decimal = (valor - entero)
    digito = 0 
    resultado = ''
    
    cant_digito = 0 
    
    while entero >0:
        digito =  entero % 16 
        entero = entero // 16
        if digito > 9:
            resultado = chr( 55+digito)+resultado
        else:
            resultado =  str(digito)+resultado
    
    
    while decimal >0 and cant_digito <= 15 :
        
        decimal =  decimal * 16 
        digito = int(decimal)
            
        decimal = decimal - digito
        if cant_digito == 0:
            resultado = resultado + '.'
        if digito > 9:
            
            resultado = resultado + chr( 55+digito)
        else:
            resultado = resultado +  str(digito)
            
        cant_digito += 1

    return resultado


def conv_int_oct(valor = 0):
    entero = int(valor)
    decimal = (valor - entero )
    
    
    digito = 0
    resultado = ''
    cant_digito = 0
    
    while entero >0:
        digito =  entero % 8 
        entero = entero // 8
        resultado =  str(digito)+ resultado
        
    while decimal >0 and cant_digito <= 15 :
        
        decimal =  decimal * 8 
        digito = int(decimal)
        decimal = decimal - digito
        if cant_digito == 0:
            resultado = resultado + '.'
            
        resultado = resultado +  str(digito)
            
        cant_digito += 1

    
    return resultado


if __name__=="__main__":
    print(conv_int_hex(255) )       # FF
    print(conv_int_hex(256) )       # 100
    print(conv_int_hex(4582562))    # 45 ECA2
    print(conv_int_oct(255) )       # 377
    print(conv_int_oct(256) )       # 400
    print(conv_int_oct(4582562))    # 21366242
    print(conv_int_hex(2.3) )       # 2.4CCCCCCCCCCCCC
    
    print(conv_int_oct(2.3) )       # 2.2314631463146314
