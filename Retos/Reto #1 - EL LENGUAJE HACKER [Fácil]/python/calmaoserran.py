#!/usr/bin/python3
import sys

leet_dict = {
        'a':'4','b':'I3','c':'[','d':')','e':'3','f':'|=','g':'&','h':'#','i':'1','j':',_|',
        'k':'>|','l':'1','m':'/\/\\','n':'^/','o':'0','p':'|*','q':'(_,)','r':'I2','s':'5',
        't':'7','u':'(_)','v':'\/','w':'\/\/','x':'><','y':'j','z':'2','1':'L','2':'R','3':'E',
        '4':'A','5':'S','6':'b','7':'T','8':'B','9':'g','0':'o'
        }

def leet_translator(text: str) -> str:
    """Recibe una string en lenguaje natural y la devuelve traducida a jerga leet"""

    translated_test = ""
    for char in text:
        if char in leet_dict:
            translated_test += leet_dict[char.lower()]
        # No traducimos espacios o signos.
        else:
            translated_test += char
    return translated_test

if __name__ == "__main__":
    # Si hay parámetro en la invocación lo usa como texto a traducir
    if len(sys.argv) == 2:
        texto_natural = sys.argv[1]
    else:
    # Y si no usa este parámetro hardcoded
        texto_natural = 'Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres.'
    print(leet_translator(texto_natural))