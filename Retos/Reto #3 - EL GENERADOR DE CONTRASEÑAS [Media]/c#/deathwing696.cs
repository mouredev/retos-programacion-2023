/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

using System;
using System.Text.RegularExpressions;

namespace deathwing696
{
    public class deathwing696
    {
        static private bool Es_valido(int num_cars)
        {
            bool ok = num_cars >= 8 && num_cars <= 16 ? true : false;

            return ok;
        }

        static private string Generate_pass(int num_cars, bool con_mayusculas, bool con_numeros, bool con_simbolos)
        {
            string password = "";
            string mayusculas = "QWERTYUIOPASDFGHJKLZXCVBNM";
            string minuscula = "qwertyuiopasdfghjklzxcvbnm";
            string numeros = "0123456789";
            string especiales = "!@#$%^&*()-_=+<,>.";
            string todos = minuscula;

            if (con_mayusculas)
                todos += mayusculas;

            if (con_numeros)
                todos += numeros;

            if (con_simbolos)
                todos += especiales;

            Random random = new Random();

            for (int i = 0; i < num_cars; i++)
            {
                int num = random.Next(0, todos.Length);

                password += todos[num];
            }

            return password;
        }

        public static void Main(string[] args)
        {
            string text;
            int num_cars;
            bool con_mayusculas, con_numeros, con_simbolos;
            Regex rx = new Regex(@"[SsNn]", RegexOptions.Compiled | RegexOptions.IgnoreCase);

            do
            {
                Console.Write("¿De cuantos caracteres quieres el password?");
                text = Console.ReadLine();

                try
                {
                    num_cars = Convert.ToInt16(text);
                }
                catch (Exception ex)
                {
                    num_cars = 0;
                }

            } while (Es_valido(num_cars) == false);

            do
            {
                Console.Write("¿Quieres que haya mayúsculas? (S/N)");
                text = Console.ReadLine();
            } while (!rx.IsMatch(text));

            if (text.Equals("S") || text.Equals("s"))
                con_mayusculas = true;
            else
                con_mayusculas = false;

            do
            {
                Console.Write("¿Quieres que hayan números? (S/N)");
                text = Console.ReadLine();
            } while (!rx.IsMatch(text));

            if (text.Equals("S") || text.Equals("s"))
                con_numeros = true;
            else
                con_numeros = false;

            do
            {
                Console.Write("¿Quieres que hayan símbolos? (S/N)");
                text = Console.ReadLine();
            } while (!rx.IsMatch(text));

            if (text.Equals("S") || text.Equals("s"))
                con_simbolos = true;
            else
                con_simbolos = false;

            Console.WriteLine(Generate_pass(num_cars, con_mayusculas, con_numeros, con_simbolos));

            Console.ReadKey();
        }
    }
}
