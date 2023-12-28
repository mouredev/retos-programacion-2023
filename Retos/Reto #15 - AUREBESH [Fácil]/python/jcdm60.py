# Reto #15: Aurebesh
# Dificultad: Fácil | Publicación: 10/04/23 | Corrección: 17/04/23

## Enunciado

#
# Crea una función que sea capaz de transformar Español al lenguaje básico del universo
# Star Wars: el "Aurebesh".
# - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
# - También tiene que ser capaz de traducir en sentido contrario.
#
# ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
#
# ¡Que la fuerza os acompañe!
#


class TraductorAurebesh:
    def __init__(self):
        self.diccionario_espanol_aurebesh = {
            "a": "aurek",
            "b": "besh",
            "c": "cresh",
            "d": "dorn",
            "e": "esk",
            "f": "forn",
            "g": "grek",
            "h": "herf",
            "i": "isk",
            "j": "jenth",
            "k": "krill",
            "l": "leth",
            "m": "mern",
            "n": "nern",
            "o": "osk",
            "p": "peth",
            "q": "qek",
            "r": "resh",
            "s": "senth",
            "t": "trill",
            "u": "usk",
            "v": "vev",
            "w": "wesk",
            "x": "xesh",
            "y": "yirt",
            "z": "zerek",
        }

        self.diccionario_aurebesh_espanol = {
            aurebesh: espanol
            for espanol, aurebesh in self.diccionario_espanol_aurebesh.items()
        }

    def transformar_espanol_aurebesh(self, texto):
        texto = texto.lower()
        texto_aurebesh = ""
        for letra in texto:
            if letra in self.diccionario_espanol_aurebesh:
                texto_aurebesh += self.diccionario_espanol_aurebesh[letra]
            else:
                texto_aurebesh += letra

        return texto_aurebesh

    def transformar_aurebesh_espanol(self, texto):
        palabras = texto.split()
        output_palabras = [self.transforma_palabra(palabra) for palabra in palabras]
        output_string = " ".join(output_palabras)
        return output_string

    def transforma_palabra(self, palabra):
        texto_espanol = ""
        i = 0
        while i < len(palabra):
            found = False
            for j in range(5, 0, -1):
                if ( i + j <= len(palabra) and palabra[i : i + j] in self.diccionario_aurebesh_espanol):
                    texto_espanol += self.diccionario_aurebesh_espanol[palabra[i : i + j]]
                    i += j
                    found = True
                    break
            if not found:
                i += 1
        return texto_espanol


if __name__ == "__main__":
    traductor = TraductorAurebesh()
    
    texto = traductor.transformar_espanol_aurebesh("brais moure")
    print(texto) # beshreshaurekisksenth mernoskuskreshesk

    texto = traductor.transformar_aurebesh_espanol("beshreshaurekisksenth mernoskuskreshesk")
    print(texto) # brais moure
