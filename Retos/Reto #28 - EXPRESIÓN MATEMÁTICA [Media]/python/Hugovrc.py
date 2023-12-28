import re

def comprobar_matematica(expresion: str):
    #expresion_matematica = (r"((\d+[.]\d|\d|\-\d)\s*(\+|\-|\*|\/|\%)?\s*){1,}")
    expresion_matematica = (r"((\d+[.]\d|\d|\-\d)\s?((\+|\-|\*|\/|\%)\s)?){1,}")
    #expresion_matematica = "^(\d+[.]\d|\d|\-\d) [\+|-|*|/|%] (\d+[.]\d|\d|\-\d)"
    result = re.fullmatch(expresion_matematica, expresion)

    if result:
        return True
    else:
        return False


print(comprobar_matematica("-5 + 5.9 / 10 a 13 * 15"))
print(comprobar_matematica("-5 + 5.9 / 10.0 % 13 * 90"))
print(comprobar_matematica("-5 p -89"))
print(comprobar_matematica("-5 - -89"))