/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */

using System;

namespace deathwing696
{
    public class Deathwing696
    {
        private static long Convierte_decimal_a_octal(int valor_decimal)
        {
            long octal = 0;
            const int DIVISOR = 8;
            long digito = 0;

            for (int i = valor_decimal % DIVISOR, j = 0; valor_decimal > 0; valor_decimal /= DIVISOR, i = valor_decimal % DIVISOR, j++)
            {
                digito = i % DIVISOR;
                octal += digito * (long)Math.Pow(10, j);
            }


            return octal;
        }

        private static long Convierte_octal_a_decimal(long valor_octal)
        {
            int numero = 0;
            int digito = 0;
            const int DIVISOR = 10;

            for (long i = valor_octal, j = 0; i > 0; i /= DIVISOR, j++)
            {
                digito = (int)i % DIVISOR;
                if (!(digito >= 0 && digito <= 7))
                {
                    return -1;
                }
                numero += digito * (int)Math.Pow(8, j);
            }

            return numero;
        }

        public static void Main(string[] args)
        {
            int valor_decimal = 71;
            long valor_octal = 54;

            Console.WriteLine("El valor de {0} en octal es {1}", valor_decimal, Convierte_decimal_a_octal(valor_decimal));
            Console.WriteLine("El valor de {0} en decimal es {1}", valor_octal, Convierte_octal_a_decimal(valor_octal));

            Console.ReadKey();
        }
    }
}