abaco = ["O---OOOOOOOO",
    "OOO---OOOOOO",
    "---OOOOOOOOO",
    "OO---OOOOOOO",
    "OOOOOOO---OO",
    "OOOOOOOOO---",
    "---OOOOOOOOO"]

valores = []
for seccion in abaco:
    cuenta_antes_del_alambre = seccion.count('O', 0, seccion.index('---'))
    valores.append(cuenta_antes_del_alambre)

numero_completo = int(''.join(map(str, valores)))
print("Número representado por el ábaco:", numero_completo)
