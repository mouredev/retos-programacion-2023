using System;

namespace Soluciones
{
  class Reto_00
  {
    static public void Main(String[] args)
    {
      // Declarar una variable para guardar el número actual.
      int numero_actual;

      // Iterar sobre los números del 1 al 100.
      for (numero_actual = 1; numero_actual <= 100; numero_actual++)
      {
        // Declarar variables booleanas para comprobar si el número actual es múltiplo de 3 o de 5.
        bool esMultiploDe3 = numero_actual % 3 == 0;
        bool esMultiploDe5 = numero_actual % 5 == 0;

        // Declarar una variable para guardar el mensaje a imprimir.
        string mensaje;

        // Comprobar si el numero actual es múltiplo de 3 y de 5 a la vez.
        if (esMultiploDe3 && esMultiploDe5)
        {
          mensaje = "fizzbuzz";
        }
        // Si no es múltiplo de 3 y de 5 a la vez, comprobar si es múltiplo de 3.
        else if (esMultiploDe3)
        {
          mensaje = "fizz";
        }
        // Si no es múlltiplo de 3, comprobar si es múltiplo de 5.
        else if (esMultiploDe5)
        {
          mensaje = "buzz";
        }
        // Si no es multiplo de 3 ni de 5 el mensaje es simplemente el número actual
        else
        {
          mensaje = numero_actual.ToString();
        }

        // Imprimir el mensaje con un salto de línea.
        Console.WriteLine(mensaje);
      }

      // Esperar a que el usuario pulse una tecla antes de salir.
      Console.ReadKey();
    }
  }
}
