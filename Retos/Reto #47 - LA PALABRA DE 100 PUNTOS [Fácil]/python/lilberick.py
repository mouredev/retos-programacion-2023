def valorCaracter(c):
    t='abcdefghijklmnñopqrstuvwxyz'
    if(c.isalpha()): return t.find(c)+1
    return -1;
def valorPalabra(s):
    if(s.isalpha()):
        suma=0
        for i in s: suma+=valorCaracter(i)
        return suma
    return -1
def leer_datos():
    indicaciones="Ingresa una palabra o palabras cuyos caracteres pertenezan al abecedario español:\n"
    entrada = input(indicaciones).split()
    return entrada

def juego():
  finaliza=False
  while not finaliza:
    entrada = leer_datos() 
    for i in entrada:
        print(i,end=": ")
        valor=valorPalabra(i)
        if(valor==-1): print("palabra incorrecta, solo usa letras del abecedario español.")
        else:
            if(valor==100): print(valor,"Puntos. Felicidades palabra de 100 puntos. Finalizamos el programa")
            else: print(valor,"Puntos. Si hay una palabra de 100 puntos finaliza el programa.")
        if(valor==100): finaliza=True
    print()
juego()
