def convertir_a_hacker(texto: str):
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
    HACKER = ['4', 'I3', '[', ')', '3', '|=', '&', '#', '1', ',_|', '>|',
            '1', '/\/\\', '^/', '0', '|*', '(_,)', 'I2', '5', '7',
            '(_)', '\/', '\/\/', '><', 'j', '2']
    abc_keys = dict(zip(ABC, HACKER))

    hacker_txt = []
    for palabra in texto.split():
        nueva_palabra = ''
        for letra in palabra:
            nueva_letra = abc_keys.get(letra, letra)
            nueva_palabra = nueva_palabra + nueva_letra
        hacker_txt.append(nueva_palabra)
    print(' '.join(hacker_txt))

texto = input('Escribe el texto a transformar (ej. leet -> 1337): ').strip().lower()
convertir_a_hacker(texto)
