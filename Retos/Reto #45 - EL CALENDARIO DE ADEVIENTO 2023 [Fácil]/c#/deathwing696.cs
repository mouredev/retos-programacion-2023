/*
 * ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
 * 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
 * Desde el 1 al 24 de diciembre.
 *
 * Crea un programa que simule el mecanismo de participación:
 * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
 *   participantes, mostrarlos, lanzar el sorteo o salir.
 * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
 * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
 *   (Y no lo duplicarás)
 * - Si seleccionas mostrar los participantes, se listarán todos.
 * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
 *   (Avisando de si lo has eliminado o el nombre no existe)
 * - Si seleccionas realizar el sorteo, elegirás una persona al azar 
 *   y se eliminará del listado.
 * - Si seleccionas salir, el programa finalizará.
 */

using System;
using System.Collections.Generic;
using System.ComponentModel.Design;
using System.Text.RegularExpressions;
using System.Threading;

namespace reto45
{
    public class Reto45
    {
        static void Main(string[] args)
        {
            int opcion;
            List<string> participantes = new List<string>();

            do
            {
                opcion = Menu();

                switch (opcion) 
                {
                    case 0:
                        break;

                    case 1:
                        Append_participante(participantes);
                        break;

                    case 2:
                        Delete_participante(participantes);
                        break;

                    case 3:
                        Console.WriteLine("Lista de participantes:");

                        foreach (var participante in participantes)
                        {
                            Console.WriteLine(participante.ToString());
                        }

                        break;

                    case 4:
                        Realizar_sorteo(participantes);
                        break;

                    default:
                        Console.WriteLine("Opción inválida, por favor introduzca una opción válida (Del 0 al 4)");
                        opcion = 5;
                        break;

                }
            } while (opcion != 0);

            Console.WriteLine("Adioooooos!");
            Console.ReadKey();
        }

        private static int Menu() 
        {
            string cadena;

            Console.WriteLine("*************************************************************");
            Console.WriteLine("** Bienvenido al calendario de aDEViento ¿Qué desea hacer? **");
            Console.WriteLine("** 1. Añadir participante                                  **");
            Console.WriteLine("** 2. Borrar participante                                  **");
            Console.WriteLine("** 3. Mostrar lista de participantes                       **");
            Console.WriteLine("** 4. Lanzar el sorteo                                     **");
            Console.WriteLine("** 0. Salir                                                **");
            Console.WriteLine("*************************************************************");

            cadena = Console.ReadLine();

            if (Int32.TryParse(cadena, out int opcion))
            {
                return opcion;
            }
            else
            {
                Console.WriteLine("Opción inválida, por favor introduzca una opción válida (Del 0 al 4)");
                return Menu();
            }
        }

        private static void Append_participante(List<string> participantes)
        {
            string participante, pattern = "^[a-zA-Zá-úÁ-Ú0-9_.]+$";
            Regex regex = new Regex(pattern);

            Console.Write("Introduce el nombre del nuevo participante:");
            participante = Console.ReadLine();

            if (regex.IsMatch(participante)) 
            {
                if (participantes.Contains(participante))
                {
                    Console.WriteLine("El participante ya existe en la lista");
                }
                else
                {
                    participantes.Add(participante);
                    Console.WriteLine("Participante añadido");
                }
            }
            else
            {
                Console.WriteLine("Por favor, introduzca un nombre de usuario válido compuesto por letras, números o los caracteres \"_\" o \".\"");
            }
        }

        private static void Delete_participante(List<string> participantes)
        {
            string participante;

            Console.WriteLine("Introduce el nombre del participante a eliminar");
            participante = Console.ReadLine();

            if (participantes.Remove(participante))
            {
                Console.WriteLine($"Participante {participante} eliminado con éxito");
            }
            else
            {
                Console.WriteLine($"El participante {participante} no existe en la lista y no ha podido ser eliminado");
            }
        }

        private static void Realizar_sorteo(List<string> participantes)
        {
            Random random = new Random();
            int ganador;

            if (participantes.Count > 0) 
            {
                Console.Write("Se va a proceder a realizar el sorteo...el ganador es...");
                ganador = random.Next(0, participantes.Count-1);
                Thread.Sleep(3000);
                Console.WriteLine($"{participantes[ganador]}");
            }
            else
            {
                Console.WriteLine("No se puede lanzar el sorteo, la lista está vacía, por favor, introduce, al menos, un participante");
            }
        }
    }
}