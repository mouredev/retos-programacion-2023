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
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */


using System.Text;
bool final = false;
int totalTryes = 5;
string palabra = GetWorld();
Console.WriteLine($"Palabra: {palabra}");
int totalLetrasPalabra = palabra.Length;

var palabraoculta = OcultarPalabra(palabra);
Console.WriteLine($"Palabra oculta: {palabraoculta}");


int tries = 0;


//empieza el juego

while (!final)
{
    Console.WriteLine("Escribe una letra o la palabra oculta");
    var input= Console.ReadLine();
    if (Check(palabra, input))
    {
        if (palabra == input)
        {
            Console.WriteLine($"Has ganado, te han sobrado {totalTryes - tries} intentos");
            final = true;
        }
        else
        {
            var nuevaPalabra = UpdatePalabraOculta(palabra, input, palabraoculta);
            Console.WriteLine($"Acierto continúa! {nuevaPalabra}");
        }
    }
    else
        Console.WriteLine($"Error, sigue intentandolo, intentos restantes: {totalTryes - tries}");
    tries++;
    totalTryes--;
    if (totalTryes == 0)
        final = true;
    if (final)
        Console.WriteLine("Juego finalizado");
}

static string UpdatePalabraOculta(string palabraOriginal, string letra, string palabraOculta)
{
    string returnValue = palabraOculta;
    foreach (var x in palabraOriginal)
    {
        if (palabraOriginal.Contains(letra))
        {
            List<int> indices = new List<int>();

            for (int i = 0; i < palabraOriginal.Length; i++)
            {
                if (palabraOriginal[i].ToString() == letra)
                {
                    indices.Add(i);
                }
            }
            foreach (int indice in indices)
            {
                returnValue = returnValue.Remove(indice, 1).Insert(indice, letra);
            }
            // return palabraOculta.Replace("_",letra);
        }
    }
    return returnValue;
}
static bool Check(string palabraOriginal, string Prueba)
{
    if (palabraOriginal.Contains(Prueba))
        return true;
    else
        return false;
}
 static string GetWorld()
{
    List<string> listaDeStrings = new List<string>();
    listaDeStrings.Add("Hola");
    listaDeStrings.Add("Mundo");
    listaDeStrings.Add("Palabra");
    listaDeStrings.Add("Queso");
    listaDeStrings.Add("Camion");
    listaDeStrings.Add("Muñeco");
    listaDeStrings.Add("Español");
    listaDeStrings.Add("Lenguaje");
    listaDeStrings.Add("Ejemplo");
    listaDeStrings.Add("Camino");

    var random = new Random();
    var returnValue = listaDeStrings[random.Next(listaDeStrings.Count)];
    return returnValue;
}

static string OcultarPalabra(string palabra)
{
    var porcentajeOculto = 60; 
    var random = new Random();

    var stringBuilder = new StringBuilder(palabra.Length);
    var letrasOcultas = 0;

    foreach (var letra in palabra)
    {
        if (random.Next(100) < porcentajeOculto && letrasOcultas < palabra.Length * porcentajeOculto / 100)
        {
            stringBuilder.Append("_");
            letrasOcultas++;
        }
        else
            stringBuilder.Append(letra);
     
    }
    var palabraOculta = stringBuilder.ToString();

    return palabraOculta;
}

