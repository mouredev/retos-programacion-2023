def infiltrated_characters(first_text: str, second_text:str) -> list:

    characters = []

    if len(first_text) == len(second_text):
        for index in range(0, len(first_text)):
            if first_text[index] != second_text[index]:
                characters.append(second_text[index])

    return characters

print(infiltrated_characters("Me llamo mouredev", "Me llemo mouredov"))
print(infiltrated_characters("Me llamo.Brais Moure", "Me llamo brais moure"))
print(infiltrated_characters("Me llamo.Brais Moure", "Me llamo brais moure "))
print(infiltrated_characters("", ""))