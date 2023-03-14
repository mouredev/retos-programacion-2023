def leetSpekAlphabet(words):
    dict = {
        'a': '4', 'b': 'ß', 'c': '(', 'd': '?', 'e': '3', 'f': 'ƒ', 'g': '9',
        'h': ':-:', 'i': '1', 'j': '_]', 'k': '|c', 'l': '£', 'm': 'nn', 'n': '[\]',
        'o': 'oh', 'p': '|^', 'q': '2', 'r': '/2', 's': 'ehs', 't': '~|~', 'u': 'v',
        'v': '|/', 'w': 'uu', 'x': 'ecks', 'y': '`/', 'z': '%', '1': 'L',
        '2': 'R', '3': 'E', '4': 'A', '5': 'S', '6': 'b', '7': 'T', '8': 'B',
        '9': 'q', '0': '()'
    }

    return ''.join(dict.get(text.lower(), text) for text in words)

print("Enter the text you want to convert to the hacker language: ")
word = input("")
result = leetSpekAlphabet(word)

print(result)