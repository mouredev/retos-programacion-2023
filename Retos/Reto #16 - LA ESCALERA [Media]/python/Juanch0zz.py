
number = int(input("Enter a number: "))
contador = number * 2
contador2 = -1


if number < 0:
    print("_")

    for i in range(abs(number)):
        contador2 += 2

        print(" "*contador2 + "|_")
        
    
        
    




if number > 0:
    print(" "*contador + "_")
    for i in range(number):
        contador -= 2

        print(" "*contador + "_|")
        







else:
    print("__")
