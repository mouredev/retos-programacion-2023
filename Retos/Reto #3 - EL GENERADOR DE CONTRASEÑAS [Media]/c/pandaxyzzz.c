using System;
using System.Security.Cryptography;
// hecho por puro aburrimiento
namespace GeneradorDeContrasenas
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Generador de contraseñas:");

            Console.Write("Longitud de la contraseña (entre 8 y 128 caracteres): ");
            int longitud = int.Parse(Console.ReadLine());

            if (longitud < 8 || longitud > 128)
            {
                Console.WriteLine("la longitud debe estar entre 8 y 128 caracteres.");
                return;
            }

            using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
            {
                const string caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+{}[];,.<>";

                byte[] bytes = new byte[longitud];
                rng.GetBytes(bytes);

                char[] contrasena = new char[longitud];

                for (int i = 0; i < longitud; i++)
                {
                    contrasena[i] = caracteres[bytes[i] % caracteres.Length];
                }

                Console.WriteLine("Contraseña generada: " + new string(contrasena));
            }
        }
    }
}
