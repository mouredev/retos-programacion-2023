import re

def hex_to_rgb(hex: str) -> tuple:

    hex = hex.lstrip("#")

    regex = re.compile(r"^[0-9a-fA-F]{6}$")
    if regex.match(hex):

        r = int(hex[0:2], 16)
        g = int(hex[2:4], 16)
        b = int(hex[4:6], 16)

        return (r, g, b)
    
    return (0, 0, 0)

def rgb_to_hex(r: int, g: int, b: int) -> str:

    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    return f"#{r:02x}{g:02x}{b:02x}"

print(hex_to_rgb("#ffffff"))
print(hex_to_rgb("ffffff"))
print(hex_to_rgb("#000000"))
print(hex_to_rgb("#fabada"))
print(hex_to_rgb("#cagada"))
print(hex_to_rgb("#fffffff"))
print(hex_to_rgb("#fffff"))

print(rgb_to_hex(0, 0, 0))
print(rgb_to_hex(255, 255, 255))
print(rgb_to_hex(250, 186, 218))
print(rgb_to_hex(255, 255, -5))