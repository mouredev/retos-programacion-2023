/*
 * La última semana de 2021 comenzamos la actividad de retos de programación,
 * con la intención de resolver un ejercicio cada semana para mejorar
 * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
 *
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
 */

string alphabet = "abcdefghijklmnñopqrstuvwxyz";
string word;
int score = 0;

while(score != 100)
{
    score = 0;

    Console.WriteLine("Ingresa palabra");

    word = (Console.ReadLine() ?? string.Empty).ToLower();

    if (word == string.Empty)
    {
        Console.WriteLine("No se ingresó ninguna palabra.");
    }
    else if (word.Any(char.IsNumber) || !word.Any(char.IsLetter))
    {
        Console.WriteLine("Se ingresaron caracteres no válidos.");
    }
    else
    {

        foreach (char c in word)
        {

            if ( alphabet.Contains(c))
            {
                score = score + alphabet.IndexOf(c)+1;
            }

        }

        Console.WriteLine("Tu palabra tiene {0} puntos",score);
    
    }

    if (score == 100)
    {
        Console.WriteLine("¡Acertaste!, has ingresado una palabra de 100 puntos.");
    }
}