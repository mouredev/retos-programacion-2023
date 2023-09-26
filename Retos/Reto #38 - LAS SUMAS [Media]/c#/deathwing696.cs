/*
 * Crea una función que encuentre todas las combinaciones de los números
 * de una lista que suman el valor objetivo.
 * - La función recibirá una lista de números enteros positivos
 *   y un valor objetivo.
 * - Para obtener las combinaciones sólo se puede usar
 *   una vez cada elemento de la lista (pero pueden existir
 *   elementos repetidos en ella).
 * - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
 *   Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
 *   (Si no existen combinaciones, retornar una lista vacía)
 */

using System;
using System.Collections.Generic;

namespace deathwing696
{
    public class Deathwing696
    {
        static private List<int> lista = new List<int> { 1, 5, 3, 2 };
        static private int objetivo = 6;
        static private List<int>[] soluciones = new List<int>[Factorial(lista.Count)];
        static private int num_soluciones = 0;

        public static int Factorial(int numero)
        {
            int total = numero;

            for (int i = numero - 1; i > 0; i--)
            {
                total *= i;
            }

            return total;
        }

        public static void Permuta_y_suma(List<int> numeros, int suma, List<int> valores_usados)
        {
            if (suma == objetivo)
            {
                valores_usados.Sort();
                valores_usados.Capacity = valores_usados.Count;

                if (!Existe_fila(valores_usados))
                {
                    soluciones[num_soluciones] = new List<int>(valores_usados);
                    num_soluciones++;
                }
            }
            else
            {
                if (suma > objetivo)
                {
                    valores_usados.RemoveAt(valores_usados.Count - 1);
                }
                else
                {
                    for (int i = 0; i < numeros.Count; i++)
                    {
                        int valor = numeros[i];
                        numeros.RemoveAt(i);
                        valores_usados.Add(valor);
                        Permuta_y_suma(numeros, suma + valor, valores_usados);
                        valores_usados.Remove(valor);
                        numeros.Insert(i, valor);
                    }
                }
            }
        }

        static private bool Iguales(List<int> fila1, List<int> fila2)
        {
            if (fila1.Count == fila2.Count)
            {
                for (int i = 0; i < fila1.Count; i++)
                {
                    if (fila1[i] != fila2[i])
                        return false;
                }

                return true;
            }

            return false;
        }

        static public bool Existe_fila(List<int> fila)
        {
            for (int i = 0; i < num_soluciones; i++)
            {
                if (Iguales(soluciones[i], fila))
                    return true;
            }

            return false;
        }

        public static void Escribe_soluciones_por_pantalla()
        {
            for (int i = 0; i < num_soluciones; i++)
            {
                Console.Write("[");

                for (int j = 0; j < soluciones[i].Count; j++)
                {
                    Console.Write(soluciones[i][j]);

                    if (j < soluciones[i].Count - 1)
                        Console.Write(", ");
                }

                Console.WriteLine("]");
            }
        }

        public static void Main(string[] args)
        {
            var valores_usados = new List<int>();

            Permuta_y_suma(lista, 0, valores_usados);

            Escribe_soluciones_por_pantalla();

            Console.ReadKey();
        }
    }
}
