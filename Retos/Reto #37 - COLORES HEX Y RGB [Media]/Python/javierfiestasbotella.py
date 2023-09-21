'''
/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */
'''
def rgb_a_hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def hex_a_rgb(hex_color):  
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return (r, g, b)

#ejemplo
print(rgb_a_hex(0, 0, 0))
print(hex_a_rgb('#000000'))