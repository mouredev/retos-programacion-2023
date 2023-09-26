def rgb_to_hex(r,g,b):
    
    red_hex = hex(r)
    green_hex = hex(g)
    blue_hex = hex(b)
    
    red_hex = str(red_hex)
    green_hex = str(green_hex)
    blue_hex = str(blue_hex)
    red_hex = red_hex.replace("0x","")
    
    if len(red_hex)<2:
        red_hex = "0"+red_hex
    
    
    green_hex = green_hex.replace("0x","")
    
    if len(green_hex) <2:
        green_hex = "0"+green_hex
    
    blue_hex  = blue_hex.replace("0x","")
    
    if len(blue_hex)<2:
        blue_hex = "0"+blue_hex
    
    return "#" + red_hex + green_hex+blue_hex

def hex_to_rgb(hex):
    
    hex_value = str(hex)
    
    hex_value = hex_value.replace("#","")
    
    red_value = hex_value[0:2]
    red_value = int(red_value,16)
  
    green_value = hex_value[2:4]
    green_value = int(green_value,16)
      
    blue_value = hex_value[4:]
    blue_value = int(blue_value,16)
    tuple = (red_value,green_value,blue_value)
    return tuple


print(rgb_to_hex(17,115,200))

print(hex_to_rgb("#1773C8"))  