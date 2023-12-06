def abaco(tablero: list[str]) -> int:
    respuesta = 0
    for i in range(7):
        temporal = tablero[i].split("-")
        respuesta += len(temporal[0]) * (10 ** (7 - i - 1))
    return respuesta


if __name__ == "__main__":
    tablero = [
        "O---OOOOOOOO",
        "OOO---OOOOOO",
        "---OOOOOOOOO",
        "OO---OOOOOOO",
        "OOOOOOO---OO",
        "OOOOOOOOO---",
        "---OOOOOOOOO",
    ]
    print(abaco(tablero))
