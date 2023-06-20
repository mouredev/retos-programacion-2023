def ConvertToOct(decimal):
    oct_lst = ConversionProcess(decimal, 8)
    return int(ToString(oct_lst))

def ConvertToHex(decimal):
    hex_lst = []
    num_lst = ConversionProcess(decimal, 16)
    for element in num_lst:
        match element:
            case 10: element = 'A'
            case 11: element = 'B'
            case 12: element = 'C'
            case 13: element = 'D'
            case 14: element = 'E'
            case 15: element = 'F'
        hex_lst.append(element)
    return ToString(hex_lst)

def ConvertToBin(decimal):
    bin_lst = ConversionProcess(decimal, 2)
    return (int(ToString(bin_lst)))

def ConversionProcess(decimal, base):
    remainder_lst = []
    while decimal > 0:
        remainder_lst.append(decimal % base)
        decimal //= base
    remainder_lst.reverse()
    return remainder_lst

def ToString(num_lst):
    return (''.join(str(x) for x in num_lst))

def main():
   decimal = int(input('Enter a decimal number: '))
   print(f'Octal: {ConvertToOct(decimal)}')
   print(f'Hexadecimal: {ConvertToHex(decimal)}')
   print(f'Binary: {ConvertToBin(decimal)}')
   

main()