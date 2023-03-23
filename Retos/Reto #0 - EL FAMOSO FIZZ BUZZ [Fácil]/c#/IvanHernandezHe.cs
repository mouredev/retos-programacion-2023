

namespace retos_de_programacion_2023
{
    class reto_00
    {
        static void Main()
        {
            Fizzbuzz(100);
            Console.ReadKey();
        }

        private static void Fizzbuzz(int limite)
        {
            for (int i = 1; i <= limite; i++)
            {
                string m = (( i % 3 == 0) && ( i % 5 == 0)) ? "fizzbuzz" : ( i % 3 == 0) ? "fizz" : ( i % 5 == 0) ? "buzz" : i.ToString() ;
                Console.WriteLine(m);
            }
        }
    }
}