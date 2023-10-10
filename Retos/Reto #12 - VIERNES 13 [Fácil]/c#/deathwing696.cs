/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

using System;
using System.Globalization;

namespace deathwing696
{
    public class Deathwing696
    {
        private static string Get_nombre_mes_dado_numero(int numero_mes)
        {
            try
            {
                DateTimeFormatInfo formato_fecha = CultureInfo.CurrentCulture.DateTimeFormat;

                return CultureInfo.InvariantCulture.TextInfo.ToTitleCase(formato_fecha.GetMonthName(numero_mes));
            }
            catch
            {
                return "";
            }
        }

        private static int Zeller(int q, int m, int K, int J)
        {
            if (m < 3)
            {
                m += 12;
                K -= 1;
            }
            int h = (q + 13 * (m + 1) / 5 + K + K / 4 + J / 4 - 2 * J) % 7;
            return h;
        }

        private static bool Tiene_viernes_13(int anyo, int mes)
        {
            // Ajustar el mes y el año para encajar en la fórmula
            if (mes < 3)
            {
                mes += 12;
                anyo -= 1;
            }

            // Aplicar la fórmula de Zeller para el día 13 del mes
            int dayOfWeek = Zeller(13, mes, anyo % 100, anyo / 100);

            // 6 corresponde a viernes en la fórmula de Zeller
            return dayOfWeek == 6;
        }

        public static void Main(string[] args)
        {
            int anyo = 2023, mes = 9;

            if (mes >= 1 && mes <= 12)
            {
                if (Tiene_viernes_13(anyo, mes))
                    Console.WriteLine("{0} tiene un viernes 13", Get_nombre_mes_dado_numero(mes));
                else
                    Console.WriteLine("{0} no tiene un viernes 13", Get_nombre_mes_dado_numero(mes));
            }

            anyo = 2023;
            mes = 10;

            if (mes >= 1 && mes <= 12)
            {
                if (Tiene_viernes_13(anyo, mes))
                    Console.WriteLine("{0} tiene un viernes 13", Get_nombre_mes_dado_numero(mes));
                else
                    Console.WriteLine("{0} no tiene un viernes 13", Get_nombre_mes_dado_numero(mes));
            }

            anyo = 2023;
            mes = 8;

            if (mes >= 1 && mes <= 12)
            {
                if (Tiene_viernes_13(anyo, mes))
                    Console.WriteLine("{0} tiene un viernes 13", Get_nombre_mes_dado_numero(mes));
                else
                    Console.WriteLine("{0} no tiene un viernes 13", Get_nombre_mes_dado_numero(mes));
            }

            anyo = 2023;
            mes = 1;

            if (mes >= 1 && mes <= 12)
            {
                if (Tiene_viernes_13(anyo, mes))
                    Console.WriteLine("{0} tiene un viernes 13", Get_nombre_mes_dado_numero(mes));
                else
                    Console.WriteLine("{0} no tiene un viernes 13", Get_nombre_mes_dado_numero(mes));
            }

            Console.ReadLine();
        }
    }
}
