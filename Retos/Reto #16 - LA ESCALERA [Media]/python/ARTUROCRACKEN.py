# funcion para printear escalera

def escalera(n):

    if n > 0:
        for i in range(0, n+1):
            if i != 0:
                print('  '*(n-i) + '_|')
            else:
                print('  '*(n-i) + '_')
    elif n < 0:
        for i in range(0, -n+1):
            if i != 0:
                print(' '*((i*2)-1) + '|_')
            else:
                print('_')
    else:
        print('__')

print('Ascendente:')
escalera(4)
print('\nDescendente:')
escalera(-4)
print('\n0:')
escalera(0)
