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


string[] preguntas = {"1. Añadir participante", "2. Borrar participante", "3. Ver lista de participantes", "4. Solteo", "5. Salir"};

Main();

void Main()
{
    int opcion = 0;
    List<string> participantes = new List<string>();
    do
    {
        Console.Clear();
        Console.WriteLine("Menú");
        Console.WriteLine("====");
        for (int i = 0; i < preguntas.Length; i++)
        {
            Console.WriteLine(preguntas[i]);
        }
        Console.Write("Elige una opción: ");
        opcion = Convert.ToInt32(Console.ReadLine());
        switch (opcion)
        {
            case 1:
                Console.Write("Introduce el nombre del participante: ");
                AnadirParticipante(participantes);
                break;
            case 2:
                BorrarParticipante(participantes);
                break;
            case 3:
                Console.WriteLine("Lista de participantes");
                Console.WriteLine("======================");
                foreach (string participante in participantes)
                {
                    Console.WriteLine(participante);
                }
                Console.WriteLine("======================");
                Console.WriteLine("Pulsa una tecla para continuar...");
                Console.ReadKey();
                break;
            case 4:
                Sorteo(participantes);
                break;
            case 5:
                Console.WriteLine("¡Hasta pronto!");
                break;
            default:
                Console.WriteLine("Opción incorrecta");
                break;
        }
    } while (opcion != 5);
}

void AnadirParticipante(List<string> participantes)
{
    Console.Write("Introduce el nombre del participante: ");
    if (!participantes.Contains(Console.ReadLine()))
    {
        participantes.Add(Console.ReadLine());
    }
    else
    {
        Console.WriteLine("El participante ya existe");
    }
    
}
void BorrarParticipante(List<string> participantes)
{
    Console.Write("Introduce el nombre del participante: ");
    if (participantes.Contains(Console.ReadLine()))
    {
        participantes.Remove(Console.ReadLine());
    }
    else
    {
        Console.WriteLine("El participante no existe");
    }
    
}

void Sorteo(List<string> participantes)
{
    var posicion = new Random().Next(0, participantes.Count);
    Console.WriteLine("El ganador es: " + participantes[posicion]);
    participantes.RemoveAt(posicion);    
    Console.WriteLine("Pulsa una tecla para continuar...");
    Console.ReadKey();
}