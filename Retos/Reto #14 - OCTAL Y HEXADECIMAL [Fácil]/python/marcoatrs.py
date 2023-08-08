def dec2hexa(num: int) -> str:
    replaces = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    hexa = []
    while num > 16:
        hexa.insert(0, replaces.get((num % 16), str((num % 16))))
        num //= 16
    hexa.insert(0, replaces.get(num, str(num)))
    return "".join(hexa)


def dec2oct(num: int) -> str:
    oct = []
    while num > 8:
        oct.insert(0, str(num % 8))
        num //= 8
    oct.insert(0, str(num))
    return "".join(oct)


def convert(num: int):
    return dec2hexa(num), dec2oct(num)


print(convert(19489052815))
