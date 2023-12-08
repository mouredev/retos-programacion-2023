/*
 * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente
 * desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
 */

using System;

namespace reto25
{
    public class Reto25
    {
        static void Main(string[] args)
        {
            bool codigo_konami = false;

            do
            {
                var tecla = Console.ReadKey();

                if (tecla.Key == ConsoleKey.UpArrow)
                {
                    tecla = Console.ReadKey();

                    if (tecla.Key == ConsoleKey.UpArrow)
                    {
                        tecla = Console.ReadKey();

                        if (tecla.Key == ConsoleKey.DownArrow)
                        {
                            tecla = Console.ReadKey();

                            if (tecla.Key == ConsoleKey.DownArrow)
                            {
                                tecla = Console.ReadKey();

                                if (tecla.Key == ConsoleKey.LeftArrow)
                                {
                                    tecla = Console.ReadKey();

                                    if (tecla.Key == ConsoleKey.RightArrow)
                                    {
                                        tecla = Console.ReadKey();

                                        if (tecla.Key == ConsoleKey.LeftArrow)
                                        {
                                            tecla = Console.ReadKey();

                                            if (tecla.Key == ConsoleKey.RightArrow)
                                            {
                                                tecla = Console.ReadKey();

                                                if (tecla.Key == ConsoleKey.B)
                                                {
                                                    tecla = Console.ReadKey();

                                                    if (tecla.Key == ConsoleKey.A)
                                                    {
                                                        codigo_konami = true;
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }

            } while (!codigo_konami);

            Console.WriteLine();
            Console.WriteLine("Enhorabuena! Has introducido el código Konami");

            Console.ReadKey();
        }
    }
}