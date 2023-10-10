import locale

def read_abacus_number(abacus: list) -> str:

    if len(abacus) != 7:
        raise Exception("Tamaño total incorrecto")

    number = ""

    for row in abacus:
        if len(row) == 12 and "---" in row and row.replace("---", "") == "OOOOOOOOO":
            number += str(len(row.split("---")[0]))
        else:
            raise Exception("Formato de fila incorrecto")

    return "{:,}".format(int(number)).replace(",", ".")

abacus = ["O---OOOOOOOO",
          "OOO---OOOOOO",
          "---OOOOOOOOO",
          "OO---OOOOOOO",
          "OOOOOOO---OO",
          "OOOOOOOOO---",
          "---OOOOOOOOO"]

# abacus = ["OOOOOOOOO---",
#           "OOOOOOOOO---",
#           "OOOOOOOOO---",
#           "OOOOOOOOO---",
#           "OOOOOOOOO---",
#           "OOOOOOOOO---",
#           "OOOOOOOOO---"]

# abacus = ["---OOOOOOOOO",
#           "---OOOOOOOOO",
#           "---OOOOOOOOO",
#           "---OOOOOOOOO",
#           "---OOOOOOOOO",
#           "---OOOOOOOOO",
#           "---OOOOOOOOO"]

# abacus = ["---OOOOOOOOO",
#           "---OOOOOOOOO",
#           "---OOOOOOOOO",
#           "O---OOOOOOOO",
#           "---OOOOOOOOO",
#           "---OOOOOOOOO",
#           "---OOOOOOOOO"]

print(read_abacus_number(abacus))