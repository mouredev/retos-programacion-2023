leet = {'a': '4', 'b': 'I3', 'c': '[', 'd': ')', 'e': '3', 'f': '|=',
        'g': '&', 'h': '#', 'i': '1', 'j': ',_|', 'k': '>|', 'l': '1',
        'm': '/\/\\', 'n': '^/', 'o': '0', 'p': '|*', 'q': '(_,)',
        'r': '|2', 's': '5', 't': '7', 'u': '(_)', 'v': '\/', 'w': '\/\/', 'x': '><', 'y': 'j', 'z': '2'}

text = list('hello world!'.lower())
text2 = text.copy()

for i in range(len(text2)):
    if text2[i] in leet.keys():
        text2[i] = leet[text2[i]]

print(''.join(text))
print(''.join(text2))
