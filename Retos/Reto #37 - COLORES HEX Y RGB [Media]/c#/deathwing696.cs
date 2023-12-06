/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */

using System;

namespace deathwing696
{
    public class deathwing696
    {
        private string Convierte_RGB_en_HEX(int r, int g, int b)
        {
            string hex, hex_r, hex_g, hex_b;

            hex_r = String.Format("{0:X}", r);
            hex_g = String.Format("{0:X}", g);
            hex_b = String.Format("{0:X}", b);

            hex = String.Format("#{0}{1}{2}", hex_r, hex_g, hex_b);

            return hex;
        }

        private string Convierte_HEX_en_RGB(string hex)
        {
            var cadena = hex.Replace("#", "");
            string r, g, b, valor;
            int v_r, v_g, v_b;

            r = "" + cadena[0] + cadena[1];
            g = "" + cadena[2] + cadena[3];
            b = "" + cadena[4] + cadena[5];

            v_r = Convert.ToInt32(r, 16);
            v_g = Convert.ToInt32(g, 16);
            v_b = Convert.ToInt32(b, 16);

            return String.Format("R{0}, G{1}, B{2}", v_r, v_g, v_b);
        }

        public static void Main(string[] args)
        {
            deathwing696 clase = new deathwing696();

            Console.WriteLine("Pruebas:");
            Console.WriteLine("Conversión RGB A HEX:");
            Console.WriteLine("R255, G114, B192 -> #FF72C0");
            Console.WriteLine(clase.Convierte_RGB_en_HEX(255, 114, 192));

            Console.WriteLine("Conversión RGB A HEX:");
            Console.WriteLine("102, G184, B76 -> #66B84C");
            Console.WriteLine(clase.Convierte_RGB_en_HEX(102, 184, 76));

            Console.WriteLine("Conversión HEX a RGB:");
            Console.WriteLine("#34DC95 -> R52, G220, B149");
            Console.WriteLine(clase.Convierte_HEX_en_RGB("#34DC95"));

            Console.WriteLine("Conversión HEX a RGB:");
            Console.WriteLine("#001AD6 -> R0, G26, B214");
            Console.WriteLine(clase.Convierte_HEX_en_RGB("#001AD6"));


            Console.ReadKey();
        }
    }
}