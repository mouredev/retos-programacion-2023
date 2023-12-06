def abaco(table: list[str]) -> str:
    num = 0
    
    for i in range(7):
        division = table[i].split("-")
        num += len(division[0]) * (10 ** (7 - i -1))
    
    num_str = "{:,}".format(num).replace(",", ".")
    print(num_str)


abaco(["O---OOOOOOOO",
        "OOO---OOOOOO",
        "---OOOOOOOOO",
        "OO---OOOOOOO",
        "OOOOOOO---OO",
        "OOOOOOOOO---",
        "---OOOOOOOOO"])
