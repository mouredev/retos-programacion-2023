def teclado_T9(pulsaciones: str):
    teclado = {"2":"ABC", "3":"DEF", "4":"GHI", "5":"JKL", "6":"MNO", "7":"PQRS", "8":"TUV", "9":"WXYZ"}
    #print(teclado.get("2")[0])
    #print(teclado["2"][0])
    letra = []
    palabra = ""
    
    letra = pulsaciones.split("-")
    for tecla in letra:
        if tecla[0] in teclado.keys():
            palabra += teclado[tecla[0]][len(tecla)- 1]#
    print(palabra)

teclado_T9("6-666-88-777-33-3-33-888")
teclado_T9("44-88-4-656")