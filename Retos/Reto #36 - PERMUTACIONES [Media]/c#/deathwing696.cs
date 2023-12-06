/*
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
 */

using System;

namespace deathwing696
{
    public class deathwing696
    {
        public static void Permuta(char[] charList, int loBound, int upBound)
        {
            for (int i = loBound; i <= upBound; i++)
            {

                Intercambia(ref charList[loBound], ref charList[i]);
                if (loBound == upBound)
                {
                    Console.Write(charList);
                    Console.WriteLine("");
                }

                Permuta(charList, loBound + 1, upBound);
                Intercambia(ref charList[loBound], ref charList[i]);
            }

        }

        public static void Intercambia(ref char a, ref char b)
        {
            if (a == b) return;
            a ^= b;
            b ^= a;
            a ^= b;
        }

        public static void Main(string[] args)
        {
            string c = "hola";
            char[] c2 = c.ToCharArray();
            Permuta(c2, 0, c2.Length - 1);
            Console.ReadKey();
        }
    }
}