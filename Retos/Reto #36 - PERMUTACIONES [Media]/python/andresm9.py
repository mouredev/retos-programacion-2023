import sys, itertools

def print_permutations(input):
  if input:
    permutations = itertools.permutations(input)
    for p in permutations:
      print("".join(p))

input = "Hola"
print_permutatins(input)
"""
it should print this words:
Hola
Hoal
Hloa
Hlao
Haol
Halo
oHla
oHal
olHa
olaH
oaHl
oalH
lHoa
lHao
loHa
loaH
laHo
laoH
aHol
aHlo
aoHl
aolH
alHo
aloH
"""
