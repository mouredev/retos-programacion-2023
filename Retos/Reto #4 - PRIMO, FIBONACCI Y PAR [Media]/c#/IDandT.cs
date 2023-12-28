/*
* Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
* Ejemplos:
* - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
* - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
*/
using System;
using System.Text;

namespace Soluciones
{
  class Reto_04
  {
    static bool IsPrime(int number)
    {
      int timesOk = 0;
      for (int i = 1; i <= number; i++)
      {
        if (number % i == 0)
        {
          timesOk++;
        }
      }
      return timesOk == 2;
    }

    static bool IsPair(int number)
    {
      return number % 2 == 0;
    }

    static bool IsFibonacci(int number)
    {
      if (number == 1) return true;

      int prev = 1;
      int current = 1;
      int next;

      while (current <= number)
      {
        next = current + prev;
        prev = current;
        current = next;
        if (current == number) return true;
      }

      return false;
    }

    static void CheckNumber(int number)
    {
      StringBuilder message = new($"El numero {number} ");
      message.Append(
          IsPrime(number) ? "es primo, " : "no es primo, ").Append(
          IsFibonacci(number) ? "es Fibonacci " : "no es Fibonacci ").Append(
          IsPair(number) ? "y es par." : "y es impar."
        );
      Console.WriteLine(message);
    }

    static public void Main()
    {
      CheckNumber(2);
      CheckNumber(7);
      CheckNumber(13);
      CheckNumber(33);
      CheckNumber(34);
      CheckNumber(89);
      CheckNumber(144);
      CheckNumber(146);

      Console.ReadKey();
    }
  }
}