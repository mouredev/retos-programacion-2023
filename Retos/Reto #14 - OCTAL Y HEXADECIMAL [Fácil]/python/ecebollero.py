def decToHex(n):
    
    hexadecimals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','A', 'B', 'C', 'D', 'E', 'F']
    hex = ''
    
    while n > 0:
        quotient, rest = divmod(n,16)
        hex = hexadecimals[rest] + hex
        n = quotient

    return hex
        
def decToOct(n):
    
    octals = ['0', '1', '2', '3', '4', '5', '6', '7']
    oct = ''

    while n > 0:
        quotient, rest = divmod(n,8)
        oct = octals[rest] + oct
        n = quotient
    
    return oct 

if __name__ == '__main__':
    
    number = input('Enter a decimal number to transform it to Hex and Oct: ')
    
    try:
        n = int(number)
        print(f'The number {n} in hexadecimal is {decToHex(n)}')
        print(f'The number {n} in octal is {decToOct(n)}')
    except ValueError:
        print("That's not a number")
    
