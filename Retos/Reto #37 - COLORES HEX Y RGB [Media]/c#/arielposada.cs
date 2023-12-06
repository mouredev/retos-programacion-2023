using System;

namespace Reto37
{
    class Program
    {
        public static string RgbToHex(int r, int g, int b)
        {
            return $"#{r:X2}{g:X2}{b:X2}";
        }

        public static void HexToRgb(string hex, out int r, out int g, out int b)
        {
            if (hex.StartsWith("#"))
            {
                hex = hex.Substring(1);
            }

            r = Convert.ToInt32(hex.Substring(0, 2), 16);
            g = Convert.ToInt32(hex.Substring(2, 2), 16);
            b = Convert.ToInt32(hex.Substring(4, 2), 16);
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Examples:");

            Console.WriteLine("RGB to HEX (midnight blue):");
            string hexValue = RgbToHex(25, 25, 112);
            Console.WriteLine(hexValue);

            Console.WriteLine("HEX to RGB (royal blue):");
            HexToRgb("#4169E1", out int r, out int g, out int b);
            Console.WriteLine($"(r: {r}, g: {g}, b: {b})");
        }
    }
}
