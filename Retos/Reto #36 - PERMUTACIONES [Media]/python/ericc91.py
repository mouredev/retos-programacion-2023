from itertools import permutations

def permutacion (palabra):
    permutaciones = permutations(palabra,len(palabra))
    for p in permutaciones:
        print("".join(p)) 
