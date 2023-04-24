
def  fizzBazz ():
    for  number  in  range ( 1 , 101 ):
        if  number  %  3  ==  0  and  number  %  5  ==  0 :
            print("fizzbazz" )
        elif number %  5  ==  0 :
            print( "bazz" )
        elif number  %  3  ==  0 :
            print( "fizz")
        else :
            print(number)
    
    
if  __name__ == "__main__" :

    fizzBazz ()