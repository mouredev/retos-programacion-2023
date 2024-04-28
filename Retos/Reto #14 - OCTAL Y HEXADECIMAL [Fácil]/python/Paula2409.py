"""
/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */
 """
def octal_hexadecimal(number):
    table_hexa = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
    number_octal,number_hexa = number,number
    result_octal, result_hexa = [],[]
    
    ''' Calculate Octal number'''
    while number_octal > 0:
        result_octal.append(str(number_octal % 8))
        number_octal = number_octal // 8

    octal = "".join(result_octal[::-1])

    ''' Another way to return '''
    # for digit in result_octal[::-1]:
    #     octal += str(digit)

    '''Calculate Hexadecimal number '''
    while number_hexa > 0:
        if str(number_hexa % 16) in table_hexa:
            result_hexa.append(table_hexa[str(number_hexa % 16)])
        else:
            result_hexa.append(str(number_hexa % 16))        
        number_hexa = number_hexa // 16

    hexadecimal = "".join(result_hexa[::-1]) 
    
    if number == 0:
        octal,hexadecimal = 0,0
    return f"The number {number} in octal is: {octal} and in hexadecimal is: {hexadecimal}"

print(octal_hexadecimal(0))
print(octal_hexadecimal(100))
print(octal_hexadecimal(1000))