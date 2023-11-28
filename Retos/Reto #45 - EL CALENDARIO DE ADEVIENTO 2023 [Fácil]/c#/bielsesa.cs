namespace RetosProgramacion
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            new Adeviento().GestionaSorteo();
        }
    }

    internal class Adeviento
    {
        private List<string?> participantes = new();

        public void GestionaSorteo()
        {
            Console.WriteLine("#¡Buenas! Bienvenide al programa de selección de ganadores para el calendario de aDEViento 2023.#");
            string? seleccion;
            do
            {
                Console.WriteLine("""
                                  ===============================================================================================
                                  Selecciona una opción:
                                    1 - Mostrar participantes
                                    2 - Añadir participante
                                    3 - Eliminar participante
                                    4 - Realizar sorteo
                                    0 - Salir
                                  ===============================================================================================
                                  """);
                seleccion = Console.ReadLine();

                switch (seleccion)
                {
                    case "1":
                        MostrarParticipantes(true);
                        break;
                    case "2":
                        AñadirParticipante();
                        break;
                    case "3":
                        EliminarParticipante();
                        break;
                    case "4":
                        RealizarSorteo();
                        break;
                    default:
                        continue;
                }
                
            } 
            while (seleccion != null && !seleccion.Equals("0"));
            
            Console.WriteLine("#¡Que tengas un buen día!#");
            Console.WriteLine("Presiona ENTER para salir ...");
            Console.ReadLine();
        }

        private void MostrarParticipantes(bool clearConsoleOnEnter)
        {
            if (clearConsoleOnEnter) Console.Clear();
            if (!participantes.Any())
            {
                Console.WriteLine("No hay participantes actualmente.");
            }
            else
            {
                Console.WriteLine("Participantes:");
                participantes.ForEach(Console.WriteLine);
            }
            ContinueAndClearConsole();
        }

        private void AñadirParticipante()
        {
            Console.Clear();
            Console.WriteLine("Escribe el nombre del participante a añadir.");
            string? participante;

            do
            {
                participante = Console.ReadLine();
            } 
            while (string.IsNullOrWhiteSpace(participante));
            
            if (participantes.Contains(participante))
            {
                Console.WriteLine("Este participante ya existe.");
                ContinueAndClearConsole();
                return;
            }
            
            participantes.Add(participante);
            Console.WriteLine($"Se ha añadido correctamente a {participante}.");
            MostrarParticipantes(false);
        }

        private void EliminarParticipante()
        {
            Console.Clear();

            if (!participantes.Any())
            {
                Console.WriteLine("No hay ningún participante, así que no se puede eliminar ninguno.");
                ContinueAndClearConsole();
            }
            else
            {
                Console.WriteLine("¿Qué participante quieres eliminar?");
                Console.WriteLine("(Si quieres ver la lista de participantes antes, escribe 0 a continuación)");
                var participante = Console.ReadLine();

                if (participante.Equals("0"))
                {
                    participantes.ForEach(Console.WriteLine);
                    Console.WriteLine("""
                                      ------------------------------------
                                      Escribe el participante a eliminar:"
                                      ------------------------------------
                                      """);
                    participante = Console.ReadLine();
                }
                
                if (string.IsNullOrWhiteSpace(participante) || !participantes.Contains(participante))
                {
                    Console.WriteLine("Este participante no se encuentra en la lista.");
                    ContinueAndClearConsole();
                    return;
                }

                participantes.Remove(participante);
                Console.WriteLine($"Se ha eliminado correctamente a {participante}");
                
                MostrarParticipantes(false);
            }
        }

        private void RealizarSorteo()
        {
            Console.Clear();
            if (!participantes.Any() || participantes.Count == 1)
            {
                Console.WriteLine($"No se puede realizar el sorteo con {participantes.Count} participante{(participantes.Count == 1 ? string.Empty : "s")}.");
            }
            else
            {
                var ganador = participantes[new Random().Next(0, participantes.Count)];
                Console.WriteLine($"The winner is {ganador}!");
                participantes.Remove(ganador);
            }
            ContinueAndClearConsole();
        }

        private static void ContinueAndClearConsole()
        {
            Console.WriteLine("Presiona ENTER para continuar.");
            Console.ReadLine();
            Console.Clear();
        }
    }
}
