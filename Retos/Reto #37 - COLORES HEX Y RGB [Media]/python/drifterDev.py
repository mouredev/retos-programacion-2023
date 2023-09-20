def hex_a_rgb(hex: str) -> str:
    componente_1 = str(int(hex[1:3], 16))
    componente_2 = str(int(hex[3:5], 16))
    componente_3 = str(int(hex[5:7], 16))
    resultado = [
        "(r: ",
        componente_1,
        ", g: ",
        componente_2,
        ", b: ",
        componente_3,
        ")",
    ]
    return "".join(resultado)


def rgb_a_hex(r: int, g: int, b: int) -> str:
    componente_1 = format(r, "02X")
    componente_2 = format(g, "02X")
    componente_3 = format(b, "02X")
    return "#" + componente_1 + componente_2 + componente_3


def main():
    print("Funcion para pasar de RGB a HEX")
    print(rgb_a_hex(0, 0, 0))
    print(rgb_a_hex(34, 139, 34))
    print(rgb_a_hex(0, 128, 255))
    print(rgb_a_hex(255, 255, 0))
    print(rgb_a_hex(255, 0, 128))
    print("Funcion para pasar de HEX a RGB")
    print(hex_a_rgb("#000000"))
    print(hex_a_rgb("#228B22"))
    print(hex_a_rgb("#0080FF"))
    print(hex_a_rgb("#FFFF00"))
    print(hex_a_rgb("#FF0080"))


if __name__ == "__main__":
    main()
