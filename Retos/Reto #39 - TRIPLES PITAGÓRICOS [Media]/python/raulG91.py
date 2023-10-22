from math import pow
def find_triples(max_number):
    triples = []
    for value in range(1,max_number+1):
        for value2 in range(value+1,max_number+1):
                sum = value**2 + value2**2
                square_root = sum **0.5

                if square_root.is_integer() and square_root <= max_number:
                    tuple = (value,value2,int(square_root))
                    triples.append(tuple)
    return triples

result = find_triples(max_number=50)
print(result)