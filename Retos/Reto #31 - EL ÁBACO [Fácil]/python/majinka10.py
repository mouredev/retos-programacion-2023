def leer_abaco(abaco):
    numero=[]
    for number in abaco:
        numero_elemento=0
        for item in number:
            if item == 'O':
                continue
            else:
                numero_elemento=number.index(item)
        numero.append(numero_elemento)
    print("".join(str(_) for _ in numero))

leer_abaco(["O---OOOOOOOO","OOO---OOOOOO","---OOOOOOOOO","OO---OOOOOOO","OOOOOOO---OO","OOOOOOOOO---","---OOOOOOOOO"])
leer_abaco(["O---OOOOOOOO","OOO---OOOOOO","---OOOOOOOOO","OO---OOOOOOO","OOOOOOO---OO","OOOOOOOOO---"])
leer_abaco(["---OOOOOOOOO","---OOOOOOOOO","---OOOOOOOOO","OOO---OOOOOO"])