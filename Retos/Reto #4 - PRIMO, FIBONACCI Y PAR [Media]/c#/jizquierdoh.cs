using System;

namespace ConsoleApp1
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.Write("Introduce un número: ");
      int numero = int.Parse(Console.ReadLine());

      if (EsPrimo(numero))
      {
        Console.Write(numero + " es primo, ");
      }
      else
      {
        Console.Write(numero + " no es primo, ");
      }

      if (EsFibonacci(numero))
      {
        Console.Write("es fibonacci, ");
      }
      else
      {
        Console.Write("no es fibonacci, ");
      }

      if (EsPar(numero))
      {
        Console.WriteLine("es par.");
      }
      else
      {
        Console.WriteLine("es impar.");
      }

      Console.ReadLine();
    }

    static bool EsPrimo(int n)
    {
      if (n < 2)
      {
        return false;
      }
      for (int i = 2; i <= Math.Sqrt(n); i++)
      {
        if (n % i == 0)
        {
          return false;
        }
      }
      return true;
    }

    static bool EsFibonacci(int n)
    {
      int a = 0, b = 1;
      while (b < n)
      {
        int c = a;
        a = b;
        b = a + c;
      }
      return b == n;
    }

    static bool EsPar(int n)
    {
      return n % 2 == 0;
    }
  }
}
