
def read_abaco(abaco):
    multiplicador = 1000000
    sum = 0
    for i in abaco:
        abaco_number = i.split('---')[0]
        sum = sum + multiplicador*len(abaco_number)
        multiplicador /= 10
    return int(sum)
        
        
if __name__ == "__main__":
    combinaciones = [
        "O---OOOOOOOO",
        "OOO---OOOOOO",
        "---OOOOOOOOO",
        "OO---OOOOOOO",
        "OOOOOOO---OO",
        "OOOOOOOOO---",
        "---OOOOOOOOO",
    ]
    print(read_abaco(combinaciones))