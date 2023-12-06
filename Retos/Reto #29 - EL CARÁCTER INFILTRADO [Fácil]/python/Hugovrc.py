def caracter_infiltrado(cadena: str, cadena2: str):
    lista_caracteres = []

    size = min(len(cadena), len(cadena2))
    
    for indice in range(size):
        if cadena[indice] != cadena2[indice]:
            lista_caracteres.append(cadena2[indice])
    
    print(lista_caracteres)

caracter_infiltrado("hola meure gracias por los retos", "hola.moure gracias por los retos")
caracter_infiltrado("me,llamo Hugo", "me llamo+hugo")
