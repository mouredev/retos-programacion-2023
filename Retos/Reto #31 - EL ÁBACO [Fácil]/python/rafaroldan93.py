array_prueba = ["O---OOOOOOOO",
                "OOO---OOOOOO",
                "---OOOOOOOOO",
                "OO---OOOOOOO",
                "OOOOOOO---OO",
                "OOOOOOOOO---",
                "---OOOOOOOOO"]

print("".join(list(map(lambda fila: str(fila.find("-")), array_prueba))))