#Solucion FIZZ BUZZ - Reto 0

for fizz_buzz in range(1, 101):

    if fizz_buzz % 15 == 0:
        print("FizzBuzz")                                        
        continue

    elif fizz_buzz % 3 == 0:
        print("Fizz")
        continue

    elif fizz_buzz % 5 == 0:        
        print("Buzz")                                    
        continue


    print(fizz_buzz)