# Reto #4: PRIMO, FIBONACCI Y PAR
#### Dificultad: Media | Publicación: 23/01/23 | Corrección: 30/01/23

## Enunciado

"""

```
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
```
#### Tienes toda la información extendida sobre los retos de programación semanales en **[retosdeprogramacion.com/semanales2023](https://retosdeprogramacion.com/semanales2023)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.

"""

# Titulo
print(''.center(70, '*'))
print(' Reto #04 - Primo, Fibonacci y Par '.center(70, '*'))
print(''.center(70, '*'))


def check_prime(number) -> bool:
  print("check_prime")
  
  if number in [0, 1]:
    return False
  
  for n in range (2, int(number/2)+1, 1):
    if number % n == 0:
      return False
  
  return True


def check_fibonacci(number) -> bool:
  print("check_fibonacci")
  
  fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811]
  
  if number <= 317811:
    return True if number in fibonacci_list else False
  else:
    num1, num2 = 196418, 317811
    fibonacci_list2 = []
    while num2 <= 300000000:
      fibonacci_list2.append(num1)
      fibonacci_list2.append(num2)
      num1 = num1 + num2
      num2 = num1 + num2

    return True if number in fibonacci_list2 else False


def check_even(number) -> bool:
  print("check_even")
  return True if number % 2 == 0 else False


def check_prime_fibonacci_even():
  
  number = int(input("\nEnter a integer number to check: \n"))
  
  result_prime = "es primo" if check_prime(number) == True else "no es primo"
  result_fibonacci = "es fibonacci" if check_fibonacci(number) == True else "no es fibonacci"
  result_even = "es par" if check_even(number) == True else "es impar"
  
  result = f"{number} {result_prime}, {result_fibonacci} y {result_even}."
  
  print(f"\n{result}\n")


def main():
  check_prime_fibonacci_even()


if __name__ == "__main__":
  main()