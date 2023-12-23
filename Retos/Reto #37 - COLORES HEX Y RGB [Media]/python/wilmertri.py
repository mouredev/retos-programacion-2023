'''
    Crea las funciones capaces de transformar colores HEX
    a RGB y viceversa.
    Ejemplos:
    RGB a HEX: r: 0, g: 0, b: 0 -> #000000
    HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
'''


def convert_colors():
    while True:
        print("Seleccione una opción: \n1. Convertir de HEX a RGB\n2. Convertir de RGB a HEX\n3. Salir")
        option = int(input("Elija una opción: "))
        match option:
            case 3:
                break
            case 1:
                color = input("Ingrese el color en HEXADECIMAL: #")
                print(hex_to_rgb(color))
            case 2:
                color = input("Ingrese el color en RGB separados por comas: ")
                print(rgb_to_hex(color))


def hex_to_rgb(color) -> str:
    if len(color) != 6:
        message = "\nNo es correcto el color en HEX\n"
    else:
        color = [color[i:i + 2] for i in range(0, len(color), 2)]
        rgb = [str(int(c, 16)) for c in color]
        message = "\nRGB: (" + ','.join(rgb) + ")\n"

    return message


def rgb_to_hex(color) -> str:
    color = color.split(',')
    if len(color) != 3:
        message = "\nNo es correcto el color en RGB\n"
    elif any(int(c) > 255 or int(c) < 0 for c in color):
        message = "\nNo tiene valores correctos en el RGB\n"
    else:
        hexa = [hex(int(c))[2:].upper() for c in color]
        hexa = ['0' + h if len(h) == 1 else h for h in hexa]
        message = "\nHEX: #" + ''.join(hexa) + "\n"

    return message


convert_colors()