def caracter_infiltrado(texto_1: str, texto_2: str) -> list:
    infiltrados = []
    if len(texto_1) != len(texto_2):
        print("Ambas cadenas de texto deben ser iguales en longitud")
        return
    for ch1, ch2 in zip(texto_1, texto_2):
        if ch1 == ch2:
            continue
        infiltrados.append(ch2)
    return infiltrados

print(caracter_infiltrado("Soy marquitos", "Soy.m4rquit0s"))
