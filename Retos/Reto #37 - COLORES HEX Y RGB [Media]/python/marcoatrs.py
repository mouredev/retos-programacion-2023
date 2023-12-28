def dec2hexa(num: int) -> str:
    replaces = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    hexa = []
    while num > 16:
        hexa.insert(0, replaces.get((num % 16), str((num % 16))))
        num //= 16
    hexa.insert(0, replaces.get(num, str(num)))
    return "".join(hexa)


def rgb2hex(r: int, g: int, b: int) -> str:
    rhex = dec2hexa(r)
    ghex = dec2hexa(g)
    bhex = dec2hexa(b)

    rhex = rhex if len(rhex) == 2 else f"0{rhex}"
    ghex = ghex if len(ghex) == 2 else f"0{ghex}"
    bhex = bhex if len(bhex) == 2 else f"0{bhex}"

    return f"#{rhex}{ghex}{bhex}"


def hex2rgb(he: str) -> tuple:
    he = he.replace("#", "")
    if len(he) != 6:
        print("Formato no compatible")
        return
    r = int(he[:2], 16)
    g = int(he[2:4], 16)
    b = int(he[4:], 16)
    return r, g, b


print(rgb2hex(0, 0, 0))
print(hex2rgb("#00FFFF"))
print(hex2rgb(rgb2hex(0, 255, 128)))
