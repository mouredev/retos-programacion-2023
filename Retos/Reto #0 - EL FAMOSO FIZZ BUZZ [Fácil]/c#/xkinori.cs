namespace retos_programacion2023__0
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Escribe un programa que muestre por consola (con un print) los\r\n" +
                "números de 1 a 100 (ambos incluidos y con un salto de línea entre\r" +
                "\ncada impresión), sustituyendo los siguientes:\r" +
                "\nMúltiplos de 3 por la palabra \"fizz\".\r" +
                "\nMúltiplos de 5 por la palabra \"buzz\".\r" +
                "\nMúltiplos de 3 y de 5 a la vez por la palabra \"fizzbuzz\".\r\n");
            Console.WriteLine("====================================================================\n");

            for (int i = 1; i <= 100; i++)
            {

                if (i % 5 == 0 && i % 3 == 0)
                {
                    Console.WriteLine($"fizzbuzz!!\n");
                }
                else if (i % 3 == 0)
                {
                    Console.WriteLine($"FIZZ!!\n");
                }
                else if (i % 5 == 0)
                {
                    Console.WriteLine($"BUZZ!!\n");
                }
                else { Console.WriteLine($"{i}\n"); }

            }
        }
    }
}