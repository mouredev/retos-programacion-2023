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
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace reto45
{
    public class Reto45
    {
        static void Main(string[] args)
        {
            Concurso concurso = new Concurso();
            Concurso.Option option = Concurso.Option.Inicio;


            while (option != Concurso.Option.Salir)
            {
                option = concurso.ShowMenu();
                switch (option)
                {
                    case Concurso.Option.Mostrar:
                        concurso.Mostrar();
                        break;
                    case Concurso.Option.Anadir:
                        concurso.Anadir();
                        break;
                    case Concurso.Option.Borrar:
                        concurso.Borrar();
                        break;
                    case Concurso.Option.Lanzar:
                        concurso.Lanzar();
                        break;
                    default:
                        break;
                }

            }
        }

        public class Concurso
        {
            private List<string> participantes;

            public Concurso()
            {
                participantes = new List<string>();
            }

            public void Lanzar()
            {
                Console.WriteLine("\n********* Sorteo ****************");
                Random random = new Random();
                int indiceAleatorio = random.Next(0, participantes.Count);
                string nombreParticipante = participantes[indiceAleatorio];
                Console.WriteLine($"¡¡El ganador es {nombreParticipante}!!");

                participantes.Remove(nombreParticipante);

                Console.WriteLine("*********************************\n");

                Continuar();
            }

            private static void Continuar()
            {
                Console.WriteLine("Pulse una tecla para continuar");
                Console.ReadLine();
            }

            public void Borrar()
            {
                Console.WriteLine("\n********* Borrar participante ****************");
                Console.Write("Introduzca su nombre: ");
                string nombreParticipante = Console.ReadLine();
                if (!string.IsNullOrWhiteSpace(nombreParticipante) && participantes.Contains(nombreParticipante))
                {
                    participantes.Remove(nombreParticipante);
                    Console.WriteLine($"El participante {nombreParticipante} se ha borrado");
                }
                else
                {
                    Console.WriteLine("¡¡El participante no existe!!");
                }
                Console.WriteLine("*************************************************\n");

                Continuar();
            }

            public void Anadir()
            {
                Console.WriteLine("\n********* Añadir participante ****************");
                Console.Write("Introduzca su nombre: ");
                string nombre = Console.ReadLine();
                if (!participantes.Contains(nombre))
                {
                    participantes.Add(nombre);
                }
                else
                {
                    Console.WriteLine("¡¡Participante ya existe!!");
                }
                Console.WriteLine("*************************************************\n");

                Continuar();
            }

            public void Mostrar()
            {

                Console.WriteLine("\n********* Lista de participantes ****************");
                foreach (string participante in participantes)
                {
                    Console.WriteLine(participante);
                }
          
                Console.WriteLine("*************************************************\n");

                Continuar();
            }

            public  Option ShowMenu()
            {
                Console.Clear();

                Console.WriteLine("\n*************************");
                Console.WriteLine("0. Salir");
                Console.WriteLine("1. Mostrar participantes");
                Console.WriteLine("2. Añadir participante");
                Console.WriteLine("3. Borrar participante");
                Console.WriteLine("4. Lanzar sorteo");
                Console.WriteLine("*************************\n");
                Console.Write("Elija una opción: ");
                Option option = (Option)Enum.Parse(typeof(Option), Console.ReadLine());
                if (!Enum.IsDefined(typeof(Option), option))
                {
                    Console.WriteLine("¡¡Opcion no permitida!!");
                }

                return option;

            }

            public enum Option
            {
                Inicio = -1,
                Salir = 0,
                Mostrar = 1,
                Anadir = 2,
                Borrar = 3,
                Lanzar = 4
            }
        }
    }

}