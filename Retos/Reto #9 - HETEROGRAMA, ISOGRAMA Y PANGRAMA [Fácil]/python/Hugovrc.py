def heterograma(palabra):
    diccionario = {}
    contador = 0

    for letras in palabra.lower():
        if letras in diccionario:
            if diccionario[letras] == 1:
                contador += 1
            diccionario[letras] += 1
        else:
            diccionario[letras] = 1
    if contador == 0:
        print("La palabra es un Heterograma")   
    
heterograma("yuxtaponer")
heterograma("centrifugado")

def isograma(palabra):
    diccionario = {}


    for letras in palabra.lower():
        diccionario[letras] = diccionario.get(letras, 0) + 1
        if diccionario[letras] == 2:
            print("La Palabra es un Isograma")
            #print(diccionario)
            
            
    
    
isograma("shampoo")
isograma("escritura")

def pangrama(palabra):
    abecedario = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, 
                  "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, 
                  "q":0, "r":0, "s":0, "t":0, "u":0, "ü":0, "v":0, "w":0, 
                  "x":0, "y":0, "z":0}
    contador = 0
    
    for letras in palabra.lower():
        
        if letras in abecedario:
            abecedario[letras] = abecedario.get(letras, 0) + 1
            if abecedario[letras] == 1:
               
               contador +=1
            
    if contador == 27:        
        print("La Palabra es un pangrama")

pangrama("Benjamin pidio una bebida de kiwi y fresa. Noe, sin vergüenza, la mas exquisita champaña del menu")