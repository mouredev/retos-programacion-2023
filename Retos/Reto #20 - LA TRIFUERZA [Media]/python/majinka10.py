def primero(n:int):
    for i in range(n):
        print(' ' * (2*n-i-1) + '*' * (2*i+1))

def segundo(n:int):
    for i in range(n):
        print(' ' * (n-i-1) + '*' * (2*i+1) + ' ' * (2*n- (i*2) -1) + '*' * (2*i+1))

def trifuerza(n:int):
    primero(n)
    segundo(n)
    
trifuerza(5)