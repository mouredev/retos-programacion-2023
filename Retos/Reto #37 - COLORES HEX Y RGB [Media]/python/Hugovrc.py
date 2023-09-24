def hex_a_rgb(valor: str) -> str:

    # Descartamos el #
    valor_hex = valor[1:7]
    # covertimos el primer par
    r = str(int(valor_hex[0:2],16))
    # covertimos el segundo par
    g = str(int(valor_hex[2:4],16))
    # covertimos el tercer par
    b = str(int(valor_hex[4:6],16))
    
    return f"HEX a RGB: R:{r}, G:{g}, B:{b}"

def rgb_a_hex(r: str, g: str, b:str) -> str:
    valor_r = hex(int(r))[2:4]
    if len(valor_r) == 1:
        valor_r = "0"+valor_r
    else:
        valor_r = hex(int(r))[2:4]
    valor_g = hex(int(g))[2:4]
    if len(valor_g) == 1:
        valor_g = "0"+valor_g
    else:
        valor_g = hex(int(g))[2:4]
    valor_b = hex(int(b))[2:4]
    if len(valor_b) == 1:
        valor_b = "0"+valor_b
    else:
        valor_b = hex(int(b))[2:4]    

    return f"RGB a HEX: #{valor_r.upper()}{valor_g.upper()}{valor_b.upper()}"

print(hex_a_rgb("#000000"))
print(rgb_a_hex("0", "0", "0"))

print(hex_a_rgb("#ABCDEF"))
print(rgb_a_hex("171","205","239"))