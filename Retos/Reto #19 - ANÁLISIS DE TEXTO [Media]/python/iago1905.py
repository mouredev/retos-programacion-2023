palabras = 0
media = 0
oraciones = 0
larga = ''
n_letras = 0
texto =  "Esto es un texto de pruebaaaaa. Radiolaaaaa."
texto = texto.split(' ')

for palabra in texto:
    palabras += 1
    n_letras += len(palabra)
    if len(palabra) > len(larga):
        larga = palabra
    if '.' in palabra:
        oraciones += 1

media = n_letras / palabras
print(f'El texto tiene {palabras} palabras, {oraciones} oraciones y una media de {media} letras por palabra. Y la palabra mas larga es {larga}')