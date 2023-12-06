# Solution

equivalences = {
    'a':'4',
    'b':'l3',
    'c':'[',
    'd':')',
    'e':'3',
    'f':'|=',
    'g':'&',
    'h':'#',
    'i':'1',
    'j':',_|',
    'k':'>|',
    'l':'1',
    'm':'/\\/\\',
    'n':'^/',
    'o':'0',
    'p':'|*',
    'q':'(_,)',
    'r':'l2',
    's':'5',
    't':'7',
    'u':'(_)',
    'v':'\\/',
    'w':'\\/\\/',
    'x':'><',
    'y':'j',
    'z':'2',
    '1':'L',
    '2':'R',
    '3':'E',
    '4':'A',
    '5':'S',
    '6':'b',
    '7':'T',
    '8':'B',
    '9':'g',
    '0':'o',
    ' ': ' '
}

def hacker(input_text):

    string_converted = ''.join(list(map(lambda txt: txt.replace(txt, equivalences[txt]), input_text)))

    return string_converted


if __name__ == '__main__':
    print(hacker('Hello'.lower()))
