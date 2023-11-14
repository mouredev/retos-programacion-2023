originalText = input("Please give me something to translate: ")
leetedTex = ''

dictionary = {
    'a':'4',
    'b':'8',
    'c':'(',
    'd':'[)',
    'e':'3',
    'f':'|=',
    'g':'6',
    'h':'#',
    'i':'1',
    'j': "_/",
    'k': "|<",
    'o': "0",
    't': "7",
}

for char in originalText:
    sanitazedChar = char.lower()
    if sanitazedChar in dictionary:
        leetedTex = leetedTex +  dictionary[sanitazedChar]
    else:
        leetedTex = leetedTex +  sanitazedChar 

print(leetedTex)