def heterograma(palabra: str ) -> str:
    letras_unicas = set(palabra) # Volvemos un conjunto nuestra palabra, y esta borrará todos los datos repetidos.
    # Ahora simplemente comparamos si el input dado es lo mismo en cuanto cantidad de elementos con el conjunto.
    if len(palabra) == len(letras_unicas):
        return f"\"{palabra}\" Es un heterograma ✅"
    else:
        return f"\"{palabra}\" No es un heterograma ❌"

# Todas las letras deben contener la misma cantidad en la palabra
def isograma(palabra: str) -> str:
    letras = {}
    for letra in palabra:
        if letra in letras:
            letras[letra] += 1
        else:
            letras[letra] = 1

    if len(set(letras.values())) == 1:
        return f"\"{palabra}\" Es un isograma ✅"
    else:
        return f"\"{palabra}\" No es un isograma ❌"

def pangrama(frase: str): # Oración con todas las letras del alfabeto
    letras = set("abcdefghijklmnopqrstuvwxyz") # Alfabeto
    letras_faltantes = letras.difference(set(frase.lower()))   
    if letras_faltantes:
        return f"\"{frase}\" -> No es un pangrama ❌"
    else: 
        return f"\"{frase}\" -> Es un pangrama ✅"

if __name__ == '__main__':
    print(heterograma("Perfectamente"))
    print(heterograma("Marte"))
    print()
    
    print(isograma("Automatizado"))
    print(isograma("Compra"))
    print()
    
    print(pangrama("Mouredev reto de programación"))
    print(pangrama("The quick brown fox jumps over the lazy dog."))