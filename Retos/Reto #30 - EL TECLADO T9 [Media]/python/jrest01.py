t9_keyboard = {
    '1' : '',
    '2' : 'abc',
    '3' : 'def',
    '4' : 'ghi',
    '5' : 'jkl',
    '6' : 'mno',
    '7' : 'pqrs',
    '8' : 'tuv',
    '9' : 'xyz'
}

def t9_traduction(input):
    final = ''
    input = input.split('-')
    for i in input:
        option_values = t9_keyboard[i[0]]
        char = option_values[len(i)-1]
        final += char
    return final


if __name__ == '__main__':
    input = '6-666-88-777-33-3-33-888'
    # print(input.split('-'))
    print(t9_traduction(input))