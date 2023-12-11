import re

def cleanText(text: str) -> str:
    # Elimina caracteres especiales
    pattern = r'[^a-zA-ZñÑáéíóúÁÉÍÓÚüÜ]'
    text_clear = re.sub(pattern, '', text)
    list_text = [str.lower(ch) for ch in text_clear]

    # Conversión de vocales con tildes
    map_ch = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u'
    }
    list_ = []
    for ch in list_text:
        if ch in map_ch.keys():
            list_.append(map_ch.get(ch))
        else:
            list_.append(ch)
        
    return list_

def isHeterograma(text: str) -> None:
    # Palabra que no repite ninguna letra
    clean_text = cleanText(text)
    len_original = len(clean_text)
    
    if len_original == len(set(clean_text)):
        print('La palabra o frase es un Heterograma')
    else:
        print('La palabra o frase NO es un Heterograma')

def isIsograma(text: str) -> None:
    # Palabra en la que cada letra aparece el mismo número de veces
    clean_text = cleanText(text)

    counter = []
    for ch in clean_text:
        counter.append(clean_text.count(ch))
    
    if (len(set(counter)) == 1) & (counter[0] > 1):
        print('La palabra o frase es un Isograma')
    else:
        print('La palabra o frase NO es un Isograma')


def isPangrama(text: str) -> None:
    # Texto que usa todas las letras posibles del alfabeto
    clean_text = cleanText(text)
    n_ch = len(set(clean_text))
    
    if n_ch == 27:
        print('La palabra o frase es un Pangrama')
    else:
        print('La palabra o frase NO es un Pangrama')
    
def isHIP(text: str) -> None:
    isHeterograma(text)
    isIsograma(text)
    isPangrama(text)

if __name__=='__main__':
    isHeterograma('Sujeto')
    isIsograma('Mama')
    isPangrama('El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja.')
    isHIP('murciélago')
