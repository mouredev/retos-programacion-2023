def encontrar_numeros_pitagoricos(n):

    triples = []
    for a in range(1, n +1):
        for b in range(a, n + 1):
            c = (a**2 + b**2)**0.5
            if c.is_integer() and c <= n:
                triples.append((a, b, int(c)))
    return triples

numero_limite = int(input("Introduce un número para buscar sus Triples Pitagóricos: "))
triples_pitagoricos = encontrar_numeros_pitagoricos(numero_limite)

print(f"Triples Pitagoricos menos o iguales a {numero_limite} ")

for triple in triples_pitagoricos:
    print(triple)

    