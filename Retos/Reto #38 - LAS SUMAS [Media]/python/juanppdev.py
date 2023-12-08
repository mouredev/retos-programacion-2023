from itertools import combinations

def encontrar_combinaciones(lista, objetivo):
    soluciones = []
    for r in range(1, len(lista) + 1):
        for combo in combinations(lista, r):
            if sum(combo) == objetivo:
                soluciones.append(list(combo))
    return soluciones

# Ejemplo de uso:
lista = [1, 2, 3, 4, 5, 6]
objetivo = 12
resultados = encontrar_combinaciones(lista, objetivo)
print(resultados)