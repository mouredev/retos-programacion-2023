/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

for (int valueNumber = 1; valueNumber <= 100; valueNumber++)
{
  string valueString = "";

  if (valueNumber % 3 == 0)
    valueString += "Fizz";

  if (valueNumber % 5 == 0)
    valueString += "Buzz";

  Console.WriteLine(
    valueString == string.Empty
      ? valueNumber
      : valueString
  );
}
