#!/usr/bin/env python3

diccionario = {'.':'.', ',':',', ' ':' ', 'ñ':'^/~', 'a':'4', 'b':'|3', 'c':'[', 'd':')', 'e':'3', 'f':'|=', 'g':'&', 'h':'#', 'i':'1', 'j':',_|', 'k':'>|', 'l':'|_', 'm':'JVI', 'n':'^/', 'o':'0', 'p':'|*', 'q':'(_,)', 'r':'|2', 's':'5', 't':'7', 'u':'v', 'v':'\/', 'w':'\/\/', 'x':'><', 'y':'j', 'z':'2'}

palabra = input('Ingresa una frase sin tilde: ')

palabra_low = palabra.lower()


leet_code=''

for char in palabra_low:

    for key, valor in diccionario.items():

        if(char == key):
            leet_code+=valor
            break

print(leet_code)
