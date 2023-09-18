def hex_to_rgb(hex):
  rgb = []
  for i in (0, 2, 4):
    decimal = int(hex[i:i+2], 16)
    rgb.append(decimal)
  
  return f"#{hex} -> rgb{tuple(rgb)}"


def rgb_to_hex(r, g, b):
    return 'rgb({},{},{}) -> #{:02x}{:02x}{:02x}'.format(r, g, b, r, g, b)


print(hex_to_rgb('FF5733'))
print(rgb_to_hex(255, 87, 51))