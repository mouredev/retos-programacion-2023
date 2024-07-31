/*
# Reto #4: PRIMO, FIBONACCI Y PAR
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

namespace program
{
    public class Prifibopar
    {
        private string Primo(int x)
        {
            int cont = 0;
            if (x <= 1)
            {
                return "No es primo, ";
            }

            for (int i = 1; i <= x; i++)
            {

                if (x % i == 0)
                {
                    cont++;
                }
            }
            if (cont > 2)
            {
                return "No es primo, ";
            }
            else
            {
                return "Es primo, ";
            }
        }
        private string fibonacci(int x)
        {
            int num1 = 0;
            int num2 = 1;
            int actual = num2;

            while (actual < x)
            {
                actual = num1 + num2;
                num1 = num2;
                num2 = actual;
            }
            if (actual == x)
            {
                return "Es fibonacci, ";
            }
            else
            {
                return "No es fibonacci, ";
            }
        }

        private string Par(int x)
        {
            if (x % 2 == 0)
            {
                return "es par";
            }
            else
            {
                return "es impar";
            }
        }

        private string Verificar(int x)
        {
            return "El numero " + x + " " + Primo(x) + fibonacci(x) + Par(x);
        }
        public static void Main(String[] args)
        {
            Prifibopar objeto = new Prifibopar();

            Console.WriteLine("Escribe un numero para ver si es primo, fibonacci y par");
            string? variable = Console.ReadLine();

            if (int.TryParse(variable, out int numero))
            {
                Console.WriteLine(objeto.Verificar(numero));
            }
            else
            {
                Console.WriteLine($"El valor {variable} ingresado no es valido");
            }


        }

    }
}