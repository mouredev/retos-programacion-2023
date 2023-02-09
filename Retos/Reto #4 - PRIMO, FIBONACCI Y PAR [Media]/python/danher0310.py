def fibonacci_of(n):
  cache = {0: 0, 1: 1}
  if n < 2:  # Base case
    return n
  cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  
  return cache[n]


def eval_fibo(num):
  
  sequenci = [fibonacci_of(n) for n in range(num+1)]  
  print(sequenci)
  return True if num in sequenci else False
  
def is_prime(num):
  if num > 2:
    for i in range(2,num):    
      return False if num%i == 0 else True
  else: 
    return False

def is_par(num):
  return True if num%2 ==0 else False



def eval_condition():
  num = input("Introduzca un numero: ")
  if num.isnumeric(): 
    num = int(num)
    msj =""
    msj += f"{num} es Fibonacci\n" if eval_fibo(num) else f"{num} No es Fibonacci \n"
    msj += f"{num} es Primo\n" if is_prime(num) else f"{num} No es primo \n"
    msj += f"{num} es Par\n" if is_par(num) else f"{num} No es par \n"
    return msj
    
    
  else:
    print("Introduzca un numero entero para poder ser envaluado")
    return eval_condition()

print(eval_condition())


