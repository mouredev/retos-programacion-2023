import sys

def heterograma(w):
    for i in w:
        if w.count(i) != 1:
            return('No es un heterograma')
    return('Es un heterograma, por lo tanto un isograma de primer orden')


def isograma(w):
    c = [w.count(i) for i in w]
    if c.count(c[0]) == len(c):
        return('Es un isograma de orden {}'.format(c[0]))
    else:
        return('No es un isograma')

def panagrama(w):
    alphabet_low = list(map(chr, range(97, 123)))
    alphabet_cap = list(map(chr, range(65, 91)))
    special  = ['á', 'é', 'í', 'ó', 'ú', 'ü', 'ñ', '.', ',', ' ']
    for i in w:
        if i not in alphabet_low+alphabet_cap+special:
            return('No es un panagrama')
    return('Es un panagrama')


if __name__ == '__main__':
    w_heterograma = sys.argv[1]
    w_isograma    = sys.argv[2]
    w_panagrama   = sys.argv[3]

    print(heterograma(w_heterograma))
    print(isograma(w_isograma))
    print(panagrama(w_panagrama))
