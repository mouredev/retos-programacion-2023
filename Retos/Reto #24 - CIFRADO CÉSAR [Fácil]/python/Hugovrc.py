
def cifrado_cesar(posicion: int, palabra: str, descifrar: False):
    abecedario = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    cifrado = ""
    
    if descifrar == False:
        for letra in palabra:
            if letra.upper() in abecedario:
                posicion_lista_abcedario = abecedario.index(letra.upper())
                cantidad_total = posicion_lista_abcedario + posicion
                
                if cantidad_total >= len(abecedario):
                    nueva_posicion = cantidad_total - len(abecedario)
                    cifrado += abecedario[nueva_posicion]
                else:
                    cifrado += abecedario[posicion_lista_abcedario + posicion]
            else:
                cifrado += " "
    else:
        for letra in palabra:
            if letra.upper() in abecedario:
                posicion_lista_abcedario = abecedario.index(letra.upper())
                cantidad_total = posicion_lista_abcedario + posicion
                if posicion <= len(abecedario):
                    cifrado += abecedario[posicion_lista_abcedario - posicion]
                elif posicion > len(abecedario):
                    nueva_posicion = cantidad_total - len(abecedario)
                    cifrado += abecedario[nueva_posicion]
                    cifrado += abecedario[posicion_lista_abcedario - posicion]
            else:
                cifrado += " "
    print(cifrado)
    

cifrado_cesar(10, "vñ pecdk vemqy uk zrjjk",True)
cifrado_cesar(5, "me gusta mucho la pizza", False)
print()
cifrado_cesar(7, "hola mundo", False)
cifrado_cesar(7, "ÑVRH SBTKV", True)