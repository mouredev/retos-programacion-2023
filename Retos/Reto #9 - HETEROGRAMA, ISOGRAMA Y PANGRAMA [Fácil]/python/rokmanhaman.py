"""Reto #9: HETEROGRAMA, ISOGRAMA Y PANGRAMA
FÁCIL | Publicación: 27/02/23 | Resolución: 06/03/23
/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */"""

# HETEROGRAMA: palabra o frase que no contiene ninguna letra repetida.
# ISOGRAMA: palabra o frase en la que cada letra aparece el mismo número de veces
# PANGRAMA:  es un texto que usa todas las letras posibles del alfabeto de un idioma

import string

class MyText():

    def __init__(self, text):
        self.text = text
    
    def is_heterograma(self):
        text_without_spaces = self.text.replace(" ", "")
        text_without_duplicated = set(text_without_spaces)
        
        ocurrencias = {
            text_without_duplicated: 
            self.text.count(text_without_duplicated) 
            for text_without_duplicated in text_without_duplicated}
        
        max_occ = max(ocurrencias.values())

        return "es HETEROGRAMA" if max_occ == 1 else "no es HETEROGRAMA"
  
    def is_isograma(self):
        text_without_spaces = self.text.replace(" ", "")
        text_without_duplicated = set(text_without_spaces)
        
        ocurrencias = {
            text_without_duplicated: 
            self.text.count(text_without_duplicated) 
            for text_without_duplicated in text_without_duplicated}
        
        lista = list(ocurrencias.values())
        check = True
        for index, val in enumerate(lista):
            check = lista[index] == lista[0] and check

        return  "es ISOGRAMA" if check == True else "no es ISOGRAMA"
    
    def is_pangrama(self):
        text_without_spaces = self.text.replace(" ", "")
        text_without_duplicated = set(text_without_spaces)
        lpos = string.ascii_lowercase
        
        check = True
        for l in lpos:
            if l in text_without_duplicated:
                check = True and check
            else:
                check = False
            


        return  "es PANGRAMA" if check == True else "no es PANGRAMA"


#frase = "murciélago"
#frase = "mama"
frase = "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja"

f = MyText(frase)
print(f.is_heterograma())
print(f.is_isograma())
print(f.is_pangrama())
        
