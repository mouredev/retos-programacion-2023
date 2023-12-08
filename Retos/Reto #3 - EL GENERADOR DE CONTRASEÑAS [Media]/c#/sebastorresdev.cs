//# Reto #3: EL GENERADOR DE CONTRASEÑAS
//#### Dificultad: Media | Publicación: 16/01/23 | Corrección: 23/01/23

//## Enunciado

/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */


using System.Text;

Console.WriteLine("*** Generador de contraseñas ***");
Console.WriteLine("--------------------------------");
Console.WriteLine(@"Ingrese la configuración que desee para su contraseña.
Cualquier otra tecla ingresada se considerara como respuesta 'NO'.");

Console.WriteLine("Seleccionar longitud [8-16]");
int length = Convert.ToInt32(Console.ReadLine());
while(length < 8 || length > 16)
{
    Console.WriteLine("Tiene que ingresar un número en el rango de 8 - 16");
    Console.WriteLine("Seleccionar longitud [8-16]");
    length = Convert.ToInt32(Console.ReadLine());
}

Console.WriteLine("Con letras mayúsculas? [S]");
bool isUppercase = Console.ReadLine()?.ToUpper() == "S";

Console.WriteLine("Con números? [S]");
bool isNumbers = Console.ReadLine()?.ToUpper() == "S";

Console.WriteLine("Con símbolos [S]");
bool isSymbol = Console.ReadLine()?.ToUpper() == "S";

string letters = "abcdefghijklmnopqrstuvwxyz";
string symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";

StringBuilder sb = new();
Random random = new();

while (sb.Length < length)
{
    sb.Append(letters[random.Next(letters.Length)]);

    if(isUppercase)
        sb.Append(letters.ToUpper()[random.Next(letters.Length)]);
    
    if(isNumbers)
        sb.Append(random.Next(10));
    
    if(isSymbol)
        sb.Append(symbols[random.Next(symbols.Length)]);
}

// muesta la contraseña generada
Console.WriteLine($"Contraseña generada: {ShuffleString(sb.ToString())}");


// Mezcla el string
string ShuffleString(string str)
{
    List<char> letter = str.ToList();
    Random _random = new();
    StringBuilder sb = new();
    int index = _random.Next(letter.Count);
    while (letter.Count > 0)
    {
        sb.Append(letter[index]);
        letter.RemoveAt(index);
        index = _random.Next(letter.Count);
    }

    return sb.ToString();
}