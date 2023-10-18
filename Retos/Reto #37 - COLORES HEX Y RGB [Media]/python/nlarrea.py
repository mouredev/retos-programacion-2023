"""
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
"""

from re import findall, search

def from_hexa_to_rgb(color: str):
    # Check if given color is in hexadecimal
    if (
        not type(color) == str or
        not "#" in color or
        (len(color) != 4 and len(color) != 7)
    ):
        return "This is not in a correct hexadecimal format."
    elif search(r"[^#0-9a-f]", color.lower()):
        return "Hexadecimal only contains digits from 0-9 and A-F."

    # Get the RGB value
    def hexa_to_int(hexa):
        return int(hexa, base=16)
    
    [r, g, b] = list(map(lambda item: hexa_to_int(item), findall(r".{2}", color[1:])))
    return {"r": r, "g": g, "b": b}


def from_rgb_to_hexa(rgb: dict):
    r, g, b = rgb["r"], rgb["g"], rgb["b"]

    # Check if given color is RGB
    def in_range(number:int): return number >= 0 and number <= 255

    if len(rgb) != 3:
        return "You must enter values for all RGB colors."
    elif type(r) != int or type(g) != int or type(b) != int:
        return "You must enter int values."
    elif (not in_range(r) or not in_range(g) or not in_range(b)):
        return "Numbers must be between 0-255."

    # Get the hexadecimal value
    def int_to_hexa(integer: int):
        return "%02x" % integer

    return f"#{int_to_hexa(r)}{int_to_hexa(g)}{int_to_hexa(b)}"


print(from_hexa_to_rgb("#000000"))                          # { r: 0, g: 0, b: 0 }
print(from_hexa_to_rgb("#ffd486"))                          # { r: 255, g: 212, b: 134 }
print(from_rgb_to_hexa({"r": 0, "g": 0, "b": 0}))           # #000000
print(from_rgb_to_hexa({"r": 110, "g": 235, "b": 131}))     # #6eeb83