from typing import List

def leer_abaco(abaco: List[str]) -> int:
    numero = ""
    for linea in abaco:
        if linea.startswith("---"):
            numero += "0"
            continue
        if linea.endswith("---"):
            numero += "9"
            continue
        numero += str(len(linea.split("-")[0]))
    return numero


abaco = ["O---OOOOOOOO",
         "OOO---OOOOOO",
         "---OOOOOOOOO",
         "OO---OOOOOOO",
         "OOOOOOO---OO",
         "OOOOOOOOO---",
         "---OOOOOOOOO"]

print(leer_abaco(abaco))
