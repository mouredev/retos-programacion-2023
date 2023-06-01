def snake(n:int):
    if n > 2:
        symbol = ['═',"║","╗","╝","╔","╚"]
        if n%2==0:
            ciclos = int(n/2-1)
        else:
            ciclos = int(n/2-0.5)
        print(symbol[0]*(n-1) + symbol[2])
        for i in range(1,ciclos+1):
            print(symbol[1]*(i-1) +
                symbol[4] + 
                symbol[0]*(n-i*2-1) + 
                symbol[2] + 
                symbol[1]*i)
        if n%2==0:
            print(symbol[1]*(ciclos) +
                symbol[0] + 
                symbol[3] + 
                symbol[1]*(ciclos))
        for i in range(ciclos, 0,-1):
            print(symbol[1]*(i-1) +
                symbol[5] + 
                symbol[0]*(n-i*2) + 
                symbol[3] + 
                symbol[1]*(i-1))

for x in range(0,11):
    print(x)    
    snake(x)
