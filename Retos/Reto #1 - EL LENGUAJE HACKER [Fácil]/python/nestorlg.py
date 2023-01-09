def to_leet (texto):
    
    result = ''
    
    for i in range(0, len(texto)):
        if (texto[i].upper() == 'A'):
            result += '4'
        elif (texto[i].upper() == 'B'):
            result += 'I3'
        elif (texto[i].upper() == 'C'):
            result += '['
        elif (texto[i].upper() == 'D'):
            result += ')'
        elif (texto[i].upper() == 'E'):
            result += '3'
        elif (texto[i].upper() == 'F'):
            result += '|='
        elif (texto[i].upper() == 'G'):
            result += '&'
        elif (texto[i].upper() == 'H'):
            result += '#'
        elif (texto[i].upper() == 'I'):
            result += '1'
        elif (texto[i].upper() == 'J'):
            result += ',_|'
        elif (texto[i].upper() == 'K'):
            result += '>|'
        elif (texto[i].upper() == 'L'):
            result += '1'
        elif (texto[i].upper() == 'M'):
            result += '/\\/\\'
        elif (texto[i].upper() == 'N'):
            result += '^/'
        elif (texto[i].upper() == 'O'):
            result += '0'
        elif (texto[i].upper() == 'P'):
            result += '|*'
        elif (texto[i].upper() == 'Q'):
            result += '(_,)'
        elif (texto[i].upper() == 'R'):
            result += '|2'
        elif (texto[i].upper() == 'S'):
            result += '5'
        elif (texto[i].upper() == 'T'):
            result += '7'
        elif (texto[i].upper() == 'U'):
            result += '(_)'
        elif (texto[i].upper() == 'V'):
            result += '\/'
        elif (texto[i].upper() == 'W'):
            result += '\/\/'
        elif (texto[i].upper() == 'X'):
            result += '><'
        elif (texto[i].upper() == 'Y'):
            result += 'j'
        elif (texto[i].upper() == 'Z'):
            result += '2'
        else:
            result += texto[i]
    
    return result
        

mi_texto = 'Hola mundo, mi nombre es Nestor y soy de Las Palmas de Gran Canaria'
mi_texto_leet = to_leet(mi_texto)
print(mi_texto, ' -> ', mi_texto_leet)
