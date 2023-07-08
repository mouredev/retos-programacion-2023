string texto = "MOUREDEV - PRIMO DE LAURA MOURE (LA RULETA DE LA SUERTE)";
int desplazamiento = 3;
string textoCifrado = CifrarCesar(texto, desplazamiento);

Console.WriteLine("Texto original: " + texto);
Console.WriteLine("Texto cifrado: " + textoCifrado);


Console.WriteLine("***************");
Console.WriteLine("Descrifrando");
Console.WriteLine("***************");
string Descifrado = DescifrarCesar(textoCifrado, desplazamiento);
Console.WriteLine("Texto Descifrado: " + Descifrado);
Console.ReadKey();

static string CifrarCesar(string texto, int desplazamiento)
{
    string textoCifrado = "";

    foreach (char c in texto)
    {
        if (char.IsLetter(c))
        {
            char cifrado = (char)(((c - 'A') + desplazamiento) % 26 + 'A');
            textoCifrado += cifrado;
        }
        else
        {
            textoCifrado += c;
        }
    }
    return textoCifrado;
}

static string DescifrarCesar(string textoCifrado, int desplazamiento)
{
    string textoDescifrado = "";

    foreach (char c in textoCifrado)
    {
        if (char.IsLetter(c))
        {
            char descifrado = (char)(((c - 'A') - desplazamiento + 26) % 26 + 'A');
            textoDescifrado += descifrado;
        }
        else
        {
            textoDescifrado += c;
        }
    }

    return textoDescifrado;
}
