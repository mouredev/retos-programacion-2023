

#This code makes a reverse count. The user can choose the number to begin and the seconds to wait between each number.

from time import sleep

number_to_count = input("Give me the number wich you want to begin: ")
seconds_to_wait = input("Give the seconds that you want to wait between each number: ")

def reverse_Count(number, seconds):
    cont=number

    if number < 0:
        return print("The number must be positive")
    
    for x in range(number+1): ## plus 1 in order to show 0 at last position 
        print(cont)
        sleep(seconds)
        cont=cont-1

reverse_Count(number_to_count, seconds_to_wait)

