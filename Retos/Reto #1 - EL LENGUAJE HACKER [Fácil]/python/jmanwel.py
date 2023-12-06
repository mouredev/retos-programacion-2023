
def translate_to_1337 (s):
    output = ""
    leet = {'a':'4','b':'I3','c':'[','d':')','e':'3','f':'|=','g':'&','h':'#','i':'1', 'j':',_|', 'k':'>|', 
'l':'1', 'm':'/\/\\', 'n':'^/', 'o':'0','p':'|*','q':'(_,)', 'r':'I2', 's':'5','t':'7','u':'(_)',
'v':'\/','w':'\/\/','x':'><','y':'j','z':'2'}
    phrase = []
    for i in s.lower().split(" "):
        word = []
        for j in i:
            if j not in ",.![]()\\/#$%&=-0123456789":
                word.append(leet[j])
            else:
                word.append(j)
        phrase.append(''.join(word))
    for i in phrase:
        output += i + " "
    return output.strip()


print(translate_to_1337("esto es una prueba"))
print(translate_to_1337("esto es una prueba, para amigos! #"))
