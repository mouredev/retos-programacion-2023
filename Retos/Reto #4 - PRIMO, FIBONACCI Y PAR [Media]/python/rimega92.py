# Escribe un programa que, dado un número, compruebe y muestre si es primo,
# fibonacci y par.
# Ejemplos:
# - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"


def primo(n):
      if n < 2:
         return False
      for i in range(2, n):
         if n % i == 0 and n != i:
               return False
      return True

def fibonacci(n):
      a = 0
      b = 1
      for i in range(n):
         c = a + b
         a = b
         b = c
         if n == a:
               return True
      return False

def par(n):
      if n % 2 == 0:
         return True
      else:
         return False
      

def main():
   n = int(input("Ingrese un número: "))
   is_prime = primo(n)
   is_fibonacci = fibonacci(n)
   is_even = par(n)

   if is_prime and is_fibonacci and is_even:
      print(f"{n} es primo, fibonacci y es par")
   elif is_prime and not is_fibonacci and is_even:
      print(f"{n} es primo, no es fibonacci y es par")
   elif is_prime and not is_fibonacci and not is_even:
      print(f"{n} es primo, no es fibonacci y es impar")
   elif not is_prime and not is_fibonacci and is_even:
      print(f"{n} no es primo, no es fibonacci y es par")
   elif not is_prime and not is_fibonacci and not is_even:
      print(f"{n} no es primo, no es fibonacci y es impar")
   elif not is_prime and is_fibonacci and is_even:
      print(f"{n} no es primo, es fibonacci y es par")
   elif not is_prime and is_fibonacci and not is_even:
      print(f"{n} no es primo, es fibonacci y es impar")
   elif is_prime and is_fibonacci and not is_even:
      print(f"{n} es primo, es fibonacci y es impar")

if __name__ == '__main__':
   main()