def excel(column):
    ALPHABET = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
    if len(column) > 1:
        a_value = len(column[1:]) * 26
        first_value = ALPHABET.index(column[0]) + 1
        return a_value + first_value
    return ALPHABET.index(column) + 1

print(excel("C"))
print(excel("AAA"))
print(excel("BA"))
