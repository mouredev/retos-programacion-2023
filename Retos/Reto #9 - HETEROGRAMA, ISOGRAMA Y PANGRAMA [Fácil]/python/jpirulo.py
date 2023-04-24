class VerificadorPalabras:
    def es_heterograma(self, texto: str) -> bool:
        conjunto = set(texto)
        if len(texto) == len(conjunto):
            return True
        else:
            return False

    def es_isograma(self, texto: str) -> bool:
        texto = texto.lower().replace(" ", "")
        letras = set()
        for letra in texto:
            if letra in letras:
                return False
            else:
                letras.add(letra)
        return True

    def es_pangrama(self, texto: str) -> bool:
        abecedario = set('abcdefghijklmnopqrstuvwxyz')
        letras_texto = set(texto.lower().replace(" ", ""))
        return abecedario.issubset(letras_texto)


verificador = VerificadorPalabras()


texto1 = "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja."
if verificador.es_pangrama(texto1):
    print(texto1, "es un pangrama")
else:
    print(texto1, "no es un pangrama")

texto2 = "Este texto no es un pangrama"
if verificador.es_pangrama(texto2):
    print(texto2, "es un pangrama")
else:
    print(texto2, "no es un pangrama")

texto1 = "Hola mundo"
if verificador.es_heterograma(texto1):
    print(texto1, "es un heterograma")
else:
    print(texto1, "no es un heterograma")

texto2 = "repetir"
if verificador.es_isograma(texto2):
    print(texto2, "es un isograma")
else:
    print(texto2, "no es un isograma")
