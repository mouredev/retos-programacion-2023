using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var valores = new Dictionary<char, int>();
        for (int i = 0; i < 14; i++)
        {
            valores.Add((char)(i + 'A'), i + 1);
        }
        valores.Add('Ñ', 15);
        for (int i = 14; i < 26; i++)
        {
            valores.Add((char)(i + 'A'), i + 2);
        }

        int puntos = 0;

        while (puntos != 100)
        {
            Console.Write("Introduce una palabra: ");
            string palabra = Console.ReadLine().ToUpper();
            puntos = 0;
            foreach (char letra in palabra)
            {
                if (valores.ContainsKey(letra))
                {
                    puntos += valores[letra];
                    //Console.WriteLine($"El valor de la letra {letra} es: {valores[letra]}");
                }
            }
            Console.WriteLine("La valoración de la palabra es: " + puntos);
        }

        Console.WriteLine("¡Has alcanzado los 100 puntos!");
    }
}
