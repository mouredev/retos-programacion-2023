/*
* Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
* Podrás configurar generar contraseñas con los siguientes parámetros:
* - Longitud: Entre 8 y 16.
* - Con o sin letras mayúsculas.
* - Con o sin números.
* - Con o sin símbolos.
* (Pudiendo combinar todos estos parámetros entre ellos)
*/
using System;

namespace Soluciones
{
  class Reto_03
  {
    static readonly string lowerChars = "abcdefghijklmnñopqrstuvwxyz";
    static readonly string upperChars = "ABCDEFGHYJKLMNÑOPQRSTUVWXYZ";
    static readonly string numberChars = "0123456789";
    static readonly string specialChars = "\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";
    static readonly Random rand = new();

    // Lee la pulsacion de la tecla Y o N por consola y devuelve un booleano
    static bool ReadYesOrNo(string question)
    {
      Console.Write(question);
      ConsoleKeyInfo keyPressed;
      do
      {
        keyPressed = Console.ReadKey(true);
      } while (keyPressed.Key != ConsoleKey.Y && keyPressed.Key != ConsoleKey.N);
      Console.WriteLine(keyPressed.KeyChar);
      return keyPressed.Key == ConsoleKey.Y;
    }

    // Solicita la longitud de la password por consola
    static int ReadPassLenght()
    {
      int passLength;
      do
      {
        Console.Write("¿Longitud? (8-16): ");
        string input = Console.ReadLine() ?? "0";
        if (!int.TryParse(input, out passLength)) passLength = 0;
        if (passLength < 8 || passLength > 16) Console.WriteLine("Longitud incorrecta!");
      } while (passLength < 8 || passLength > 16);
      return passLength;
    }

    // Elige un caracter aleatorio de la cadena recibida
    static char GetRandomCharFrom(string origin)
    {
      int index = rand.Next(0, origin.Length);
      return origin[index];
    }

    // Baraja el string, reordenando de forma aleatoria los caracteres
    static string ShufflePassword(string password)
    {
      char[] newPassword = password.ToCharArray();
      for (int index = 0; index < password.Length; index++)
      {
        int newIndex = rand.Next(0, password.Length);
        (newPassword[newIndex], newPassword[index]) = (newPassword[index], newPassword[newIndex]);
      }
      return new string(newPassword);
    }

    // El algoritmo asegura al menos un caracter de cada tipo solicitado. Para ello realiza lo siguiente:
    // Incluir una minuscula
    // Incluir una mayuscula (si corresponde)
    // Incluir un numero (si corresponde)
    // Incluir un caracter especial (si corresponde)
    // Rellenar el resto de posiciones con caracteres aleatorios de cualquiera de los tipos solicitados
    // Barajar todos los caracteres de la password, de modo que los primeros incluidos se mezclen
    static string GeneratePassword(int lenght, bool upper, bool numbers, bool special)
    {
      string password = "";
      string fullCharSet = "";

      // Como minimo pondremos un caracter de cada tipo seleccionado. El resto seran random.
      // Los ponemos al principio, ya que al final barajaremos todos los caracteres.
      password += GetRandomCharFrom(lowerChars);
      fullCharSet += lowerChars;
      if (upper)
      {
        password += GetRandomCharFrom(upperChars);
        fullCharSet += upperChars;
      }
      if (numbers)
      {
        password += GetRandomCharFrom(numberChars);
        fullCharSet += numberChars;
      }
      if (special)
      {
        password += GetRandomCharFrom(specialChars);
        fullCharSet += specialChars;
      }

      // Una vez incluido un caracter de cada tipo, rellenamos el resto de la password.
      do
      {
        password += GetRandomCharFrom(fullCharSet);
      } while (password.Length < lenght);

      // Barajamos los caracteres para conseguir entremezclar los primeros incluidos con el resto
      // Console.WriteLine(password); // Antes de barajar
      password = ShufflePassword(password);

      return password;
    }

    static public void Main()
    {
      int passLenght = ReadPassLenght();
      bool flagUpper = ReadYesOrNo("¿Mayusculas? (y/n): ");
      bool flagNumbers = ReadYesOrNo("¿Numeros? (y/n): ");
      bool flagSpecial = ReadYesOrNo("¿Caracteres especiales? (y/n): ");

      Console.WriteLine(GeneratePassword(passLenght, flagUpper, flagNumbers, flagSpecial));

      Console.ReadKey();
    }
  }
}