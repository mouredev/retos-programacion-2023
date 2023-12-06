def read_abacus_str(abacus_list: list):
    
    abacus_number = ""
    for line in abacus_list:
        num = str(len(line.split("-")[0]))
        abacus_number = abacus_number + num
    abacus_number = int(abacus_number)
    
    return abacus_number

if __name__ == "__main__":
    
    abacus_list = [
        "O---OOOOOOOO",
        "OOO---OOOOOO",
        "---OOOOOOOOO",
        "OO---OOOOOOO",
        "OOOOOOO---OO",
        "OOOOOOOOO---",
        "---OOOOOOOOO"]
    abacus_number = read_abacus_str(abacus_list)
    print(abacus_number)