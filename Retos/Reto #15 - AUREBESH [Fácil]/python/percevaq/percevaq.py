import sys
import os
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print('Instala la libreria python Pillow\n'
          'pip install Pillow\n')
    sys.exit(1)

###############################################################################
MANIFEST = {
    'name': 'Reto #15',
    'language': 'python',
    'github': 'https://github.com/percevaq',
}
###############################################################################
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
    _translation = ''
    if _language == 'a':
        i = 0
        while i < len(_word):
            if _word[i: i + 2] in TRANSLITERATION:
                _translation += f' {TRANSLITERATION[_word[i:i + 2]]}'
                i += 2
            elif _word[i: i + 3] in TRANSLITERATION:
                _translation += f' {TRANSLITERATION[_word[i:i + 3]]}'
                i += 3
            else:
                if _word[i] in TRANSLITERATION:
                    _translation += f' {TRANSLITERATION[_word[i]]}'
                else:
                    _translation += f' {_word[i]}'
                i += 1
        return _translation.strip()
    elif _language == 's':
        sub_words = _word.split()
        for sub_word in sub_words:
            for key, value in TRANSLITERATION.items():
                if value == sub_word:
                    _translation += key
                    break
            else:
                _translation += sub_word
        return _translation


def generate_imagen(_translation):
    image = Image.new("RGB", (1920, 1080), "black")
    font = ImageFont.truetype(os.path.join(
        os.path.dirname(__file__), 'Aurebesh.ttf'), size=72)
    draw = ImageDraw.Draw(image)
    x = 960 - (len(_translation) * 70) / 2
    y = 520
    draw.text((x, y), _translation, font=font, align='center')
    image.show()


def main():
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
    translation = translate(word, language)
    print(translation)
    if language == 'a':
        print('Aquí te muestro la traducción')
        create_image = input(
            '¿Quieres ver como se escribiría?\n'
            'Si=S /No=N\n'
        ).lower()
        if create_image == 's':
            generate_imagen(word)


if __name__ == '__main__':
    main()
