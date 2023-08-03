def dibuja_escalones(n: int):
    if n > 0:
        print('  '*n+'_')
        for i in range(n):
            print('  '*(n-i-1)+'_|')
    elif n < 0:
        print('_')
        for i in range(abs(n)):
            print('  '*(i)+' |_')
    else:
        print('__')

dibuja_escalones(-4)