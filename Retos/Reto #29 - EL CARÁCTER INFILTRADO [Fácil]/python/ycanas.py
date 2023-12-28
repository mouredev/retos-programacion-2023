def check(str1: str, str2: str) -> list:
    undercovers = list()

    if len(str1) == len(str2):
        for index, character in enumerate(str2):
            if not character == str1[index]:
                undercovers.append(character)

    return undercovers


print(check("Me llamo mouredev", "Me llemo mouredov"))
print(check("Me llamo.Brais Moure", "Me llamo brais moure"))
print(check("Me llamo.Brais Moure", "Me llamo brais moure "))
print(check("", ""))
