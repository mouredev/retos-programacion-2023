from random import randint
from threading import Timer
from os import _exit

def end_game(i):
    print(" /\nTiempo!! ")
    print("Nº respuestas correctas: " + str(i))  
    _exit(0)

def get_number(num_digits):
    #Create a random number with num_digits digits 
    max_number = (10** num_digits) - 1
    return randint(1,max_number)


def game():
    lv_end = False
    number_digit1 = 1
    number_digit2 = 1
    num_correct = 0

    while not(lv_end):
        #Get numbers
        a = get_number(number_digit1)
        b = get_number(number_digit2)
        #Calculate operation
        random = randint(0,3)
        result = 0

        if random == 0:
            result = a + b
            print("Operacion: " + str(a) + " + " + str(b))
        elif random == 1:
            result = a-b
            print("Operacion: " + str(a) + " - " + str(b))
        elif random == 2:
            result = a*b
            print("Operacion: " + str(a) + " * " + str(b))
        elif random == 3:
            result = a//b
            print("Operacion: " + str(a) + " / " + str(b))     
        #Set a 3 seconds timer     
        t = Timer(3.0,end_game,[num_correct])
        t.start()       
        user_input = int(input("Resultado: "))
        t.cancel()

        if result != user_input:
            #Incorrect answer --> cancel execution
            lv_end = True
        else: 
            num_correct += 1    

            if num_correct % 5 == 0:
            #5 questions have been answered correctly
                if number_digit1 == number_digit2:
                    number_digit1 += 1
                elif number_digit2 < number_digit1:    
                    number_digit2 += 1 
    print("Nº respuestas correctas: " + str(num_correct))            
                    

game()    