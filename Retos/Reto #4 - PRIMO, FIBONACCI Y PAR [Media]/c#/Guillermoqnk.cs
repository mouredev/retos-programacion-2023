using System.Text;

namespace Reto04
{
    internal class Guillermoqnk
    {
        static void Main(string[] args)
        {
            string input;

            Console.WriteLine("Introduce a number to check if it is Fibonacci, even or prime: ");

            input = Console.ReadLine();

            try
            {
                var numberToCheck = Convert.ToInt32(input);

                StringBuilder output = new StringBuilder();

                output.Append($"{numberToCheck} {CheckEven(numberToCheck)}, {CheckFibonacci(numberToCheck)}, and {CheckPrime(numberToCheck)}");

                Console.WriteLine(output.ToString());                
            }
            catch(Exception ex)
            {
                Console.WriteLine("That's not a number.");
            }
        }

        private static string CheckFibonacci(int numberToCheck)
        {
            if (numberToCheck == 1)
                return "is fibonacci";

            int previousNumber = 1;
            int temp;

            for (int i = 1; i < numberToCheck; temp = previousNumber, previousNumber = i, i = temp+previousNumber )
            {
                int fiboToCheck = i + previousNumber;

                if(fiboToCheck > numberToCheck)
                {
                    return "is not fibonacci";
                }
                else if(fiboToCheck == numberToCheck)
                {
                    return "is fibonacci";
                }
            }

            return "is not fibonacci";
        }

        private static string CheckEven(int numberToCheck)
        {
            if(numberToCheck % 2 == 0)
            {
                return "is even";
            }
            else
            {
                return "is not even";
            }
        }

        private static string CheckPrime(int numberToCheck)
        {
            int counter = 0;

            for(int i = 1; i <= numberToCheck; i += 1)
            {
                if (numberToCheck % i == 0)
                    counter++;
            }

            if (counter == 2)
                return "is prime";
            else
                return "is not prime";
        }
    }
}