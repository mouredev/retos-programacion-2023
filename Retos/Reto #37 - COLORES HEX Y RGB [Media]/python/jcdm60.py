# Reto #37: Colores HEX y RGB
#### Dificultad: Media | Publicación: 18/09/23 | Corrección: 25/09/23

## Enunciado


#
# Crea las funciones capaces de transformar colores HEX
# a RGB y viceversa.
# Ejemplos:
# RGB a HEX: r: 0, g: 0, b: 0 -> #000000
# HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
#

class ColorConverter:
    @staticmethod
    def rgb_to_hex(rgb_color):
        r, g, b = rgb_color
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))
        hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
        return hex_color

    @staticmethod
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip("#")
        try:
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)
            return (r, g, b)
        except ValueError:
            raise ValueError("Formato de color HEX no válido")


if __name__ == "__main__":
    converter = ColorConverter()

    rgb_color = (215, 40, 40)
    hex_color = converter.rgb_to_hex(rgb_color)
    print("RGB a HEX:", hex_color)

    hex_color = "#f57e00"
    rgb_color = converter.hex_to_rgb(hex_color)
    print("HEX a RGB:", rgb_color)