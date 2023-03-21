def main():
    input1 = inputText()
    hacker = hackText(input1)
    print(f'Texto en lenguaje hacker:\n {hacker}')

alphabeth = {
    'a': '4', 'b': '|3', 'c': '[', 'd': '|>', 'e': '3',
    'f': '|=', 'g': '&', 'h': '#', 'i': '1', 'j': ']', 
    'k': '|(', 'l': '7', 'm': 'nn', 'n': '^', 'o': '0', 
    'p': '|*', 'q': '9', 'r': '|2', 's': '5', 't': '-|-', 
    'u': '(_)', 'v': '|/', 'w': '\|/', 'x': '><', 'y': 'j', 
    'z': '2', ' ': ' '
}

def inputText():
    textUser = input('Ingresa un texto\n')
    lowerText = textUser.lower()
    return lowerText

def hackText(text):
    convertedText = []

    for i in text:
        if i in alphabeth:
            convertedText.append(alphabeth[i])
            leet = ''.join(convertedText)
    return str(leet)

if __name__ == '__main__':
    main()