
dict_traductor = { 'a' : '4',   'b' : 'I3',   'c' : '[',     'd' : ')',    'e' : '3',   'f' : '|=',     'g' : '&' , 
                    'h' : '#',  'i' : '1',    'j' : ',_|',   'k' : '>|',   'l' : '1',   'm' : '|\\/|',  'n' : '^/',
                    'o' : '0',  'p' : '|*',   'q' : '(_,)',  'r' : 'I2',   's' : '5',   't' : '7',      'u' : '(_)',
                    'v' : '\/', 'w' : '\/\/', 'x' : '><',    'y' : 'j',    'z' : '2',

                    '0':'o',  '1':'L',    '2':'R',     '3':'E',  '4':'A',  '5':'S',   '6':'b',  '7':'T',   '8':'B',  '9':'g'
                    }

def traductor(texto):
    texto = texto.lower()
    texto_traducido = ''.join([dict_traductor[letra] for letra in texto if letra in dict_traductor])

    return texto_traducido

def main():
    texto = input('Introduce el texto a traducir: ')
    print(traductor(texto))


if __name__ == '__main__':
    main()