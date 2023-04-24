'''
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *  con el alfabeto y los números en "leet".
 *  (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
 
 #robots.txt for all our sites
User-agent: *
Disallow: /content/*
'''
import requests
from bs4 import BeautifulSoup
import time


def scrapLeng() -> dict:
    url = 'https://simple.wikipedia.org/wiki/Leet';
    req = requests.get(url);
    soup = BeautifulSoup(req.text, 'html.parser');
    listHtml = soup.find('div', attrs={'class':'mw-body-content mw-content-ltr'});
    label_list = listHtml.find_all('li');
    slang = [element.text for element in label_list if ': ' in element.text][0:26];
    traductor = dict();
    url = None;
    req = None;
    soup = None;
    listHtml = None;
    for registro in slang:
        letter = registro.split(':')[0].strip();
        trans = registro.split(':')[1].strip();
        traductor[letter] = trans.split(',');
    slang = None;
    return traductor;


def lengHacker() -> None:
    textHacker = ''; 
    text = input('Introduzca cadena de texto: ');
    start_time = time.time();
    traductor = scrapLeng();
    for letter in text:
        if letter.upper() in traductor.keys():
            newText = traductor[letter.upper()][0];
            textHacker += newText.strip();
            continue;
        textHacker += letter;
    text = None;
    traductor = None;
    print(textHacker)
    print("Proceso finalizado --- %s segundos ---" % (time.time() - start_time))
    


if __name__ == '__main__':
    lengHacker();
            
        
    
    

