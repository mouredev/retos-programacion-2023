def convertToBase(decimal,base):
    digitos = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    resultado = []
    while decimal >= base:
        resultado.append(digitos[decimal % base])
        decimal  = decimal // base        
    resultado.append(digitos[decimal])
    return "".join(resultado[::-1])

def convertirDecimalToOctal(decimal):
    return convertToBase(decimal,8)

def convertDecimalToHexa(decimal):
    return convertToBase(decimal,16)

print(convertToBase(8596,16))
print(convertDecimalToHexa(8596))
print(convertToBase(8596,8))
print(convertirDecimalToOctal(8596))