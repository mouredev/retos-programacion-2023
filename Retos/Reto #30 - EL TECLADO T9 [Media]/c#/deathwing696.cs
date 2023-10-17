/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 */

using System;
using System.Text.RegularExpressions;

namespace reto30
{
    public class Reto30
    {
        static void Main(string[] args)
        {
            string entrada1 = "6-666-88-777-33-3-33-888", entrada2 = "44-666-555-2-0-222-666-6-666-0-33-7777-8-2-7777-111";

            Console.WriteLine($"Entrada:{entrada1}");
            Console.WriteLine($"Salida:{Teclado_T9(entrada1)}");

            Console.WriteLine($"Entrada:{entrada2}");
            Console.WriteLine($"Salida:{Teclado_T9(entrada2)}");

            Console.ReadKey();
        }

        private static string Teclado_T9(string entrada)
        {
            string salida = "", pattern = @"^(\d)\1*$";
            Regex regex = new Regex(pattern);
            var pulsaciones = entrada.Split('-');
            int i = 0;

            foreach (var conjunto_letras in pulsaciones)
            {
                if (regex.IsMatch(pulsaciones[i]))
                {
                    switch(conjunto_letras[0]) 
                    {
                        case '0':
                            salida += ' ';
                            break;
                        case '1':
                            switch (conjunto_letras.Length)
                            {
                                case 1:
                                    salida += ',';
                                    break;
                                case 2:
                                    salida += '.';
                                    break;
                                case 3:
                                    salida += '?';
                                    break;
                                case 4:
                                    salida += '!';
                                    break;
                            }
                            break;
                        case '2':
                            switch (conjunto_letras.Length)
                            {
                                case 1:
                                    salida += 'A';
                                    break;
                                case 2:
                                    salida += 'B';
                                    break;
                                case 3:
                                    salida += 'C';
                                    break;
                            }
                            break;
                        case '3':
                            switch (conjunto_letras.Length)
                            {
                                case 1:
                                    salida += 'D';
                                    break;
                                case 2:
                                    salida += 'E';
                                    break;
                                case 3:
                                    salida += 'F';
                                    break;
                            }
                            break;
                        case '4':
                            switch (conjunto_letras.Length)
                            {
                                case 1:
                                    salida += 'G';
                                    break;
                                case 2:
                                    salida += 'H';
                                    break;
                                case 3:
                                    salida += 'I';
                                    break;
                            }
                            break;
                        case '5':
                            switch (conjunto_letras.Length)
                            {
                                case 1:
                                    salida += 'J';
                                    break;
                                case 2:
                                    salida += 'K';
                                    break;
                                case 3:
                                    salida += 'L';
                                    break;
                            }
                            break;
                        case '6':
                            switch (conjunto_letras.Length)
                            {
                                case 1:
                                    salida += 'M';
                                    break;
                                case 2:
                                    salida += 'N';
                                    break;
                                case 3:
                                    salida += 'O';
                                    break;
                            }
                            break;
                        case '7':
                            switch (conjunto_letras.Length)
                            {
                                case 1:
                                    salida += 'P';
                                    break;
                                case 2:
                                    salida += 'Q';
                                    break;
                                case 3:
                                    salida += 'R';
                                    break;
                                case 4:
                                    salida += 'S';
                                    break;
                            }
                            break;
                        case '8':
                            switch (conjunto_letras.Length)
                            {
                                case 1:
                                    salida += 'T';
                                    break;
                                case 2:
                                    salida += 'U';
                                    break;
                                case 3:
                                    salida += 'V';
                                    break;
                            }
                            break;
                        case '9':
                            switch (conjunto_letras.Length)
                            {
                                case 1:
                                    salida += 'W';
                                    break;
                                case 2:
                                    salida += 'X';
                                    break;
                                case 3:
                                    salida += 'Y';
                                    break;
                                case 4:
                                    salida += 'Z';
                                    break;
                            }
                            break;
                    }
                }
                else
                {
                    Console.WriteLine("Conjunto de entrada no válido");
                    salida = "";
                    break;
                }

                i++;
            }

            return salida;
        }
    }
}