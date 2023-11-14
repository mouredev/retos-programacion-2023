from string import ascii_lowercase

'''
Crea 3 funciones, cada una encargada de detectar si una cadena de
texto es un heterograma, un isograma o un pangrama.
Debes buscar la definición de cada uno de estos términos.
'''

class AnalisaPalabras:
    def __init__(self, palabra):
        self.palabra = palabra

    def heterograma(self):
        palabra = self.palabra.lower()
        letras_unicas = set(palabra)

        if len(letras_unicas) == len(palabra):
            return print("Heterograma ->" ,True)
        else:
            return print("Heterograma ->" ,False)

    def isograma(self):
        palabra = self.palabra.lower()
        letras_unicas = set(palabra)

        if len(letras_unicas) != len(palabra):
            return print("Isograma ->" ,True)
        else:
            return print("Isograma ->" ,False)

    def pangrama(self, texto):
        texto = set("".join(texto.lower().split()))
        abc = list(ascii_lowercase)

        if "ñ" in texto:
            abc.append("ñ")

        if any(f not in texto for f in abc):
            return print("Pangrama ->" ,False)
        else:
            return print("Pangrama ->" ,True)


palabra01 = AnalisaPalabras("Fernando")
palabra01.heterograma()
palabra01.isograma()
palabra01.pangrama("The quick brown fox jumps over the lazy dogñ")