using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FizzBuzzReto0
{
    internal class Program
    {
        private static int _totalNumbers = 100;

        /// <summary>
        /// Main method
        /// </summary>
        /// <param name="args"></param>
        static void Main(string[] args)
        {
            for (int i= 1; i <= _totalNumbers; i++)
            {
                CheckNumber(i); 
            }
            
            Console.WriteLine("End program!");
            Console.ReadKey();  
        }


        /// <summary>
        /// Method for check the numbers
        /// </summary>
        /// <param name="number"></param>
        private static void CheckNumber(int number)
        {
            if (number % 3 == 0 && number % 5 == 0)
                Console.WriteLine($"Number: {number} - FizzBuzz");
            else if (number % 3 == 0)
                Console.WriteLine($"Number: {number} - Fizz");
            else if (number % 5 == 0)
                Console.WriteLine($"Number: {number} - Buzz");
            else
                Console.WriteLine($"Number: {number}");
        }
    }
}
