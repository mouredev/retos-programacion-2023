def rgb_to_hex(r, g, b):
    return "#{:02X}{:02X}{:02X}".format(r, g, b)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return "r: {}, g: {}, b: {}".format(r, g, b)

# rgb_to_hex
r, g, b = 250, 186, 218
hex_color = rgb_to_hex(r, g, b)
print(hex_color)  # Imprime "#000000"

# hex_to_rgb
hex_color = "#fabada"
rgb_color = hex_to_rgb(hex_color)
print(rgb_color)  # Imprime "r: 0, g: 0, b: 0"
