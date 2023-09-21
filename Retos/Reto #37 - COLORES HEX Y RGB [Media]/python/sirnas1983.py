def rgb_to_hex_converter(r,g,b) -> int:
    try:
        if 0<=r<=255 and 0<=g<=255 and 0<=b<=255:  
            r = str(hex(r))[2:].rjust(2,'0') 
            g = str(hex(g))[2:].rjust(2,'0') 
            b = str(hex(b))[2:].rjust(2,'0') 
            return "#" + r + g + b
        else:
            raise ValueError("r, g and b must be in 0-255 range")
    except:
        raise TypeError("r, g and b must be integers between 0 and 255")
    
def hex_to_rgb_converter(hex_color: str | int) -> (int, int, int):
    try:
        hex_color = str(hex_color)
        r = int(hex_color[-6:-4],16)
        g = int(hex_color[-4:-2],16)
        b = int(hex_color[-2:],16)
        if 0<=r<=255 and 0<=g<=255 and 0<=b<=255:  
            return r, g, b    
        else:
            raise ValueError("Hex color out of range")
    except:
        raise TypeError("Invalid HEX color")
