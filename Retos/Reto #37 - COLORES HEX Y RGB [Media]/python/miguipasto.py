# Crea las funciones capaces de transformar colores HEX
# a RGB y viceversa.
# Ejemplos:
# RGB a HEX: r: 0, g: 0, b: 0 -> #000000
# HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)

def dec_to_hex(decimal: int):
    lista_hexadecimal = '0123456789ABCDEF'
    resto_1 = decimal % 16
    resto_2 = (decimal // 16) % 16
    hexadecimal = lista_hexadecimal[resto_2] + lista_hexadecimal[resto_1]
    return hexadecimal

def RGB_to_HEX(red: int, green: int, blue: int):
    hexadecimal_red = dec_to_hex(red)
    hexadecimal_green = dec_to_hex(green)
    hexadecimal_blue = dec_to_hex(blue)
    hexadecimal = f'#{hexadecimal_red}{hexadecimal_green}{hexadecimal_blue}'
    return hexadecimal

def hex_to_dec(hexadecimal: str):
    hexadecimal = hexadecimal.lstrip('#')
    decimal = int(hexadecimal, 16)
    return decimal

def HEX_to_RGB(hexadecimal: str):
    decimal = hex_to_dec(hexadecimal)
    red = (decimal >> 16) & 255
    green = (decimal >> 8) & 255
    blue = decimal & 255
    return f'(r: {red}, g: {green}, b: {blue})'

# Ejemplos de uso
rgb_color = RGB_to_HEX(50, 0, 0)
print(f'RGB a HEX: r: 50, g: 0, b: 0 -> {rgb_color}')

hex_color = HEX_to_RGB('#802000')
print(f'HEX a RGB: hex: #802000 -> {hex_color}')
