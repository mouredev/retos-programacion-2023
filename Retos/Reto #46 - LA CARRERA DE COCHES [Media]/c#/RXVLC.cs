using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/*
 * INFO IMPORTANTE:
 * COCHE 1 Y 2 = C1 y C2,
 * ARBOL = A,
 * CUANDO EL COCHE TOCA EL ARBOL SE CONVIERTE EN B y SE PARALIZA UN TURNO,
 * Meta = META
 * No He podido poner los emojis debido a mi poca experiencia.
 * Tal vez fué mi terminal , no sé
 */
namespace _46
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string coche1 = "C1";
            string coche2 = "C2";
            string meta = "META";
            var pista1 = new System.Collections.ArrayList(); // Utilizando ArrayList en lugar de Array
            var pista2 = new System.Collections.ArrayList(); // Utilizando ArrayList en lugar de Array

            int numGuiones = Convert.ToInt32(Console.ReadLine());
            for (int i = 0; i < numGuiones; i++)
            {
                if (i != 0)
                {
                    pista1.Add("_");
                    pista2.Add("_");
                }
                else
                {
                    pista1.Add(meta);
                    pista2.Add(meta);
                }
            }

            Random rnd = new Random();
            int numArboles1 = rnd.Next(1, 4);
            for (int i = 0; i < numArboles1; i++)
            {
                int posPistaArbol1 = rnd.Next(1, numGuiones);
                pista1[posPistaArbol1] = 'A';
            }
            int numArboles2 = rnd.Next(1, 4);
            for (int i = 0; i < numArboles2; i++)
            {
                int posPistaArbol2 = rnd.Next(1, numGuiones);
                pista2[posPistaArbol2] = 'A';
            }

            pista1[pista1.Count - 1] = coche1;
            pista2[pista2.Count - 1] = coche2;

            int pos1, pos2;
            pos1 = pista1.Count - 1;
            pos2 = pista2.Count - 1;
            do
            {
                if (pos1 > 0)
                {
                    int avance1 = rnd.Next(1, 4); // Determina el avance del coche 1
                    if (pista1[pos1 - 1].ToString() != "A")
                    {
                        pista1[pos1] = '_';
                        if (pos1 - avance1 < 0)
                        {
                            pos1 = 0;
                        }
                        else
                        {
                            pos1 -= avance1;
                        }
                        if (pos1 >= 0)
                        {
                            pista1[pos1] = coche1;
                        }
                    }
                    else
                    {
                        pista1[pos1 - 1] = "B";
                    }

                    Console.WriteLine($"Coche 1 se mueve {avance1} posiciones: {string.Join("", pista1.ToArray())}");
                }

                if (pos2 > 0)
                {
                    int avance2 = rnd.Next(1, 4); // Determina el avance del coche 2
                    if (pista2[pos2 - 1].ToString() != "A")
                    {
                        pista2[pos2] = '_';
                        if(pos2 -avance2 < 0)
                        {
                            pos2 = 0;
                        }
                        else
                        {
                            pos2 -= avance2;
                        }

                        if (pos2 >= 0)
                        {
                            pista2[pos2] = coche2;
                        }
                    }
                    else
                    {
                        pista2[pos2 - 1] = "B";
                    }

                    Console.WriteLine($"Coche 2 se mueve {avance2} posiciones: {string.Join("", pista2.ToArray())}");
                }

                
                Console.WriteLine("\n");
                System.Threading.Thread.Sleep(1000); // Espera de 1 segundo entre turnos
                if (pos2 <= 0 && pos1 <= 0)
                {
                    Console.WriteLine("Empate, los dos coches han llegado al mismo tiempo!");
                    break;
                }
                else if (pos1 <= 0)
                {
                    Console.WriteLine("¡El coche 1 ha llegado a la meta! ¡Gana el coche 1!");
                    break;
                }
                else if (pos2 <= 0)
                {
                    Console.WriteLine("¡El coche 2 ha llegado a la meta! ¡Gana el coche 2!");
                    break;
                }

            } while (true);


            Console.ReadKey();
        }
    }
}
