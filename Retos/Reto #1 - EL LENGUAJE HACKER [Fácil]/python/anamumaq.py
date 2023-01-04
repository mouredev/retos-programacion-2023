def lenguaje_hacker (texto):

    dic = {'A':'4', 'B':'|3', 'C':'[', 'D':')', 'E':'3', 'F':'|=', 'G':'&', 'H':'#', 'I':'1',
                'J':',_|', 'K':'>|', 'L':'1', 'M':'/\/"\"', 'N':'^/', 'O':'0', 'P':'|*', 'Q':'(_,)',
                'R':'I2', 'S':'5', 'T':'7', 'U':'(_)', 'V':'\/', 'W':'\/\/', 'X':'><', 'Y':'j', 'Z':'2'}

    texto = texto.upper()

    for spanish, hacker in dic.items():
        texto = texto.replace(spanish,hacker)

    print(texto)

