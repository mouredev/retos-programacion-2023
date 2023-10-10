"""
Reto 4: Primo, Fibonacci y Par
Escribe un programa que, dado un número, compruebe y muestre si es primo,
fibonacci y par.
Ejemplos:
- Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
- Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""

def is_prime(number):
  if number > 1:
    for i in range(2, number):
      if (number % i) == 0:
        return False 

      else:
        return True

  else:
    return False

def is_even(number):
  if (number % 2 )== 0:
    return True

  else:
    return False

def is_fibonacci(number):
  n1, n2 = 0, 1

  is_in_fibo = False

  while number > n2:    
    n1 = n1 + n2
    n2 = n1 + n2

    if n2 == number or n1 == number:
      is_in_fibo = True

    else:
      is_in_fibo = False
  return is_in_fibo

if __name__ == "__main__":
  while True:
    number = 0
    try:
      number = int(input('Inserta un numero a verificar: '))

    except ValueError:
      print("Inserta un valor valido!")

    if number < 1:
      break

    is_prime_txt = f"{number} es primo" if is_prime(number) else f"{number} no es primo"
    is_fibo_txt = f", fibonacci" if is_fibonacci(number) else f", no es fibonacci"
    is_even_txt = f"y es par" if is_even(number) else f"y es impar"
    text = f"{is_prime_txt} {is_fibo_txt} {is_even_txt}"
    print(text)
    number = 0