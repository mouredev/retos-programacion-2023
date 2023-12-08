from pprint import pprint


def sumas_recursiva(lista: list, objetivo: int) -> list:
    lista = list(filter(lambda x: x <= objetivo, lista))

    def auxiliar(lista: list, res: list, objetivo: int):
        for e in res.copy():
            aux = e.copy()
            aux.append(lista[0])
            if sum(aux) <= objetivo:
                res.append(aux)
        res.append([lista[0]])
        if len(lista) != 1:
            auxiliar(lista[1:], res, objetivo)

    resultado = list()
    auxiliar(lista, resultado, objetivo)
    return list(filter(lambda x: sum(x) == objetivo, resultado))


pprint(sumas_recursiva([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
pprint(sumas_recursiva([1, 5, 3, 2], 6))


def sumas_iterativa(lista: list, objetivo: int) -> list:
    res = list()
    lista = list(filter(lambda x: x <= objetivo, lista))
    for n in lista:
        for e in res.copy():
            aux = e.copy()
            aux.append(n)
            if sum(aux) <= objetivo:
                res.append(aux)
        res.append([n])
    return list(filter(lambda x: sum(x) == objetivo, res))


pprint(sumas_iterativa([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
pprint(sumas_iterativa([1, 5, 3, 2], 6))
