def analizar_expresion(expresion: str) -> bool:
    simbolos = "+-*/%"
    expresion = expresion.split()
    for i in range(len(expresion)):
        if i % 2 == 0:
            try:
                numero = int(expresion[i])
            except:
                return False
        else:
            if not expresion[i] in simbolos:
                return False
    return True


if __name__ == "__main__":
    expresion = input("Introducir la expresion a analizar: ")
    res = "true" if analizar_expresion(expresion) else "false"
    print("Es una expresion valida? " + res)
