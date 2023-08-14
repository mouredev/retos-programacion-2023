'''
The `leet` function takes a string or integer as input and returns the leet (1337) version of the
text.

:param text: The `text` parameter in the `leet` function is either a string or an integer
:type text: str|int
:return: The function `leet` returns a string that has been converted to leet (1337) text.
'''
def leet(text: str|int) -> str:
    leet_text = ''
    vocabulary = {
        'a': '4',
        'b': 'I3',
        'c': '[',
        'd': ')',
        'e': '3',
        'f': '|=',
        'g': '&',
        'h': '#',
        'i': '1',
        'j': ',_|',
        'k': '>|',
        'l': '1',
        'm': '/\/\\',
        'n': '^/',
        'o': '0',
        'p': '|*',
        'q': '(_,)',
        'r': 'I2',
        's': '5',
        't': '7',
        'u': '(_)',
        'v': '\/',
        'w': '\/\/',
        'x': '><',
        'y': 'j',
        'z': '2',
        '1': 'L',
        '2': 'R',
        '3': 'E',
        '4': 'A',
        '5': 'S',
        '6': 'b',
        '7': 'T',
        '8': 'B',
        '9': 'g',
        '0': 'o',
    }
    
    for letter in str(text):
        leet_text += vocabulary[letter]

    return leet_text

# The code is asking the user to input a text and then it calls the `leet` function with the user's
# input as the argument. The leet version of the input text is then printed to the console.
input = input('Give me a text: ')
print('the leet text is: %s' %(leet(input)))