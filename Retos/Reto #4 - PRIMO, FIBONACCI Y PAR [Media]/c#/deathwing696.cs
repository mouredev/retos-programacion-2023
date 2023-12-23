/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

using System;
namespace deathwing696
{
    public class Deathwing696
    {

        private static string Es_primo(int numero)
        {
            int divisores = 0;

            for (int i = 1; i <= numero; i++)
            {
                if (numero % i == 0)
                    divisores++;
            }

            if (divisores > 2)
                return "no es primo";
            else
                return "es primo";
        }

        private static string Es_fibonacci(int numero)
        {
            int n1 = 0, n2 = 1, n3;

            if (numero == n1 || numero == n2)
            {
                return "fibonacci";
            }
            else
            {
                for (int i = 2; ; i++)
                {
                    n3 = n1 + n2;

                    if (numero == n3)
                    {
                        return "fibonacci";
                    }
                    else
                    {
                        if (n3 > numero)
                        {
                            return "no es fibonacci";
                        }
                        else
                        {
                            n1 = n2;
                            n2 = n3;
                        }
                    }
                }
            }
        }

        private static string Es_par(int numero)
        {
            if (numero % 2 == 0)
                return "es par";
            else
                return "es impar";
        }

        public static void Main(string[] args)
        {
            int numero1 = 2, numero2 = 7;
            string es_primo_1, es_primo_2, es_fibonacci_1, es_fibonacci_2, es_par_1, es_par_2;

            es_primo_1 = Es_primo(numero1);
            es_primo_2 = Es_primo(numero2);

            es_fibonacci_1 = Es_fibonacci(numero1);
            es_fibonacci_2 = Es_fibonacci(numero2);

            es_par_1 = Es_par(numero1);
            es_par_2 = Es_par(numero2);

            Console.WriteLine("{0} {1}, {2} y {3}", numero1, es_primo_1, es_fibonacci_1, es_par_1);
            Console.WriteLine("{0} {1}, {2} y {3}", numero2, es_primo_2, es_fibonacci_2, es_par_2);

            Console.ReadKey();
        }
    }
}