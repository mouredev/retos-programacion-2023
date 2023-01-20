x = 1
while x <= 100:
    
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz") 
    else:
        if x % 3 == 0:    
            print("fizz")  
        else:
            if x % 5 == 0:
                print("buzz") 
            else:
                print(x)

    x = x + 1