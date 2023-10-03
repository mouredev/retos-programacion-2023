#!/usr/bin/env python3

def is_pitagoric_triple(triple):
    return (triple[0]**2 + triple[1]**2 == triple[2]**2)

def calculate_pitagoric_triple(max):
    triples = []

    for i in range(1, max+1):
        for j in range(1, max+1):
            for k in range(1, max+1):
                t = [i,j,k]
                t = sorted(t)
                if is_pitagoric_triple(t) and t not in triples:
                    triples.append(t)
    return triples

if __name__ == "__main__":
    print(calculate_pitagoric_triple(10))
    print(calculate_pitagoric_triple(100))
