/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 * - Gracias moure por esto, eres una máquina SALUDOS!!!
 */
using System;

namespace Reto4Moure
{
    internal class Program
    {
        static void Main(string[] args)
        {
            CheckNumber(5);
            CheckNumber(50);
            CheckNumber(15);
            CheckNumber(7);
            CheckNumber(70);
            CheckNumber(18);
            CheckNumber(2);
            CheckNumber(21);
            Console.ReadKey();
        }

        /// <summary>
        /// Check number and show result
        /// </summary>
        /// <param name="num"></param>
        public static void CheckNumber(int num)
        {
            bool pair = IsPair(num);
            bool prime = IsPrime(num);
            bool fibo = IsFibonacci(num);
            Console.WriteLine($"{num} par: {pair}, prime: {prime}, fibonnacci: {fibo}");
        }

        /// <summary>
        /// Is pair number?
        /// </summary>
        /// <param name="number"></param>
        /// <returns></returns>
        public static bool IsPair(int number)
        {
            var result = (number % 2 == 0)? true: false;
            return result;
        }

        /// <summary>
        /// Is prime number?
        /// </summary>
        /// <param name="number"></param>
        /// <returns></returns>
        public static bool IsPrime(int number)
        {
            if (number <= 1) return false;
            if (number <= 3) return true;
            if (number % 2 == 0 || number % 3 == 0) return false;

            for (int i = 5; i * i <= number; i = i + 6)
            {
                if (number % i == 0 || number % (i + 2) == 0)
                {
                    return false;
                }
            }
            return true;
        }

        /// <summary>
        /// is fibonnacci this number
        /// </summary>
        /// <param name="number"></param>
        /// <returns></returns>
        public static bool IsFibonacci(int number)
        {
            int a = 0, b = 1;
            while (a < number)
            {
                int temp = a;
                a = b;
                b = temp + b;
                if (a == number) 
                    return true;
            }
            return false;
        }
    }
}
