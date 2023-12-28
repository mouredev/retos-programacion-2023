abaco = [
    "O---OOOOOOOO",
    "OOO---OOOOOO",
    "---OOOOOOOOO",
    "OO---OOOOOOO",
    "OOOOOOO---OO",
    "OOOOOOOOO---",
    "---OOOOOOOOO"
]

multiplo = 100000
cuenta = 0

for linea in abaco:
    linea = linea[0:linea.index("-")]
    cuenta += len(linea) * multiplo
    multiplo /= 10
    
print(int(cuenta))