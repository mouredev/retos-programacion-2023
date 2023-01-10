#Reto de programación #0

for i in range(0,100):
    n = i+1
    if n % 3 == 0:
        t = "fizz"
        if n % 5 == 0:
            t = "fizzbuzz"
            print( t )
        else:
            print ( t )
    else:
        if n %5 == 0:
            t = "buzz"
            print ( t )
        else:
            print (n)