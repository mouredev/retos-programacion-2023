import http.client
import re
from unicodedata import normalize
from random import randrange
from replit import clear # To clean the terminal

secred_word = ''
unfinished_word = ''


def create_secred_word():
    global secred_word, unfinished_word
    
    word = get_word()    
    normalize_word = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize("NFD", word), 0, re.I)
    secred_word = normalize_word; unfinished_word = normalize_word
    
    hiddem_counter = int(len(word) * 60 / 100)  
    for _ in range(0, hiddem_counter):
        hidde_character()


def get_word():
    conn = http.client.HTTPSConnection("random-word-api.herokuapp.com")
    conn.request("GET", "/word?lang=es")
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")[2:len(data.decode("utf-8"))-2]


def hidde_character():
    global unfinished_word

    random_position = randrange(0, len(secred_word))
    character = unfinished_word[random_position:random_position+1]

    if character != '_' or character != ' ':
        unfinished_word = unfinished_word[:random_position] + '_' + unfinished_word[random_position+1:]
    else:
        hidde_character()


def reveal_word(_input):
    global unfinished_word
        
    if len(_input) == 1 and secred_word.count(_input) > 0:
        for match in re.finditer(_input, secred_word):
            unfinished_word = unfinished_word[:match.start()] + _input + unfinished_word[match.end():]

    elif _input == secred_word:
        unfinished_word = _input
         

def validate_input(_input):
    if len(re.findall('[a-z]', _input)) == 0:
        print('(!) Only characters from a to z are allowed.');
        return False
    
    if len(_input) > 1 and len(secred_word) != len(_input):
        print('(!) The entry must contain a single letter or the complete word.')
        return False
    
    return True

    
def start_game():
    lives = 5
    character_fails = ''
    
    create_secred_word()

    clear()

    while secred_word != unfinished_word and lives > 0:
        
        print('(+) ' + lives * '❤️ ')     
        print('(+) Complete the word: %s' % unfinished_word)
        if character_fails != '':
            print('(+) Characters used: %s' % character_fails)   
            
        _input = input('(-) Write a letter or a word: ').lower()        
        clear()
        
        if validate_input(_input):
            if (secred_word.count(_input) > 0):
                reveal_word(_input)
            else:
                print('(!) The entry not match.')
                lives -= 1
                if len(_input) == 1:
                    character_fails = ' '.join([character_fails, _input])
                    
    else:                            
        print('(+) The secred word is "%s"' % secred_word)
        print('(+) You Win!!' if lives > 0  else 'You Lost :(')

if __name__ == '__main__' :
    pay = True
    while pay:
        start_game()
        pay = (input('(-) Do you want to play again?\n(-) Type "y" to play again and another key to end the game: ').lower()  == 'y')
    
    clear()
