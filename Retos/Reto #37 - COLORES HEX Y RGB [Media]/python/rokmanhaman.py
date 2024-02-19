"""
Reto #37: COLORES HEX Y RGB
MEDIA | Publicación: 18/09/23 | Resolución: 25/09/23
/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */
"""

def dec_to_hex(number):
    cociente_list = [number // 16]
    resto_list = [number % 16]
    i = 0
    while cociente_list[i] >= 16:
        cociente_list.append(cociente_list[i] // 16)
        resto_list.append(cociente_list[i] % 16)
        i = i + 1

    last_cociente  = cociente_list[i]
    invert_resto = resto_list[::-1]
    hex_values = "0123456789ABCDEF"
    last_cociente_hex = hex_values[last_cociente]
    invert_resto_hex = [hex_values[y] for y in invert_resto]

    resultado_text = str(last_cociente_hex)+ "".join(map(str, invert_resto_hex))

    return resultado_text

def hex_to_dec(number):
    acc = 0
    hex_values = "0123456789ABCDEF"
    
    for i, j in enumerate(number[::-1]):

        acc += hex_values.index(j) * 16**i

    return acc


def hex_to_rgb(hex):

    r = hex_to_dec(hex[0:2])
    g = hex_to_dec(hex[2:4])
    b = hex_to_dec(hex[4:6]) 

    return print(f"\n\nEl color HEX {hex} corresponde al color RGB: ({r},{g},{b})\n\n")



def rgb_to_hex(r,g,b):

    if r >= 0 and r <=255 and g >= 0 and g<=255 and b >= 0 and b <=255:
        rhex = dec_to_hex(r)
        ghex = dec_to_hex(g)
        bhex = dec_to_hex(b)      
    else:
        print( "ingrese valores entre 0 y 255")

    return print(f"\n\nEl color RGB {r}-{g}-{b} corresponde al color hex: #{rhex}{ghex}{bhex}\n\n")


rgb_to_hex(255,210,194)


hex_to_rgb('FFD2C2')



