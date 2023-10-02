signos_permitidos = "0123456789+-/*% "
parejas_invalidas = ["*/", "/*", "%/", "/%", "*%", "%*", "%%", "+/", "-/"]


def expresion_matematica(expresion: str) -> bool:
    # Caracter invalido
    for c in expresion:
        if c not in signos_permitidos:
            return False
    # Signos dobles
    expresion = expresion.replace(" ", "")
    for par in parejas_invalidas:
        if par in expresion:
            return False
    return True

print(expresion_matematica("2 + 4"))
print(expresion_matematica("2 + /4"))
print(expresion_matematica("2 +y 4"))
