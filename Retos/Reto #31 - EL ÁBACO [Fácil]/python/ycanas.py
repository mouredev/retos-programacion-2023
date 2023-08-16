def abaco(sequence: list) -> int:
    if not len(sequence) == 7:
        raise Exception("Error")
    
    output = 0
    length = len(sequence) - 1

    for index, item in enumerate(sequence):
        if len(item) == 12 and "---" in item and item.replace("---", '') == "OOOOOOOOO":
            number = len(item.split("---")[0])
            output = output + (number * (10 ** length // 10 ** index))

    return output
    
    
print(abaco(["O---OOOOOOOO", "OOO---OOOOOO", "---OOOOOOOOO", "OO---OOOOOOO", "OOOOOOO---OO", "OOOOOOOOO---", "---OOOOOOOOO"]))
