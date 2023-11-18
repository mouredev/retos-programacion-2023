# Reto #9: Heterograma, isograma y pangrama

# 
# Crea 3 funciones, cada una encargada de detectar si una cadena de texto es un heterograma, un isograma o un pangrama.
# - Debes buscar la definición de cada uno de estos términos.
# 

def es_heterograma(texto):
    texto = texto.replace(" ", "").lower()
    return len(texto) == len(set(texto))


def es_isograma(texto):
    texto = texto.replace(" ", "").lower()
    return len(texto) == len(set(texto))


def es_pangrama(texto):
    alfabeto = set("abcdefghijklmnopqrstuvwxyz")
    texto = texto.lower()
    return set(texto) >= alfabeto


texto_heterograma = "hiperblanduzcos"
texto_isograma = "anna"
texto_pangrama = "Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú"

resultado_heterograma = es_heterograma(texto_heterograma)
print(f'"{texto_heterograma}" es un heterograma: {resultado_heterograma}')
resultado_isograma = es_isograma(texto_isograma)
print(f'"{texto_isograma}" es un isograma: {resultado_isograma}')
resultado_pangrama = es_pangrama(texto_pangrama)
print(f'"{texto_pangrama}" es un pangrama: {resultado_pangrama}')

