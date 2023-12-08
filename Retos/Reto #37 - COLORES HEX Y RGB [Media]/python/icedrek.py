"""
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)

 Nota: 
    Valores HEX -> 0-9, A-F
    Valores RGB -> 0-255
"""
import re


def main():
    print("OPCION 1 - Convertir HEX a RGB")
    print("   - Valores entre 000000 y FFFFFF")
    print("\nOPCION 2 - Convertir RGB a HEX")
    print("   - Valores entre 0 y 255")
    print("   - Tres valores, separados por comas")

    opcion = input("\nOPCION: ")

    if opcion == "1":
        while True:
            rgbValue = hexToRgb()

            if rgbValue:
                break

        print(f"RGB: {rgbValue}")

    elif opcion == "2":
        while True:
            hexValue = rgbToHex()

            if hexValue:
                break

        print(f"HEX: #{hexValue}")

    else:
        print("Opcion no válida")


def hexToRgb():
    hexValue = input("introduce un valor en formato HEX: #")

    if len(hexValue) != 6:
        print("El código introducido debe tener 6 dígitos")
        return

    for _ in hexValue:
        if not re.match("[0-9a-fA-F]", _):
            print(f"'{_}' no es un caracter valido")
            return

    r = int("0x" + hexValue[:2], 16)
    g = int("0x" + hexValue[2:4], 16)
    b = int("0x" + hexValue[4:6], 16)

    rgbValue = [r, g, b]

    print(f"\nHEX: #{hexValue}")

    return rgbValue


def rgbToHex():
    rgbValue = input(
        "introduce tres numeros enre 0 y 255, separados por espacios: "
    ).split()

    hexValue = ""

    if len(rgbValue) != 3:
        print("introduce TRES numeros separados por espacios!!!")
        return

    for _ in rgbValue:
        if not re.search("\d", _):
            print(f"'{_}' no es numerico")
            return

        if int(_) < 0 or int(_) > 255:
            print(f"'{_}' no esta entre 0 y 255")
            return

        hexValue += ("{:02x}".format(int(_)))

    print(f"RGB: {rgbValue}")

    return str(hexValue).upper()


if __name__ == "__main__":
    main()
