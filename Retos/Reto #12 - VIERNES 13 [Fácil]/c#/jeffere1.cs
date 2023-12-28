using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

namespace Reto12
{
    internal class Program{
        static void Main(string[] args)
        {
            Console.WriteLine( new jeffere1().ExisteViernes13(1,2023));
            Console.WriteLine( new jeffere1().ExisteViernes13(2,2023));
        }
    }

    public class jeffere1
    {
        public bool ExisteViernes13(int mes, int año) 
        => (int) new DateTime(año, mes, 13).DayOfWeek == 5 ?  true :  false;
    }
}