import string

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
digits = list(string.digits)
alph = list(string.ascii_letters) + digits

def change_index(_list, n):
    encrypt = ''

    for x in _list: 
        index = _list.index(x) + n
        if index >= len(_list):
            multi = 1
            if index >= len(_list)*2:
                multi = round(index/len(_list))

            index = index - (len(_list) * multi)

        encrypt+= _list[index]
    
    return encrypt

def alph_crypt(n):
    lower_crypt = change_index(lower, n)
    upper_crypt = change_index(upper, n)
    digits_crypt = change_index(digits, n)
    alph_crypt = lower_crypt + upper_crypt + digits_crypt

    return alph_crypt
   
def procces(word, alph1, alph2):
    new_text = ''
    for letter in word:
        if letter in alph1:
            index_letter = alph1.index(letter)
            new_text+= alph2[index_letter]
        else:
            new_text+=letter

    return new_text

def encrypt(word, n):
    return procces(word, alph, alph_crypt(n))

def decrypt(word, n):
    return procces(word, alph_crypt(n), alph)

_type = int(input("(ENCRYPT=1, DECRYPT=2): "))
disp = int(input("DISPLACEMENTS: "))
txt = input("TYPE THE TEXT: ")

if _type == 1:
    print(f'RESULT: {encrypt(txt,disp)}')
elif _type == 2:
    print(f'RESULT: {decrypt(txt,disp)}')
else:
    print("----")