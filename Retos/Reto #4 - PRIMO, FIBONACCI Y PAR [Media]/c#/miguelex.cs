using System;


namespace miguelex
{
    internal class Program
    {
        static void Main(string[] args)
        {
            CheckNumber(1);
            CheckNumber(2);
            CheckNumber(3);
            CheckNumber(4);
            CheckNumber(5);
            CheckNumber(6);
            CheckNumber(7);
            CheckNumber(8);
            CheckNumber(9);
            CheckNumber(10);
            CheckNumber(1024);
            CheckNumber(1358742586);
        }

        static void CheckNumber(int number)
        {
            string isPrime = isPrimeNumber(number) ? "es primo, " : "no es primo, ";
            string isEven = isEvenNumber(number) ? "es par " : "es impar ";
            string isFibonacci = isFibonacciNumber(number) ? "y es un numero de Fibonacci" : "y no es un numero de Fibonacci";

            Console.WriteLine("El numero " + number + " " + isPrime + isEven + isFibonacci);
        }

        static bool isPrimeNumber(int number)
        {
            if (number == 1) return false;
            if (number == 2) return true;
            if (number % 2 == 0) return false;
            for (int i = 3; i < number; i += 2)
            {
                if (number % i == 0) return false;
            }
            return true;
        }

        static bool isEvenNumber(int number)
        {
            return number % 2 == 0;
        }

        static bool isFibonacciNumber(int number)
        {
            int a = 0;
            int b = 1;
            while (a < number)
            {
                int temp = a;
                a = b;
                b = temp + b;
            }
            return a == number;
        }

    }

}