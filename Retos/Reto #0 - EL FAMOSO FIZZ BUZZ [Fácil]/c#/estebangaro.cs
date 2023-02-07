/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
for (byte i = 1, m3 = (byte)(i%3), m5 = (byte)(i%5); i <= 100; i++, m3 = (byte)(i % 3), m5 = (byte)(i % 5))
{
    Console.WriteLine(m3 == 0 && m5 == 0 ? "fizzbuzz" : m3 == 0 ? "fizz" : m5 == 0 ? "buzz" : i);
}