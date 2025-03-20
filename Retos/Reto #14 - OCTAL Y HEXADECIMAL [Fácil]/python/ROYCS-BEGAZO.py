
def init(number: int):
    hexa = convertion(number, 16)
    octal = convertion(number, 8)
    return  f'el numero {number} en octa es {octal} \n y en hexadecimal es {hexa}'

def convertion(number: int, r : int)-> str:
    hex_values = "0123456789ABCDEF"
    convert = ''
    while True:
        if r == 16:
           convert = hex_values[number % r] + convert
        else:
            convert = str(number % r) + convert
        number //= r
        if number == 0:
            break
    return convert

print(init(12222))


