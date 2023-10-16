def encontrar_triples_pitagoricos(numero):
    triples = []
    for a in range(1, numero + 1):
        for b in range(a, numero + 1):
            c = (a**2 + b**2)**0.5
            if c.is_integer() and c <= numero:
                triples.append((a, b, int(c)))
    return triples

print(encontrar_triples_pitagoricos(10))