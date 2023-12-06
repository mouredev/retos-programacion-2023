/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
namespace Generador_de_Contraseñas
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("¡Bienvenido al generador de contraseñas!");

            while (true)
            {
                Console.WriteLine("Pulse ENTER para continuar.");
                var input = Console.ReadLine();
                if (input == "")
                {
                    Generator.Parameters();
                }
                else
                {
                    Console.WriteLine("¡Uepa, debes de pulsar ENTER!");
                }
            }
        }
    }
}

//Esta es la clase que se utiliza más arriba.
namespace Generador_de_Contraseñas
{
    internal class Generator
    {
        public static void Parameters()
        {
            //Creamos una variable de tipo string donde almacenamos los char predeterminados por el generador.
            string validChars = "abcdefghijklmnopqrstuvwxyz";

            //Creamos una variable de tipo int para almacenar la dificultad de la contraseña.
            int levelPassword = 0;

            //Creamos una variable de tipo string donde más tared almacenaremos la dificultad de la contraseña.
            string finalLevel = string.Empty;

            Console.WriteLine("Escriba la longitud de su contraseña (8-16)");
            var inputLargeString = Console.ReadLine();
            //Si no se escribe nada, la longitud de la contraseña es 8.
            if (int.TryParse(inputLargeString, out int inputLargeInt))
            {
                if (inputLargeInt < 8)
                {
                    Console.WriteLine("¡Uepa! La contraseña debe de ser de mínimo 8 carácteres. Reiniciando.");
                    Generator.Parameters();
                }
                else if (inputLargeInt > 16)
                {
                    Console.WriteLine("¡Uepa! La contraseña debe de ser de un máximo de 16 carácteres. Reiniciando.");
                    Generator.Parameters();
                }
                else
                {
                    Console.WriteLine($"Su contraseña es de {inputLargeInt} carácteres.");
                }
            }
            else if (inputLargeString == "")
            {
                inputLargeInt += 8;
                Console.WriteLine($"Ha ordenado que la contraseña sea la predeterminada. Su contraseña es de {inputLargeInt} carácteres.");
            }
            else
            {
                Console.WriteLine("Error, la longitud debe de ser un número.");
                Generator.Parameters();
            }

            Console.WriteLine("¿Quiere reajustar la longitud de su contraseña?\n\nPulse ENTER para reajustar o escriba cualquier cosa para omitir.");
            var inputRegenerate = Console.ReadLine();
            if (inputRegenerate == "")
            {
                Generator.Parameters();
            }
            else
            {
                Console.WriteLine("Escriba \"1\" si quiere que la contaseña contenga mayúsculas y minúsculas o cualquier cosa si solo quiere que contenga minúsculas");
                //Creamos una variable del tipo bool (lógica) donde almacenaremos si la entrada del usuario es verdadera (1) o falsa(0).
                bool useMayus = Console.ReadLine() == "1";
                if (useMayus)
                {
                    validChars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
                    Console.WriteLine("Ha selecionado que quiere que su contraseña contenga mayúsculas y minúsculas.");
                    levelPassword++;
                }
                else if (useMayus == false)
                {
                    Console.WriteLine("Ha selecionado que quiere que su contraseña contenga solo minúsculas.");
                }
                //Hay que intentar crear una funcion de error para cuando no se escribe ni 1 ni 0.
                else
                {
                    Console.WriteLine("No ha escrito ni 1 ni 0, reiniciando el generador.");
                    Generator.Parameters();
                }

                Console.WriteLine("Escriba \"1\" si quiere que la contaseña contenga números o cualquier cosa si no quiere que contenga números.");
                bool useNumbers = Console.ReadLine() == "1";
                if (useNumbers)
                {
                    Console.WriteLine("Ha selecionado que quiere que su contraseña contenga números.");
                    validChars += "0123456789";
                    levelPassword++;
                }
                else if (useNumbers == false) 
                {
                    Console.WriteLine("Ha selecionado que quiere que su contraseña no contenga números.");
                }
                //Hay que intentar crear una funcion de error para cuando no se escribe ni 1 ni 0.
                else
                {
                    Console.WriteLine("No ha escrito ni 1 ni 0, reiniciando el generador.");
                    Generator.Parameters();
                }

                Console.WriteLine("Escriba \"1\" si quiere que su contraseña contenga símbolos o cualquier cosa si no quiere que contenga");
                bool useSigns = Console.ReadLine() == "1";
                if (useSigns)
                {
                    Console.WriteLine("Ha selecionado que quiere que su contraseña contenga símbolos");
                    validChars += "!@#$%^&*";
                    levelPassword++;
                }
                else if (useSigns == false)
                {
                    Console.WriteLine("Ha selecionado que quiere que su contraseña no contenga símbolos.");
                }
                else
                {
                    Console.WriteLine("No ha escrito ni 1 ni 0, reiniciando el generador.");
                    Generator.Parameters();
                }
                //Creamos una instancia del generador de números aleatorios.
                Random random = new Random();

                //Creamos una matriz de tipo char que más adelante guardara la contraseña.
                char[] password = new char [inputLargeInt];

                //Llenamos la matriz con char aleatorios.
                for (int i = 0; i < inputLargeInt; i++)
                {
                    password[i] = validChars[random.Next(0,validChars.Length)];
                }

                //Miramos la longitud de la contraseña y dependiendo de esta sumamos distintos valores a la variable int "levelPassword".
                if (inputLargeInt < 11)
                {
                    
                }
                else if (inputLargeInt < 14)
                {
                    levelPassword++;
                }
                else
                {
                    levelPassword++;
                    levelPassword++;
                }

                //Miramos el número de la variable levelPassword y depende de su longitud le daremos un valor o otro a la variable finalLevel.
                if (levelPassword == 1)
                {
                    finalLevel += " muy bajo";
                }
                else if (levelPassword == 2)
                {
                    finalLevel += "bajo";
                }
                else if (levelPassword == 3)
                {
                    finalLevel += "medio";
                }
                else if (levelPassword == 4)
                {
                    finalLevel += "alto";
                }
                else
                {
                    finalLevel += "muy alto";
                }

                //Convertimos la matriz en una cadena.
                string finalPassword = new string(password);
                
                Console.WriteLine($"Su contraseña es {finalPassword}.\n\nSu nivel de seguridad es {finalLevel}.");
                Console.WriteLine("¿Quiere generar otra contraseña? Pulse 0 si quiere salir o 1 si quiere otra contraseña."); 
                bool restart = Console.ReadLine() == "0";
                if (restart)
                {
                    Environment.Exit(0);
                }
                else
                {
                    Generator.Parameters();
                }
            }

        }
    }
}
