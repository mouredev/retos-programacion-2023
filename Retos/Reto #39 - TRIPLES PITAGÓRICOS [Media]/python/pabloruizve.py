def triples_pitagoricos(x):
    print('Los triples menores o iguales a',x,'estan formados por:')
    for a in range(1,x+1):
        for b in range(a+1,x+1):
            for c in range(b+1,x+1):
                if c != a and c != b:
                    if a**2 + b**2 == c**2:
                        triple = [a,b,c]
                        print(triple)

triples_pitagoricos(50)