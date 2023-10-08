def triples_pitagoricos(maximo):
    resultados = []
    for a in range(1, maximo + 1):
        for b in range(a, maximo + 1):
            c_cuadrado = a**2 + b**2
            c = int(c_cuadrado**0.5)
            if c <= maximo and c_cuadrado == c**2:
                resultados.append((a, b, c))
    return resultados

print(triples_pitagoricos(100))