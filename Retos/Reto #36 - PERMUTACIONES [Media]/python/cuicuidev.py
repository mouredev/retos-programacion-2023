import itertools

def solution(string):
    characters = [x for x in string]
    permutations = itertools.permutations(characters, len(characters))
    
    for x in permutations:
        print(''.join(x))