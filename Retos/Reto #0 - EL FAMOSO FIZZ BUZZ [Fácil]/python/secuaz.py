#Funcion FizzBuzz
def fizzBuzz(int):
    if int %3 == 0 and int %5 == 0:
        return "FizzBuzz"
    elif int %5 == 0:
        return "Buzz"
    elif int %3 == 0:
        return "Fizz"
    else:
        return int

#Loop que imprime en el rango de 1 a 100 Fizz, Buzz o FizzBuzz segun corresponda
for i in range(1, 101):
    print (fizzBuzz(i))

