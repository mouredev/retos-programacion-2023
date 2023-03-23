replace_alphabet = {
    'A': '4',
    'B': 'I3',
    'C': '[',
    'D': ')',
    'E': '3',
    'F': '|=',
    'G': '&',
    'H': '#',
    'I': '1',
    'J': ',_|',
    'K': '>|',
    'L': '1',
    'M': '/\/\\',
    'N': '^/',
    'O': '0',
    'P': '|*',
    'Q': '(_,)',
    'R': 'I2',
    'S': '5',
    'T': '7',
    'U': '(_)',
    'V': '/',
    'W': '//',
    'X': '><',
    'Y': 'j',
    'Z': '2',
}


def hacker_language(letter):
    return replace_alphabet[letter.upper()] if letter.upper() in replace_alphabet else letter


def leet(sentence, fn):
    return ''.join(map(fn, sentence))


def main():
    sentence = input("Frase a traducir: ")
    print(leet(sentence, hacker_language))


if __name__ == '__main__':
    main()
