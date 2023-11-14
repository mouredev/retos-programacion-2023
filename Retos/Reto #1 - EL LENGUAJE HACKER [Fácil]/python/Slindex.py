texto = input('Por favor ingresa el texto a transformar 💬 ')
output = ''

leet = {'a':'4', 'A':'4',
        'e':'3', 'E':'3',
        'i':'1', 'I':'1',
        'o':'0', 'O':'0',
        'u': '(_)', 'U': '(_)',
        '1':'L',
        '2':'R',
        '3':'E',
        '4':'A',
        '5':'S',
        '6':'b',
        '7':'T',
        '8':'B',
        '9':'g',
        '0':'o'}

for char in texto:
    if char in leet:
        output = output + leet[char]
    else:
        output = output + char

print(output)