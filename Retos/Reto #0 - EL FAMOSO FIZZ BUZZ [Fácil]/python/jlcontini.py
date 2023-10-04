# Reto #0: EL FAMOSO "FIZZ BUZZ"
#### Dificultad: Fácil | Publicación: 26/12/22 | Corrección: 02/01/23

## Enunciado
"""
```
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
```
#### Tienes toda la información extendida sobre los retos de programación semanales en **[retosdeprogramacion.com/semanales2023]
(https://retosdeprogramacion.com/semanales2023)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.
"""


fizz = "fizz"
buzz = "buzz"


def is_multiple(number: int, multiple: int) -> bool:
  return number % multiple == 0


def print_numbers_in_range(a, b) -> str:
  for i in range(a, b+1):
    if is_multiple(i, 3) and is_multiple(i, 5):
      print(fizz + buzz + "\n")
    elif is_multiple(i, 3):
      print(fizz + "\n")
    elif is_multiple(i, 5):
      print(buzz + "\n")
    else:
      print(str(i) + "\n")


def main():
  print_numbers_in_range(1, 100)



if __name__ == "__main__": 
  main()
