#Reto #0: EL FAMOSO "FIZZ BUZZ"
#Dificultad: Fácil 

counter = 1

print("****Fizz Buzz****")
while counter <= 100:
    if((counter % 3 == 0) and (counter % 5 == 0)):
        print("fizzbuzz")
    elif(counter % 5 == 0):
        print("buzz")
    elif(counter % 3 == 0):
        print("fizz")
    else:
        print(counter)
    counter+= 1
