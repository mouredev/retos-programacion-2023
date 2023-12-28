# Crea una función que sea capaz de transformar Español al lenguaje básico 
# del universo Star Wars: el "Aurebesh".
# - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
# - También tiene que ser capaz de traducir en sentido contrario.

diccionario = {
    'ch': 'cherek', 'ae': 'enth', 'eo': 'onith', 'kh': 'krenth', 'ng': 'nen', 'oo': 'orenth', 'sh': 'shen',
    'th': 'thesh', 'a': 'aurek', 'b': 'besh', 'c': 'cresh', 'd': 'dorn', 'e': 'esk', 'f': 'forn', 'g': 'grek',
    'h': 'herf', 'i': 'isk', 'j': 'jenth', 'k': 'krill', 'l': 'leth', 'm': 'mern', 'n': 'nern', 'o': 'osk',
    'p': 'peth', 'q': 'qek', 'r': 'resh', 's': 'senth', 't': 'trill', 'u': 'usk', 'v': 'vev', 'w': 'wesk',
    'x': 'xesh', 'y': 'yirt', 'z': 'zerek'
    }

class traductor:
    def __init__(self) -> None:
        pass

    def aurebes_espanol(self, texto):
        texto = texto.lower()
        i = 0
        texto_final = ''
        while i < len(texto):
            letra = texto[i]
            letras = ''
            if (i + 1) < len(texto):
                letras = texto[i] + texto[i + 1]
            
            if letras in diccionario:
                texto_final += diccionario[letras]
                i += 1
            elif texto[i] in diccionario:
                texto_final += diccionario[letra]
            else:
                texto_final += texto[i]
            i += 1
        print(f"La traducción es: {texto_final}")

    def espanol_aurebes(self, texto):
        for i, value in diccionario.items():
            texto = texto.replace(value, i)
        print(f"La traducción es: {texto}")

    def start_traductor(self):
        print("Traducir de Aurebes a Español (E) o Viceversa (V)")
        opcion1 = input("Ingresa una opción: ")

        if opcion1 == 'E' or opcion1 == 'V':
            texto = input("Ingresar texto a traducir: ")
            if opcion1	== 'E':
                self.aurebes_espanol(texto)
            else:
                self.espanol_aurebes(texto)
        else:
            print("Valor incorrecto")

frase = traductor()
frase.start_traductor()
