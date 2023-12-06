using System;

/*
 * Crea una función que sea capaz de detectar si existe un viernes 13
 * en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

namespace VIERNES_13
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Viernes viernes = new Viernes();
            Console.WriteLine( viernes.isViernes13(1,2023));
            Console.WriteLine(viernes.isViernes13(2, 2023));
            Console.WriteLine(viernes.isViernes13(3, 2023));
            Console.WriteLine(viernes.isViernes13(4, 2023));
            Console.WriteLine(viernes.isViernes13(5, 2023));
            Console.WriteLine(viernes.isViernes13(6, 2023));
            Console.WriteLine(viernes.isViernes13(7, 2023));
            Console.WriteLine(viernes.isViernes13(8, 2023));
            Console.WriteLine(viernes.isViernes13(9, 2023));
            Console.WriteLine(viernes.isViernes13(10, 2023));
            Console.WriteLine(viernes.isViernes13(11, 2023));
            Console.WriteLine(viernes.isViernes13(12, 2023));
        }
    }

    public class Viernes
    {
        public string isViernes13(int mes, int año)
        {
            DateTime date = new DateTime(año, mes, 13);
            string dateString = date.ToString("dddd");
            return dateString == "viernes" ? "La fecha " + date.ToShortDateString() + " es viernes 13" : "La fecha " + date.ToShortDateString() + " no es viernes 13";
        }
    }
}
