###############################################################################
MANIFEST = {
    'name': 'Reto #15',
    'language': 'python',
    'author': 'Joaquín Gutiérrez Pedrosa',
    'github': 'https://github.com/percevaq',
}
###############################################################################
import sys


WELLCOME = """
*******************************************************************************
                  _                                      
              ___| |_ __ _ _ __  __      ____ _ _ __ ___ 
             / __| __/ _` | '__| \ \ /\ / / _` | '__/ __|
             \__ \ || (_| | |     \ V  V / (_| | |  \__ \ 
             |___/\__\__,_|_|      \_/\_/ \__,_|_|  |___/

*******************************************************************************
Ayuda: escriba /q para salir del programa\n
"""
TRANSLITERATION = {
    'a': 'aurek',
    'b': 'besh',
    'c': 'cesh',
    'ch': 'cherek',
    'd': 'dorn',
    'e': 'esk',
    'eo': 'eorek',
    'f': 'forn',
    'g': 'gesh',
    'h': 'heth',
    'i': 'isk',
    'j': 'jenth',
    'k': 'krill',
    'kh': 'khesh',
    'l': 'lesh',
    'm': 'mern',
    'n': 'nern',
    'ng': 'ngorn',
    'o': 'orn',
    'oo': 'oorek',
    'p': 'peh',
    'q': 'qek',
    'r': 'resh',
    's': 'senth',
    'sh': 'shen',
    't': 'teth',
    'th': 'thesh',
    'u': 'ush',
    'v': 'vorn',
    'w': 'wesk',
    'x': 'xesh',
    'y': 'yirt',
    'z': 'zerek'
}


def translate(_word='percevaq', _language='A'):
    _word = _word.lower()
    translation = ''
    if _language == 'a':
        i = 0
        while i < len(_word):
            if _word[i: i + 2] in TRANSLITERATION:
                translation += f' {TRANSLITERATION[_word[i:i + 2]]}'
                i += 2
            elif _word[i: i + 3] in TRANSLITERATION:
                translation += f' {TRANSLITERATION[_word[i:i + 3]]}'
                i += 3
            else:
                if _word[i] in TRANSLITERATION:
                    translation += f' {TRANSLITERATION[_word[i]]}'
                else:
                    translation += f' {_word[i]}'
                i += 1
        return translation.strip()
    elif _language == 's':
        sub_words = _word.split()
        for sub_word in sub_words:
            for key, value in TRANSLITERATION.items():
                if value == sub_word:
                    translation += key
                    break
            else:
                translation += sub_word
        return translation


print(WELLCOME)
word = input(
    '¿Que quieres traducir?: ').lower()
if '/q' in word:
    sys.exit(1)
language = input(
    'Idioma "S" para español / "A" para Aurebesh: ').lower()
if language not in ('s', 'a') or '/q' in language:
    print('Idioma no soportado')
    sys.exit(1)
if '/q' in language:
    sys.exit(1)
print(translate(word, language))
