from itertools import permutations

palabra = input("Palabra a permutar: ")

permutations_list = [''.join(p) for p in permutations(palabra)]

print(f'{palabra} -> {", ".join(permutations_list)}')
