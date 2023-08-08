def ReadAbaco(abaco,delimiter):
    Total = 0
    abac_count = len(abaco)

    for i, x in enumerate(abaco):
        i = (abac_count - i) - 1
        str_1 = x.split(delimiter)[0]
        count = len(str_1)
        Total += (10**i) * count

    return Total
def main():
    print("\n")

    abaco_1 = ["O---OOOOOOOO",
    "OOO---OOOOOO",
    "---OOOOOOOOO",
    "OO---OOOOOOO",
    "OOOOOOO---OO",
    "OOOOOOOOO---",
    "---00OOOOOOO"]
    delimiter = "---"
    response = ReadAbaco(abaco_1,delimiter)
    print(f"Resultado: {response}")

    print("\n")
if __name__ == '__main__':
    main()
