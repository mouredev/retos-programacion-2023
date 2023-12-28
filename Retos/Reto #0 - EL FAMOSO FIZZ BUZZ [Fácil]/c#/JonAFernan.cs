using System;

/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

public class Program
{
  public static void Main()
  {
    for (int x= 1; x<= 100; x++) {

      if (x%3 == 0 && x%5 == 0) Console.WriteLine("fizzbuzz");
      else if(x%3 == 0) Console.WriteLine("fizz");
      else if(x%3 == 0) Console.WriteLine("buzz");
      else Console.WriteLine(x);
    }
  }
}
