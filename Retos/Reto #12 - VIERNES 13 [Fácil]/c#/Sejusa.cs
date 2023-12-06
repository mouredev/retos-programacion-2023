/*
 * Crea una función que sea capaz de detectar si existe un viernes 13
 * en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

using System;

namespace Reto_12
{
    internal class Program
    {
        static void Main(string[] args)
        {
            CheckFriday13();
        }

        public static void CheckFriday13() //Función que revisa si es viernes 13 y si lo es muestra un mensaje.
        {
            DateTime today = DateTime.Today; //Creamos un objeto llamado time.
            if (today.DayOfWeek == DayOfWeek.Friday && today.Day == 13) //Comprobamos si es viernes y es dia 13, depende de lo que sea se ejecuta un código o otro.
            {
                Console.WriteLine("Ten cuidado con el coco. ¡Es viernes 13!");
            }
            else
            {
                Console.WriteLine("Estas a salvo (por el momento).");
            }

            Console.WriteLine("Para cerrar el programa, pulse cualquier botón.");
            Console.ReadKey(); //Pedimos al usuario que pulse una tecla para cerrar el programa.
        }
    }
}
