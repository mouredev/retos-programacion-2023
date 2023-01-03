class Reto0
{
    static void Main(string[] args)
    {
        for (int i = 1; i < 101; i++)
        {
            int múltiplo1 = i % 3;
            int múltiplo2 = i % 5;
    
            if ((múltiplo1 == 0) && (múltiplo2 == 0))
            {
            Console.WriteLine( i + "FizzBuzz");
            }
            else if (múltiplo1 == 0)
            {
            Console.WriteLine(i + "Fizz");
            }
            else if (múltiplo2 == 0)
            {
            Console.WriteLine(i + "Buzz");
            }
            else
            {
            Console.WriteLine(i);
            }
        }
    }
}
