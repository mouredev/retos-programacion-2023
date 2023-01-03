/*
* Escribe un programa que muestre por consola (con un print) los
* números de 1 a 100 (ambos incluidos y con un salto de línea entre
* cada impresión), sustituyendo los siguientes:
* - Múltiplos de 3 por la palabra "fizz".
* - Múltiplos de 5 por la palabra "buzz".
* - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
*/

namespace Soluciones
{
  class Reto_00
  {
    static public void Main(String[] args)
    {
      for (int i = 1; i <= 100; i++)
      {
        bool isMult3 = i % 3 == 0;
        bool isMult5 = i % 5 == 0;

        string message = isMult3 && isMult5 ? "fizzbuzz" :
                          isMult3 ? "fizz" :
                          isMult5 ? "buzz" :
                          i.ToString();

        Console.WriteLine(message);
      }

      Console.ReadKey();
    }
  }
}