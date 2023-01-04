def run():

    leet = {
        'A':'4',
        'B':'I3',
        'C':'[',
        'D':')',
        'E':'3',
        'F':'|=',
        'G':'&',
        'H':'#',
        'I':'1',
        'J':',_|',
        'K':'>|',
        'L':'1',
        'M':'/\/|',
        'N':'^/',
        'O':'0',
        'P':'|*',
        'Q':'(_,)',
        'R':'I2',
        'S':'5',
        'T':'7',
        'U':'(_)',
        'V':'\/',
        'W':'\/\/',
        'X':'><',
        'Y':'j',
        'Z':'2'
    }

    text = input('Type a phrase: ').upper()

    text = list(text)
    new_text = []

    for letter in text: 
        if letter in leet.keys():
            new_text.append(leet[letter])
        else:
            new_text.append(' ')
    
    new_text = "".join(new_text)
    print(new_text)


if __name__ == '__main__':
    run()