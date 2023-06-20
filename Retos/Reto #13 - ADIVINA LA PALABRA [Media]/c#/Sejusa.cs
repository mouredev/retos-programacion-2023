/*
* Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
 *   ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */

namespace Reto_13
{
    internal class Program
    {

        static void Main(string[] args)
        {
            const int totalTryes = 5; //Número de intentos.
            int attemptsLeft = totalTryes; //Número de intentos restantes.
            string originalWord = GetWord();
            string hiddenWord = HideWord(originalWord); //Ocultamos algunas letras de la palabra elegida.

            Console.WriteLine("¡Bienvenido a adivina la palabra! Pulse cualquier botón para continuar:");
            Console.ReadKey();

            while (attemptsLeft > 0)
            {
                Console.WriteLine($"\nAdivina la palabra {hiddenWord}. Tienes {attemptsLeft} intentos.");
                string guess = Console.ReadLine(); //Leemos la entrada del usuario.

                if (guess.Length == 1) //Comprobamos si la entrada es una letra y no un carácter nulo.
                {
                    char letter = guess[0]; //Obtenemos la letra introducida por el usuario.

                    if(originalWord.Contains(letter))
                    {
                        hiddenWord = UnhideLetter(originalWord, hiddenWord, letter); //Si la letra está en la palabra original, la revelamos en la palabra oculta.
                        if (hiddenWord == originalWord)
                        {
                            Console.WriteLine($"¡Felicidades, has adivinado la palabra({originalWord})! Pulse cualquier tecla para cerrar.");
                            Console.ReadKey();
                            return; //Cerramos la consola.
                        }
                    }
                    else
                    {
                        attemptsLeft--;
                    }
                }
                else if (guess.Length == originalWord.Length) //Comprobamos si la entrada es una palabra y no un carácter nulo.
                {
                    if (guess == originalWord)
                    {
                        Console.WriteLine($"¡Felicidades, has adivinado la palabra({originalWord})! Pulse cualquier tecla para cerrar.");
                        Console.ReadKey();
                        return; //Cerramos la consola.
                    }
                    else
                    {
                        attemptsLeft--;
                        
                    }
                }
                else
                {
                    Console.WriteLine("Introduce solo una letra o una palabra de la misma longitud de la palabra a adivinar.");
                }
            }
            Console.WriteLine($"Lo siento, has perdido. La palabra era {originalWord}. Pulse cualquier tecla para cerrar.");
            Console.ReadKey();
        }

        static string GetWord() //Método que muestra una palabra de una lista de manera aleatoria.
        {
            List<string> wordList = new List<string>();
            wordList.AddRange(new string[] { "hola", "mundo", "programacion", "lista", "lenguaje", "gato", "mouredev", "sejusa", "avion", "camiseta" });

            var random = new Random(); //Creamos instancia de la Random.
            var returnValue = wordList[random.Next(wordList.Count)]; //Generamos un número del 0 al número de la lista. Ese número será el índice de una palabra.
            return returnValue;
        }

        static string HideWord(string word) //Método que acepta como argumento un valor del tipo string.
        {
            char[] chars = word.ToCharArray(); //Almacenamos cada carácter de la palabra.
            int numCharsToHide = (int)Math.Ceiling(chars.Length * 0.6); //Ocultamos el 60% de los carácteres de la palabra. Math.Ceiling sirve para redondear la operación hacia arriba.

            for(int i = 0; i < numCharsToHide; i++)
            {
                int indexToHide = new Random().Next(chars.Length); //Elegimos un índice aleatorio del array de carácteres y lo almacenamos en "indexToHide".
                while (chars[indexToHide] == '_')  //Evitamos ocultar la misma letra
                {
                    indexToHide = new Random().Next(chars.Length);
                }
                chars[indexToHide] = '_'; //Si encontramos un carácter no oculto, lo reemplazamos por "_".
            }
            return new string(chars); //Creamos y devolvemos una nueva cadena con los carácteres ya ocultos.
        }

        static string UnhideLetter(string originalWord, string hiddenWord, char letter)
        {
            char[] originalChars = originalWord.ToCharArray(); //Convertimos la palabra original en un arreglo de carácteres y lo almacenamos en la variable "originalChars".
            char[] hiddenChars = hiddenWord.ToCharArray();

            for (int i = 0; i < originalChars.Length; i++)  //Recorremos el arreglo de carácteres de la palabra original.
            {
                if (originalChars[i] == letter) //Comparamos si el carácter de la posición [i] es igual al de la letra proporcionada.
                {
                    hiddenChars[i] = letter; //Si el carácter es igual a la letra proporcionada, actualizamos el arreglo de carácteres de la palabra oculta en la posición [i].
                }
            }
            return new string(hiddenChars); //Retornamos una nueva cadena creada a partir del arreglo de caráctes actualizado de la palabra oculta.
        }
    }
}
