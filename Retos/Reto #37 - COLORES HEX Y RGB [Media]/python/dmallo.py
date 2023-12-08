"""
Crea las funciones capaces de transformar colores HEX a RGB y viceversa.
Ejemplos:
RGB a HEX: r: 0, g: 0, b: 0 -> #000000
HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
"""

def dec_to_hex(number: int) -> str:

    hex = {0 : "0", 1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8",
           9 : "9", 10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F"}

    for _ in hex:
        if _ == number:
            number = hex[number]
    
    return number


def hex_to_dec(hex: str) -> list:

    dec = {"0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8,
           "9" : 9, "A" : 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15}

    xy = []

    for a in dec:
        for index, b in enumerate(hex):
            if b == a:
                xy.append(dec[a])                
    
    return xy


def rgb_to_hex(r: int, g: int, b: int):
    
    r1 = r // 16
    x1 = dec_to_hex(r1)
    r2 = r % 16
    y1 = dec_to_hex(r2)
    red = x1 + y1

    g1 = g // 16
    x2 = dec_to_hex(g1)
    g2 = g % 16
    y2 = dec_to_hex(g2)
    green = x2 + y2
    
    b1 = b // 16
    x3 = dec_to_hex(b1)
    b2 = b % 16
    y3 = dec_to_hex(b2)
    blue = x3 + y3
    
    print(f"R: {r}, G: {g}, B: {b} -> #{red}{green}{blue}")


def hex_to_rgb(nun_hex: str):

    clean_hex = nun_hex.split("#")
    hex = clean_hex[1]

    red = hex[:2]
    x1y1 = hex_to_dec(red)
    r = (x1y1[1] * 16**1) + (x1y1[0] * 16**0)

    green = hex[2:4]
    x2y2 = hex_to_dec(green)
    g = (x2y2[1] * 16**1) + (x2y2[0] * 16**0)

    blue = hex[4:6]
    x3y3 = hex_to_dec(blue)
    b = (x3y3[1] * 16**1) + (x3y3[0] * 16**0)
    
    print(f"{nun_hex} -> R: {r}, G: {g}, B:{b}")

print("\n*************** RGB to HEX ***************\n")
rgb_to_hex(0, 0, 0)       # Black
rgb_to_hex(255, 255, 255) # White
rgb_to_hex(255, 0, 0)     # Red
rgb_to_hex(0, 255, 0)     # Lime
rgb_to_hex(0, 0, 255)     # Blue
rgb_to_hex(255, 255, 0)   # Yellow
rgb_to_hex(0, 255, 255)   # Cyan
rgb_to_hex(255, 0, 255)   # Magenta
rgb_to_hex(192, 192, 192) # Silver
rgb_to_hex(128, 128, 128) # Gray
rgb_to_hex(128, 0, 0)     # Maroon
rgb_to_hex(128, 128, 0)   # Olive
rgb_to_hex(0, 128, 0)     # Green
rgb_to_hex(128, 0, 128)   # Purple
rgb_to_hex(0, 128, 128)   # Teal
rgb_to_hex(0, 0, 128)     # Navy

print("\n*************** HEX to RGB ***************\n")
hex_to_rgb("#000000")
hex_to_rgb("#FFFFFF")
hex_to_rgb("#FF0000")
hex_to_rgb("#00FF00")
hex_to_rgb("#0000FF")
hex_to_rgb("#FFFF00")
hex_to_rgb("#00FFFF")
hex_to_rgb("#FF00FF")
hex_to_rgb("#C0C0C0")
hex_to_rgb("#808080")
hex_to_rgb("#800000")
hex_to_rgb("#808000")
hex_to_rgb("#008000")
hex_to_rgb("#800080")
hex_to_rgb("#008080")
hex_to_rgb("#000080")
