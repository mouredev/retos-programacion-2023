'''
Crea las funciones capaces de transformar colores HEX
a RGB y viceversa.
Ejemplos:
RGB a HEX: r: 0, g: 0, b: 0 -> #000000
HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
'''

def to_hex(r, g, b):
    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
        r_h = str(hex(r))[2:].upper()
        g_h = str(hex(g))[2:].upper()
        b_h = str(hex(b))[2:].upper()
        
        r_h = r_h if len(r_h) == 2 else '0' + r_h
        g_h = g_h if len(g_h) == 2 else '0' + g_h
        b_h = b_h if len(b_h) == 2 else '0' + b_h
        return '#' + r_h + g_h + b_h
    else:
        return 'Codigo RGB incorrecto'

def to_rgb(hex):
    if hex[0] != '#' or len(hex) != 7:
        return 'Codigo HEX incorrecto'
    else:
        r = int(hex[1:3], 16)
        g = int(hex[3:5], 16)
        b = int(hex[5:7], 16)
        return (r, g, b)

print(to_hex(0, 0, 0))
print(to_hex(255, 255, 255))
print(to_hex(175, 50, 165))

print(to_rgb('#FFFFFF'))
print(to_rgb('#000000'))
print(to_rgb('#AF32A5'))
