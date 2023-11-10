// See https://aka.ms/new-console-template for more information


/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */

using System.Collections;

static List<char> findDifference(string textOne, string textTwo)
{
    List<char> differences = new List<char>();

    if (textOne.Length == textTwo.Length)
    {
        for (int i = 0; i < textOne.Length; i++)
        {
            if (textOne[i] != textTwo[i])
            {
                differences.Add(textTwo[i]);
            }
        }
    }

    return differences;
}

var result = findDifference("Me llamo mouredev", "Me llemo mouredov");
//var result = findDifference("M", "M");

if (result.Count == 0) Console.WriteLine("[]");
else
{
    Console.Write("[");

    for (int i = 0; i < result.Count; i++)
    {
        Console.Write($"\"{result[i]}\"");

        if (i < result.Count - 1)
            Console.Write(", ");
    }

    Console.Write("]");
}