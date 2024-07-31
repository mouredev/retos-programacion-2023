/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
  * (Pudiendo combinar todos estos parámetros entre ellos)
 */

namespace Program
{
    public class Password
    {
        public static void Main()
        {
            string? caracters = "abcdefghijklmnopqrstuvwxyz";
            string? uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            string? numbers = "0123456789";
            string? symbols = "!@#$%^&*()_+[]|;:,.<>?";
            string? password = "";

            Console.WriteLine("Ingrese la cantidad de caracteres para la contraseña: ");
            string? longitud = Console.ReadLine();

            if (!string.IsNullOrEmpty(longitud))
            {
                int int_longitud = int.Parse(longitud);
                if (int_longitud >= 8 && int_longitud <= 16)
                {

                    Console.WriteLine("Desea agregar mayusculas y/n");
                    string? mayus = Console.ReadLine();

                    Console.WriteLine("Desea agregar numeros y/n");
                    string? numerosInput = Console.ReadLine();

                    Console.WriteLine("Desea agregar caracteres especiales y/n");
                    string? especial = Console.ReadLine();

                    if (mayus == "y")
                    {
                        caracters += uppers;
                    }
                    if (numerosInput == "y")
                    {
                        caracters += numbers;
                    }
                    if (especial == "y")
                    {
                        caracters += symbols;
                    }

                    for (int i = 0; i < int_longitud; i++)
                    {
                        Random random = new Random();
                        int randomIndex = random.Next(caracters.Length);
                        char caracterChouse = caracters[randomIndex];

                        password += caracterChouse;


                    }
                    Console.WriteLine("La contraseña es: " + password);
                }
                else
                {
                    Console.WriteLine("La longitu debe estar entre 8 y 16 caracteres");
                }
            }

        }

    }
}

