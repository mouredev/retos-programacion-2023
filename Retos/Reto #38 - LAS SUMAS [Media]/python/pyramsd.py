def searchCombo(lista,objetivo):
    def rev(restante, combActual, initIndex):
        if restante == 0:
            result.append(combActual[:])
            return
        if restante < 0:
            return
        for i in range(initIndex, len(lista)):
            combActual.append(lista[i])
            rev(restante - lista[i], combActual, i + 1)
            combActual.pop()

    result = []
    rev(objetivo, [], 0)
    return result

lista=[1,5,3,2,4]
objetivo=10
print(searchCombo(lista, objetivo))