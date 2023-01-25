
# Online Python - IDE, Editor, Compiler, Interpreter
import math

def isPrime(num):
    for i in range (2,num):
        if num % i == 0:
            return "No"
    return "Si"
    
def isPair(num):
    if num % 2 == 0:
        return "Si"
    return "No"
  
def isFibonacci(num):
    count = 0
    fibo1, fibo2 = 0,1
    while count < num:
        final = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = final
        count +=1
        areturn = "Si" if final == num else ""
        if areturn != "":
            return areturn
    return "No"

def checkNumber(num):
    print (num," \n",isPrime(num)," es primo \n" ,isPair(num)," es par \n",isFibonacci(num)," es fibonacci \n")
    

checkNumber(1)
checkNumber(3)
checkNumber(4)
checkNumber(5)
checkNumber(8)
checkNumber(13)
checkNumber(100)
checkNumber(34)
checkNumber(141)
