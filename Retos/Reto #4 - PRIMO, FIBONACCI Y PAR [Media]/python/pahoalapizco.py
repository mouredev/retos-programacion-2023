
def es_par(num):
  return num % 2 == 0    

def es_multiplo(num, divisor):
  return num % divisor == 0

def fibonacci(num, memo = {}):
  if num == 0 or num == 1:
    return 1

  try:
    return memo[num]  
  except KeyError:
    resultado = fibonacci(num - 1) + fibonacci(num - 2)
    memo[num] = resultado
    return resultado

def es_primo(num):
  if num != 2 and num % 2 == 0:
    return False  
  
  proxima_riz = round((num**0.5) + 1)
  n = proxima_riz
  while n > 1:
    if es_multiplo(num, n) and n != proxima_riz:
      return False
      
    n -= 1

  return True
    
def es_fibonacci(numero):
  esfib = False
  for num in range(numero+1):
    fib = fibonacci(num)
    
    if fib == numero:
      esfib = True
      break
  
  return esfib


if __name__ == '__main__':
  num = int(input('Escribe un número: '))
  primo = es_primo(num)
  esfib = es_fibonacci(num)
  par = es_par(num)
  print(f'{num}{" es" if primo else " no es"} primo,{" es" if esfib else " no es"} fibonacci y es {"par" if par else "impar"}')

  """  - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar" """