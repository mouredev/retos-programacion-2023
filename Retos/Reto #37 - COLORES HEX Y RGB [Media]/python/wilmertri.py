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
        if option == 3:
            break
        elif option == 1:
            color = input("Ingrese el color en HEXADECIMAL: #")
            if len(color) > 6 or len(color) < 6:
                print("No es correcto el color en HEX")
            else:
                color = [color[i:i+2] for i in range(0, len(color), 2)]
                rgb = [str(int(c, 16)) for c in color]
                print("\nRGB: (" + ','.join(rgb) + ")\n")
        elif option == 2:
            color = input("Ingrese el color en RGB separados por comas: ")
            color = color.split(',')
            if len(color) > 3 or len(color) < 3:
                print("No es correcto el color en RGB")
            elif any(int(c) > 255 or int(c) < 0 for c in color):
                print("No tiene valores correctos en el RGB")
            else:
                hexa = [hex(int(c))[2:].upper() for c in color]
                print("\nHEX: #" + ''.join(hexa) + "\n")


convert_colors()