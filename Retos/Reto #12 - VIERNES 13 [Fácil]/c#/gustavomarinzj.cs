using System;

namespace ViernesTrece
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(esViernesTrece("12/2022"));
            Console.WriteLine(esViernesTrece("01/2023"));
            Console.WriteLine(esViernesTrece("02/2023"));
            Console.Read();
        }

        public static bool esViernesTrece(string mes)
        {
            string dia = "13/";
            // Concatenar el día al mes y al año
            string fechaComoString = dia + mes;
            // Convertir a tipo DateTime
            DateTime fecha = DateTime.Parse(fechaComoString);
            // Obtener el nombre del día = viernes
            string resultado = fecha.ToString("dddd");

            if (resultado == "viernes")
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
}
