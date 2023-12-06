using System.Text;

namespace Reto14
{
    internal class Guillermoqnk
    {
        static void Main(string[] args)
        {
            string input;

            Console.WriteLine("Introduce the number to transform: ");

            input = Console.ReadLine();

            try
            {
                Console.WriteLine("\nThe number in octal: ");
                Console.WriteLine(ConvertToOctal(Convert.ToDecimal(input)));
                Console.WriteLine("\nThe number in hexadecimal: ");
                Console.WriteLine(ConvertToHexadecimal(Convert.ToDecimal(input)));
            }
            catch { }
        }

        public static int ConvertToOctal(decimal input)
        {
            int numberToTry = (int)input;

            List<int> results = new List<int>();

            while(numberToTry >= 8)
            {
                int rest = numberToTry % 8;

                results.Add(rest);

                numberToTry = numberToTry / 8;
            }

            results.Add(numberToTry);

            StringBuilder output = new StringBuilder();

            results.Reverse();

            foreach(int result in results)
            {
                output.Append(result);
            }

            return Convert.ToInt32(output.ToString());
        }

        public static string ConvertToHexadecimal(decimal input)
        {
            Dictionary <int, string> hexaValues= new Dictionary<int, string>()
            {
                {0, "0"}, {1,"1"}, {2,"2"}, {3,"3"},  {4,"4"}, {5,"5"}, {6,"6"}, {7, "7"}, {8, "8"}, {9,"9"}, {10, "A"}, {11, "B"}, {12, "C"},{13, "D"},{14, "E"}, {15, "F"}
            };

            int numberToTry = (int)input;

            List<string> results = new List<string>();

            while (numberToTry >= 16)
            {
                int rest = numberToTry % 16;

                string hexa = String.Empty;

                if(hexaValues.TryGetValue(rest, out hexa))
                {
                    results.Add(hexa);
                }

                numberToTry = numberToTry / 16;
            }

            string hexal;

            if (hexaValues.TryGetValue((int)numberToTry, out hexal))
            {
                results.Add(hexal);
            }

            StringBuilder output = new StringBuilder();

            results.Reverse();

            foreach (string result in results)
            {
                output.Append(result);
            }

            return output.ToString();
        }
    }
}