import itertools

def permutaciones(palabra: str):
    pal = ""
    lista_palabras = list(itertools.permutations(palabra))
    for palabras in lista_palabras:
        pal = ",".join(palabras)
        print(pal.replace(",",""))
            


permutaciones("sol")
permutaciones("python")