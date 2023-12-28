public static void reto0()
{
    /*
     * Escribe un programa que muestre por consola (con un print) los
     * números de 1 a 100 (ambos incluidos y con un salto de línea entre
     * cada impresión), sustituyendo los siguientes:
     * - Múltiplos de 3 por la palabra "fizz".
     * - Múltiplos de 5 por la palabra "buzz".
     * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
     */
    for (int i = 0; i <= 100; i++)
    {
        string result = "";
        if (i % 3 == 0)
        {
            result += "fizz";
        }
        if (i % 5 == 0)
        {
            result += "buzz";
        }
        if (result.Equals(""))
        {
            Console.WriteLine(i);
        } else
        {
            Console.WriteLine(result);
        }
    }
}
