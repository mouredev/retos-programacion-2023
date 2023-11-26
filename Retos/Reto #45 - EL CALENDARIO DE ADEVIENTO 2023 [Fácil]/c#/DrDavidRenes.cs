using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DrDavidRenes
{
    class Program
    {
        static List<string> participantes = new List<string>();
        static Random random = new Random();

        static void Main(string[] args)
        {

            while (true)
            {
                MostrarMenu();
                string opcion = Console.ReadLine().ToLower();

                switch (opcion)
                {
                    case "1":
                        AñadirParticipante();
                        break;
                    case "2":
                        MostrarParticipantes();
                        break;
                    case "3":
                        EliminarParticipante();
                        break;
                    case "4":
                        RealizarSorteo();
                        break;
                    case "5":
                        Console.WriteLine("¡Hasta luego!");
                        return;
                    default:
                        Console.WriteLine("Opción no válida. Por favor, selecciona una opción válida.");
                        break;
                }
            }
        }

        static void MostrarMenu()
        {
            Console.WriteLine("===== Menú =====");
            Console.WriteLine("1. Añadir participante");
            Console.WriteLine("2. Mostrar participantes");
            Console.WriteLine("3. Eliminar participante");
            Console.WriteLine("4. Realizar sorteo");
            Console.WriteLine("5. Salir");
            Console.Write("Selecciona una opción: ");
        }

        static void AñadirParticipante()
        {
            Console.Write("Introduce el nombre del participante: ");
            string nombre = Console.ReadLine();

            if (participantes.Contains(nombre))
            {
                Console.WriteLine("¡Error! Este participante ya existe.");
            }
            else
            {
                participantes.Add(nombre);
                Console.WriteLine($"¡{nombre} ha sido añadido correctamente!");
            }
        }

        static void MostrarParticipantes()
        {
            Console.WriteLine("===== Participantes =====");
            if (participantes.Count == 0)
            {
                Console.WriteLine("No hay participantes registrados.");
            }
            else
            {
                foreach (var participante in participantes)
                {
                    Console.WriteLine(participante);
                }
            }
        }

        static void EliminarParticipante()
        {
            Console.Write("Introduce el nombre del participante a eliminar: ");
            string nombre = Console.ReadLine();

            if (participantes.Contains(nombre))
            {
                participantes.Remove(nombre);
                Console.WriteLine($"¡{nombre} ha sido eliminado correctamente!");
            }
            else
            {
                Console.WriteLine("¡Error! Este participante no existe.");
            }
        }

        static void RealizarSorteo()
        {
            if (participantes.Count == 0)
            {
                Console.WriteLine("¡Error! No hay participantes para realizar el sorteo.");
            }
            else
            {
                int indiceGanador = random.Next(participantes.Count);
                string ganador = participantes[indiceGanador];

                Console.WriteLine($"¡El ganador del sorteo es: {ganador}!");
                participantes.RemoveAt(indiceGanador);
            }
        }
    }
}
    

