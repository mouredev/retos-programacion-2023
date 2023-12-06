
def characters(first, second):
    char = []
    if len(first) == len(second):
        for index in range(0, len(first)):
            if first[index] != second[index]:
                char.append(second[index])

    return char

print(characters("anita lava la tina", "anito lavo la tina"))
