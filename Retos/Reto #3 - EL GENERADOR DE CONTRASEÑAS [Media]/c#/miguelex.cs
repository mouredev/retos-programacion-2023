using System;


namespace miguelex
{
    internal class Program
    {
        static void Main(string[] args)
        {
            PasswordGenerator();
            PasswordGenerator(10, true, true, true);
            PasswordGenerator(8, true);
            PasswordGenerator(16, false, true, false);
            PasswordGenerator(3, true, true, true);
            PasswordGenerator(21, true, true, true);
        }

        private static void PasswordGenerator(int size = 8, bool uppercase = false, bool digit = false, bool specials = false)
        {
            string characters = "abcdefghijklmnopqrstuvwxyz";
            string digits = "0123456789";
            string specialChars = "!@#$%^&*()_+";
            string password = "";

            if (size < 8 || size > 16)
            {
                Console.WriteLine("La clave debe tener mas de 8 caracteres y menso de 16");
                return;
            }

            if (uppercase)
            {
                characters += characters.ToUpper();
            }

            if (digit)
            {
                characters += digits;
            }

            if (specials)
            {
                characters += specialChars;
            }

            Random random = new Random();

            for (int i = 0; i < size; i++)
            {
                int randomIndex = random.Next(0, characters.Length);
                password += characters[randomIndex];
            }

            Console.WriteLine(password);
        }

    }

}