### Reto 4 ###

"""
  Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
  Ejemplos:
  - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
  - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 
 """

def fibonacci(num):
  ant=0
  post=1
  fib=[ant,post]
  
  for i in range (0,num):
      result=ant+post
      ant=post
      post=result
      fib.append(result)
  for i in fib:
      if i==num:
        fibo="es fibonacci"
        break
      else:
         fibo="no es fibonacci"
  return fibo
  

def par(num):
  if num%2==0:
      is_pair="y es par"
  else:
      is_pair="y es impar"
  return is_pair

def es_primo(num):
    global is_cousin
    if num<=2 and num>0:
        is_cousin="es primo"
    else:
        for n in range(2, num):
            if num % n == 0:
                is_cousin="no es primo"
                break
            else:
                is_cousin="es primo"
    return is_cousin
     
try:
  question=0
  while True:
    num = int(input("Ingrese un número: "))

    es_fibo=fibonacci(num)
    es_par=par(num)
    primo=es_primo(num)
  
    print (f"El número {num} {primo} , {es_fibo} {es_par}")
   

except ValueError:
    print ("No es un número válido")
finally:
   print ("Finaliza la ejecición")

        

