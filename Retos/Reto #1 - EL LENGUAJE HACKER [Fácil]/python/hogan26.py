diccionario = {'a':'4','b':'|3','c':'[','d':')','e':'3','f':'|=','g':'&','h':'#','i':'1','j':',_|','k':'>|','l':'1','m':'/\/\\','n':'^/','o':'0','p':'|*','q':'(_,)','r':'|2','s':'5','t':'7','u':'(_)','v':'\/','w':'\/\/','x':'><','y':'j','z':'2','1':'L','2':'R','3':'E','4':'A','5':'S','6':'b','7':'T','8':'B','9':'g','0':'o',' ':' '}

def traducir(palabra):    
    traduccion = ''
    for letra in palabra:
        traduccion += diccionario[letra]
    
    return traduccion

palabra = input('Ingresa una palabra\n').lower()
print(traducir(palabra))