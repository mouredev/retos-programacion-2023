class TraductorAurebesh:
    def __init__(self):
        self.aurebesh_dict = {
            "a": "aurek",
            "b": "besh",
            "c": "cresh",
            "d": "dorn",
            "e": "epp",
            "f": "eff",
            "g": "grev",
            "h": "hest",
            "i": "isht",
            "j": "jenth",
            "k": "krill",
            "l": "lemm",
            "m": "mern",
            "n": "nerf",
            "o": "oo",
            "p": "peh",
            "q": "quar",
            "r": "resh",
            "s": "senth",
            "t": "thur",
            "u": "un",
            "v": "vex",
            "w": "wyr",
            "x": "ecks",
            "y": "yirt",
            "z": "zerek"
        }

    def traducir_espanol_a_aurebesh(self, texto):
        try:
            texto = texto.lower()
            texto_traducido = ""
            i = 0
            while i < len(texto):
                if texto[i:i+2] in ["sh", "th", "ch", "ph"]:
                    texto_traducido += self.aurebesh_dict.get(texto[i:i+2], texto[i:i+2]) + " "
                    i += 2
                elif texto[i] in self.aurebesh_dict:
                    texto_traducido += self.aurebesh_dict[texto[i]] + " "
                    i += 1
                else:
                    texto_traducido += texto[i]
                    i += 1
            return texto_traducido.capitalize().strip()
        except Exception as e:
            print("Se produjo un error al traducir el texto:", e)

    def traducir_aurebesh_a_espanol(self, texto):
        try:
            texto = texto.lower()
            texto_traducido = ""
            palabras = texto.split()
            for palabra in palabras:
                for key, value in self.aurebesh_dict.items():
                    if palabra == value:
                        texto_traducido += key
                        break
                else:
                    texto_traducido += palabra
                texto_traducido += " "
            return texto_traducido.capitalize().strip()
        except Exception as e:
            print("Se produjo un error al traducir el texto:", e)

if __name__ == '__main__':
    traductor = TraductorAurebesh()
    texto_a_traducir = input("Ingrese el texto a traducir: ")
    texto_traducido = traductor.traducir_espanol_a_aurebesh(texto_a_traducir)
    print(f"El texto traducido al alfabeto Aurebesh es: {texto_traducido}")
    texto_original = traductor.traducir_aurebesh_a_espanol(texto_traducido)
    print(f"El texto traducido de regreso al español es:: {texto_original}")
