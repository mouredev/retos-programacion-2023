from pprint import pprint

def partes_recursiva(lista: list) -> list:
    def auxiliar(lista: list, res: list):
        for e in res.copy():
            aux = e.copy()
            aux.append(lista[0])
            res.append(aux)
        res.append([lista[0]])
        if len(lista) != 1:
            auxiliar(lista[1:], res)
    resultado = list()
    auxiliar(lista, resultado)
    return resultado

pprint(partes_recursiva([1, 2, 3, 4, 5]))
