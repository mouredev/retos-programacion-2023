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

namespace Reto3Password
{
    internal class Program
    {
        public static string _characteresMinus = "abcdefghijklmnopqrstuvwxyz";// %$#@";
        public static string _characteresMayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        public static string _charactersNumbers = "0123456789";
        public static string _charactersSymbols = @"%$#@,.-;:_/*¨Ç<>^()=?¿!\";
        static void Main(string[] args)
        {
            //CapitalLetter, Numbers, Symbols, total
            var _password = Password(false, false, true, 10);
            Console.WriteLine($"Password: {_password}");
            Console.ReadKey();
        }


        /// <summary>
        /// make password
        /// </summary>
        /// <param name="capitalLetterActive"></param>
        /// <param name="numbersActive"></param>
        /// <param name="symbolsActive"></param>
        /// <param name="total"></param>
        /// <returns></returns>
        public static string Password(bool capitalLetterActive, bool numbersActive, bool symbolsActive, int total = 16)
        {
            Random rdn = new Random();
            char character;
            string password = string.Empty;

            if (total < 8 || total > 16)
                return "Error";
            string ActiveCharters = _characteresMinus;
            if (capitalLetterActive)
                ActiveCharters += _characteresMayus;
            if (numbersActive)
                ActiveCharters += _charactersNumbers;
            if (symbolsActive)
                ActiveCharters += _charactersSymbols;

            for (int i = 0; i < total; i++)
            {
                character = ActiveCharters[rdn.Next(ActiveCharters.Length)];
                password += character.ToString();
            }

            return password;
        }
    }
}
