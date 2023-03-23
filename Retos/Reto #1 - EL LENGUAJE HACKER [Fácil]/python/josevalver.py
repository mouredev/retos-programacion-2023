from array import *

leeters = [['A', '4'], ['B', 'I3'], ['C', '['], ['D', ')'], ['E', '3'], ['F', '|='], ['G', '&'], ['H', '#'], ['I', '1'],
        ['J', ',_|'], ['K', '>|'], ['L', '1'], ['M', '|\\/|'], ['N', '^/'], ['O', '0'], ['P', '|*'], ['Q', '(_,)'], ['R', 'I2'],
        ['S', '5'], ['T', '7'], ['U', '(_)'], ['V', '\\/'], ['W', '\\/\\/'], ['X', '><'], ['Y', 'j'], ['Z', '2']]

numbleet = [['0', 'o'], ['1', 'L'], ['2', 'R'], ['3', 'E'], ['4', 'A'], ['5', 'S'], ['6', 'b'], ['7', 'T'], ['8', 'B'], ['9', 'g']]


def convert_text(text):
    leet_text = ''
    for char in text:
        if char.isdigit():
            for num in numbleet:
                if char == num[0]:
                    leet_text += num[1]
        elif char.isalpha():
            for letter in leeters:
                if char.upper() == letter[0]:
                    leet_text += letter[1]
        else:
            leet_text += char

    return leet_text

def main():
    text = input('Enter text to convert to leet: ')
    print(convert_text(text))

if __name__ == '__main__':
    main()