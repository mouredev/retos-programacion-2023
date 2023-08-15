def abaco(num: list) -> str:
    num_dec = ""

    for numero in num:
        indice = numero.split("---")
        num_dec += str(len(indice[0]))
        if len(num_dec)== 1:
            num_dec += "."
        if len(num_dec)== 5:
            num_dec += "."
    return num_dec

print(abaco(["O---OOOOOOOO",
             "OOO---OOOOOO",
             "---OOOOOOOOO",
             "OO---OOOOOOO",
             "OOOOOOO---OO",
             "OOOOOOOOO---",
             "---OOOOOOOOO"]))

print(abaco(["OO---OOOOOOO",
             "OOO---OOOOOO",
             "OOOOO---OOOO",
             "---OOOOOOOOO",
             "OOOOO---OOOO",
             "OOOOOOO---OO",
             "---OOOOOOOOO"]))

print(abaco(["---OOOOOOOOO",
             "O---OOOOOOOO",
             "---OOOOOOOOO",
             "OO---OOOOOOO",
             "OOOOOOO---OO",
             "OOOOOOOOO---",
             "OOOOO---OOOO"]))