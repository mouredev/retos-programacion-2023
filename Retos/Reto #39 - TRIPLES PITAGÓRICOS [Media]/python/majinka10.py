def getTerna(number: int):
    """
    Encuentra todas las ternas pitagóricas donde a, b y c son menores 
    o iguales que un numero. 

    Args:
    - number (int): Numero máximo que puede aparecer en el triple.
    Returns:
    - ternas (list): Lista con las ternas encontradas. La lista solo contiene
    ternas (a, b, c) que no son múltiplos de otras ternas, (na, nb, nc) no 
    aparecen en la lista.
    """
    ternas = []
    for n in range(1, number):
        for m in range(1, number):
            if m > n:
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                if c > number:
                    break
                ternas.append([a, b, c])
    return ternas

print(getTerna(15))
print(getTerna(10))
print(getTerna(5))
