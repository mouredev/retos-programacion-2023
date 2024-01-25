namespace Reto_47
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Bienvenido a la palabra de 100 puntos.");
            Console.WriteLine("Pulse cualquier tecla para continuar.");
            Console.ReadKey(); //Esperamos hasta que se pulsa una tecla.
            CalculatePoints();
        }

        static void CalculatePoints()
        {
            string word = (Console.ReadLine()).ToLower();
            int score;
            bool error = true;
            char close;
            Console.WriteLine("Debes escribir una palabra (sin acentos) que contenga exactamente 100 puntos");

            while (error) 
            {
                word = (Console.ReadLine()).ToLower();
                score = 0;

                if (String.IsNullOrEmpty(word))
                {
                    Console.WriteLine("No puede introducir una entrada vacía.");
                }

                else if (word.Any(char.IsNumber) || !word.Any(char.IsLetter)) //Verificar si un carácter en el input "word" es un número o no es una letra.
                {
                    Console.WriteLine("Se ingresaron caracteres no válidos.");
                }

                else
                {
                    foreach (char c in word)
                    {
                        score = score + (int)c - (int)'a' + 1; //"(int)c" y "(int)'a'" se utiliza para convertir un valor de tipo char a su representación numérica en el conjunto de caracteres ASCII .
                    }

                    Console.WriteLine($"La puntuación de su palabra es: {score}");

                    if(score == 100)
                    {
                        Console.WriteLine("¡Enhorabuena! Has escrito una palabra de exactamente 100 puntos!");
                        Console.WriteLine("¿Quieres cerrar el programa? Pulsa 1 para cerrar o introduzca otra palabra...");

                        close = Console.ReadKey().KeyChar; //Acceder al carácter específico

                        if (close == '1')
                        {
                            Environment.Exit(0); //Para cerrar el programa
                        }

                    }

                    else 
                    {
                        Console.WriteLine("¡Por los pelos! Su palabra debe de ser de exactamente 100 puntos.");
                        Console.WriteLine("Introduzca otra palabra.");
                    }
                }
            }
        }
    }
}
