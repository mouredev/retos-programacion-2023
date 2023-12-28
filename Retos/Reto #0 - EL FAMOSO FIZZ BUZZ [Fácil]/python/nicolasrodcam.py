print("EL FAMOSO FIZZ BUZZ \n")

for item in range(100):
    if (item %5 == 0 and item %3 == 0):
        print("fizzbuzz") 
    elif(item %5 == 0):
        print("buzz") 
    elif(item %3 == 0):
        print("fizz") 
    
