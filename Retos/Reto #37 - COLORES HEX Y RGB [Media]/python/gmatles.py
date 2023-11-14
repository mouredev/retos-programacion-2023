# Convertidor hex - rgb

import re


def convertir(color):
    if isinstance(color, tuple):
        if not (isinstance(color[0], int) and
                isinstance(color[1], int) and
                isinstance(color[2], int)
                ):
            return "El color RGB ingresado es invalido."

        if not (0 <= color[0] <= 255 and
                0 <= color[1] <= 255 and
                0 <= color[2] <= 255
                ):
            return "El color RGB ingresado es invalido."

        resultado = ("#" +
                     str(hex(color[0]))[2:].zfill(2) +
                     str(hex(color[1]))[2:].zfill(2) +
                     str(hex(color[2]))[2:].zfill(2)
                     ).upper()

    elif isinstance(color, str):
        if not (re.match("#[a-fA-F0-9]{6}+$", color)):
            return "El color HEX ingresado es invalido."

        resultado = (int(color[1:3], base=16),
                     int(color[3:5], base=16),
                     int(color[5:7], base=16)
                     )

    return resultado


# Probando conversiones

print(convertir("#000000"))
print(convertir("#FFFFFF"))
print(convertir((0, 0, 0)))
print(convertir((255, 255, 255)))

# Probando errores

print(convertir("000000"))
print(convertir("1000000"))
print(convertir("$000000"))
print(convertir("#0000000"))
print(convertir("#G00000"))
print(convertir("#0G0000"))
print(convertir("#00G000"))
print(convertir("#000G00"))
print(convertir("#0000G0"))
print(convertir("#00000G"))

print(convertir((256, 255, 255)))
print(convertir((255, 256, 255)))
print(convertir((255, 255, 256)))
print(convertir(("a", 255, 255)))
print(convertir((255, "a", 255)))
print(convertir((255, 255, "a")))
