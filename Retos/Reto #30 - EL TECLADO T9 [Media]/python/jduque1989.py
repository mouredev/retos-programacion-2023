# T9 dictionary

t9_mapping = {
    1: ['.', ','],
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y', 'Z'],
    0: [' '],
    '*': ['+', '-', '*', '/'],
    '#': ['?', '!', '@']
}


def t9_to_letters(t9_number):
    length = len(t9_number) - 1
    index = int(t9_number[0])
    letter = t9_mapping[index][length]
    return letter


Entrada = "6-666-88-777-33-3-33-888"  # 666-666-88-777-33-3-33-888
letters = Entrada.split("-")
t9_to_letters(letters[0])

word = []
for i in letters:
    word.append(t9_to_letters(i))

print(''.join(word))
