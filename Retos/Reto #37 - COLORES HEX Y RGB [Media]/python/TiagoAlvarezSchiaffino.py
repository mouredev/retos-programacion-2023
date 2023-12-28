import re

def rgb_to_hex(r, g, b):
    """
    Convert RGB values to HEX color.

    Parameters:
    - r (int): Red value (0 to 255).
    - g (int): Green value (0 to 255).
    - b (int): Blue value (0 to 255).

    Returns:
    - str: HEX color representation.
    """
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    return "#{:02X}{:02X}{:02X}".format(r, g, b)

def hex_to_rgb(hex_color):
    """
    Convert HEX color to RGB values.

    Parameters:
    - hex_color (str): HEX color representation.

    Returns:
    - tuple: RGB values (r, g, b).
    """
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return r, g, b

def validate_hex(hex_value):
    """
    Validate if the given string is a valid HEX color.

    Parameters:
    - hex_value (str): HEX color representation.

    Returns:
    - bool: True if the format is valid, False otherwise.
    """
    regex = re.compile(r"^[0-9a-fA-F]{6}$")
    return bool(regex.match(hex_value))

def convert_rgb_hex(r, g, b):
    """
    Convert RGB values to HEX and display the result.

    Parameters:
    - r (int): Red value (0 to 255).
    - g (int): Green value (0 to 255).
    - b (int): Blue value (0 to 255).

    Returns:
    - str: Conversion result string.
    """
    hex_color = rgb_to_hex(r, g, b)
    return f"RGB to HEX: r: {r}, g: {g}, b: {b} -> {hex_color}"

def convert_hex_rgb(hex_color):
    """
    Convert HEX color to RGB and display the result.

    Parameters:
    - hex_color (str): HEX color representation.

    Returns:
    - str: Conversion result string.
    """
    if validate_hex(hex_color):
        rgb_values = hex_to_rgb(hex_color)
        return f"HEX to RGB: hex: {hex_color} -> (r: {rgb_values[0]}, g: {rgb_values[1]}, b: {rgb_values[2]})"
    else:
        return "Invalid HEX color format."

# Example
print(convert_rgb_hex(255, 210, 194))
print(convert_hex_rgb('FFD2C2'))
