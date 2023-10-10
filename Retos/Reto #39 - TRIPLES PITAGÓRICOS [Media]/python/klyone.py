#!/usr/bin/env python3

def is_pitagoric_triple(triple):
    return (triple[0]**2 + triple[1]**2 == triple[2]**2)

def calculate_pitagoric_triple(max):
    triples = []

    for i in range(1, max+1):
        for j in range(i+1, max+1):
            k = int((i**2 + j**2)**0.5)
            if k > max:
                break

            t = [i,j,k]
            t = sorted(t)
            if is_pitagoric_triple(t) and t not in triples:
                triples.append(t)
    return triples

if __name__ == "__main__":
    print(calculate_pitagoric_triple(10))
    print(calculate_pitagoric_triple(100))
    print(calculate_pitagoric_triple(1000))
    print(calculate_pitagoric_triple(10000))
