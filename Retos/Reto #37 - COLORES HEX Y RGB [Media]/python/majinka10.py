#Tabla de conversion. 
#La clave corresponde a su conversión en decimal y el valor a hexadecimal.
conversion={0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 
            9:9, 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

valores = list(conversion.values()) # Consigo los valores de la tabla para trabajar
# con ellos facilmente luego

# Conversión de HEX a RGB

def HEX2RGB(hex:str):
    """
    Transforma un color HEX a RGB.
    
    Args:
    - hex (str): Color en formato HEX a convertir.
    Returns: 
    - rgb (list): Lista con el valor de cada uno de los canales (red, blue, green).
    """

    # Obtengo los valores hex correspondientes a cada canal.
    red = hex[1:3]
    green =  hex[3:5]
    blue = hex[5:]

    rgb = [] # Inicializo una lista vacía que guardará el valor decimal de cada color.

    # En el siguiente for se itera cada valor hexagecimal de cada canal.
    for hexa in red, green, blue:

        # Esta super linea lo que hace es iterar en hexa (valor hexagecimal) y luego 
        # obtiene el valor decimal de la tabla de conversión, lo multiplica por 16 elevado 
        # al indice (proceso de conversión de hexagecimal a decimal) y por ultimo lo agrega a la lista rgb.
        rgb.append(sum((valores.index(valor) if valor in valores else valor.index(str(valor))) * 16 ** i for i, valor in enumerate(hexa[::-1])))
    
    return rgb
    
ejemplo_hex = '#000000'
color_rgb = HEX2RGB(ejemplo_hex)
print(f"r: {color_rgb[0]}, g: {color_rgb[1]}, b: {color_rgb[2]}")

# Conversión de RGB a HEX

def RGB2HEX(red:int, green:int, blue:int):
    """
    Transforma un color RGB a HEX.

    Args: 
    - red (int): Valor del canal rojo.
    - green (int): Valor del canal verde.
    - blue (int): Valor del canal azul.
    Returns: 
    - hexadecimal (str): Color en formato HEX.
    """

    hexadecimal = '#'

    for decimal in red, green, blue:
        hexadecimal += str(hex(decimal)[2:])
    
    return hexadecimal

ejemplo_rgb = [0, 0, 0]
color_hex = RGB2HEX(ejemplo_rgb[0], ejemplo_rgb[1], ejemplo_rgb[2])
print(color_hex)
