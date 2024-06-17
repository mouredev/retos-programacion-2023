#!/usr/bin/env python3

'''
* Llamar a una API es una de las tareas más comunes en programación.
*
* Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
* resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
*
* Aquí tienes un listado de posibles APIs:
* https://github.com/public-apis/public-apis
'''

import requests

def text_format(text):
    if "setup" in text:
        print(f'\n[?] {text["setup"]}\n')
        print(f'[+] {text["delivery"]}\n')
    else:
        print(f'\n[+] {text["joke"]}\n')

def jokes():
    url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw"
    try: 
        r = requests.get(url)
        text = r.json()
        text_format(text)
    except Exception as e:
        print(f"\n[!] Se ha producido un error: {e}")

def main():
    jokes()

if __name__ == '__main__':
    main()