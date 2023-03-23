/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

using System.Security.Cryptography;

public class PasswordGenerator
{
    public static void Main(string[] args)
    {
        var CreatePassword = new CreatePassword(true, true, true);
        Console.WriteLine(CreatePassword.Create());
    }

    public class CreatePassword
    {
        private readonly bool upper;
        private readonly bool number;
        private readonly bool specialCharacters;

        public CreatePassword(bool upper, bool number, bool specialCharacters)
        {
            this.upper = upper;
            this.number = number;
            this.specialCharacters = specialCharacters;
        }

        public string Create()
        {
            var random = new Random();
            var length = random.Next(8, 16);
            var bytesSeed = new byte[64];
            string refreshToken = "";
            var specialChars = "!@#$%^&*()";
            var numbers = "0123456789";
            using (var rng = RandomNumberGenerator.Create())
            {
                rng.GetBytes(bytesSeed);
                refreshToken = Convert.ToBase64String(bytesSeed).Substring(0, length);
            }

            if (this.upper)
            {
                refreshToken = refreshToken.ToUpper();
            }
            else
            {
                refreshToken = refreshToken.ToLower();
            }

            if (this.number)
            {
                for (int i = 0; i < length; i++)
                {
                    if (i % 2 == 0 && i % 7 == 0)
                    {
                        refreshToken = refreshToken.Insert(i, numbers[random.Next(0, numbers.Length)].ToString());
                    }
                }
            }

            if (this.specialCharacters)
            {
                for (int i = 0; i < length; i++)
                {
                    if (i % 3 == 0 && i % 5 == 0)
                    {
                        refreshToken = refreshToken.Insert(i, specialChars[random.Next(0, specialChars.Length)].ToString());
                    }
                }
            }

            return refreshToken;
        }
    }
}
